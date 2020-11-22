from fastapi import APIRouter, Depends, Request
from api.app.models import Infos, Restriction
from api.utils.geojson import Feature, Polygon
from api.config import settings
from typing import List
import logging
import json
import time
from api.config import settings
from fastapi import HTTPException
from asyncpg.exceptions import InternalServerError
from api.utils.here import here

import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("restrictions")

router = APIRouter()

def get_conn():
    try:
        conn = psycopg2.connect("dbname='" + settings.postgres_database + "' user='" + settings.postgres_user + "' host='" + settings.postgres_host+  "' port='" + str(settings.postgres_port) +  "' password='" + settings.postgres_password + "'")
        return conn
    except Exception as e:
        logging.error('Al intentar conectar a la BD' + str(e))
        return None

def close_conn(conn):
    try:
        conn.close()
    except Exception as e:
        logging.error("No se puede cerrar la conexion con la BD",e)

@router.get("/getinfotypes", response_model=Infos)
def getinfotypes():
    conn = get_conn()

    res = ResponseMasterTables()
    
    try:
        sql="select info_code, info_desc from taux_infos"
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if cur.rowcount > 0:
            for row in rows:
                logging.info(row)

                info = Infos()
                info.info_code = row[0]
                info.info_desc = row[1]
                res.data.append(info)
                info = None

        close_conn(conn)
        
        res.info_code = "00"
        res.info_desc = "OK"

        return res
    except InternalServerError as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e))   


@router.put("/addrestriction", response_model=Infos)
def addrestriction(restriction: Restriction):
    conn = get_conn()

    res = Infos()

    user = "jgcasta"

    point1 = "ST_GeomFromText('POINT(" + str(restriction.lon_origin) + " " + str(restriction.lat_origin) + ")',4326)"
    point2 = "ST_GeomFromText('POINT(" + str(restriction.lon_dest) + " " + str(restriction.lat_dest) + ")',4326)"
    
    ts_desired = int(time.time())
    locations = []
    vehiculo = "car"

    route = here.resolve_route(restriction.lon_origin, restriction.lat_origin, restriction.lon_dest, restriction.lat_dest, locations, vehiculo, ts_desired)
    logger.info(route)
    
    '''
    try:

        cur= conn.cursor()
        sql="INSERT INTO public.restrictions (\"user\", point_1, point_2, geom, restricted) VALUES('" + user + "', " + point1 + ", " + point2 + ", " + str(vehicle.ts_end) + ") ON CONFLICT ON CONSTRAINT taux_vehicletype_un DO update set description = '" + vehicle.description + "', ts_ini = " + str(vehicle.ts_ini) + ", ts_end = " + str(vehicle.ts_end) + " ;"
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        res.info_code = "00"
        res.info_desc = "OK"

        return res
    except Exception as e:
        close_conn(conn)
        #raise HTTPException(status_code=500, detail=str(e))   
        logging.error("Operation not completed successfully",e)
        return res
    '''

@router.delete("/deletevehicletype/{idvehicletype}", response_model=Infos)
def deletevehicletype(idvehicletype: str):
    conn = get_conn()

    res = ResponseMasterTables()
    
    try:

        cur= conn.cursor()
        sql = "update taux_vehicletype set active = False, ts_end = 1 where id ='" + idvehicletype + "';"
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        res.info_code = "00"
        res.info_desc = "OK"

        return res
    except Exception as e:

        res.info_desc = "01"
        res.info_desc = "Operation not completed successfully"
        close_conn(conn)
        #raise HTTPException(status_code=500, detail=str(e))   
        logger.error("Operation not completed successfully" , e)
        return res

