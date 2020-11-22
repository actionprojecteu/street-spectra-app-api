from fastapi import APIRouter, Depends, Request
from api.services.app.models import Infos, Statistics, Statistic
from api.utils.geojson import Feature, Polygon
from api.config import settings
from typing import List
import logging
import json
import time
from datetime import datetime
from api.config import settings
from fastapi import HTTPException
from asyncpg.exceptions import InternalServerError
from api.utils.here import here
from api.utils.geojson import FeatureCollection, Feature, LineString

import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("steetspectra")

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

@router.get("/getspectrumgeojson/{id}", response_model=Feature)
def getspectrumgeojson(idrestriction: str):
    conn = get_conn()
    
    try:
        sql="select id, ST_AsGeoJSON(geom) :: json->'coordinates' AS coordinates, username, ts, heading, elevation, description from ss_spectra where id = " + id
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if cur.rowcount > 0:
            for row in rows:
                points = row[1]
                feature = Feature(properties = {"id":row[0], "username": row[2], "ts": row[3], "heading": row[4], "elevation": row[5], "description": row[6]}, geometry = LineString(coordinates = points))
        close_conn(conn)

        return feature
    except InternalServerError as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e))   

@router.get("/getrspectrageojson", response_model=FeatureCollection)
def getrspectrageojson():
    conn = get_conn()
    
    try:
        sql="select id, ST_AsGeoJSON(geom) :: json->'coordinates' AS coordinates, username, ts, heading, elevation, description from ss_spectra"
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        list_features = []
        if cur.rowcount > 0:
            for row in rows:
                points = row[1]
                feature = Feature(properties = {"id":row[0], "username": row[2], "ts": row[3], "heading": row[4], "elevation": row[5], "description": row[6]}, geometry = LineString(coordinates = points))
                list_features.append(feature)
        
        feature_collection = FeatureCollection(features = list_features)
        close_conn(conn)

        return feature_collection
    except InternalServerError as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e)) 


@router.get("/getrspectradata", response_model=FeatureCollection)
def getrspectradata():
    conn = get_conn()
    
    try:
        sql="select id, ST_x(geom) lon, ST_y(geom) lat, username, ts, heading, elevation, description from ss_spectra"
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        list_features = []
        if cur.rowcount > 0:
            for row in rows:
                points = row[1]
                feature = Feature(properties = {"idrestriction":row[0], "restircted": row[2], "user_creator": row[3], "ts_creator": row[4], "user_mod": row[5], "ts_mod": row[6], "description": row[7]}, geometry = LineString(coordinates = points))
                list_features.append(feature)
        
        feature_collection = FeatureCollection(features = list_features)
        close_conn(conn)

        return feature_collection
    except InternalServerError as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e)) 


@router.post("/addspectrum", response_model=Infos)
def addspectrum(restriction: Feature):

    conn = get_conn()

    res = Infos()

    geom = restriction.geometry.coordinates

    username = restriction.properties['usename']
    ts = restriction.properties['ts']
    heading = restriction.properties['heading']
    elevation = restriction.properties['elevation']
    description = restriction.properties['description']

    
    try:

        cur= conn.cursor()
        sql="INSERT INTO ss_spectra ( geom, username, ts, heading, description) VALUES(ST_GeomFromText('POINT( " + str_route + ")',4326),'" + str(username) + "', '" + str(ts) + "'," + str(heading) + "," + str(elevation) + ",'" + description + "') ;"
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        res.info_code = "00"
        res.info_desc = "OK"
        close_conn(conn)
        return res
    except Exception as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e))   
        logger.error("Operation not completed successfully",e)


@router.post("/getstatistics", response_model=Statistics)
def getstatistics():
    conn = get_conn()
    stat = Statistics()
    try:
        sql="select username, count(*) from ss_spectra group by username"
        cur= conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        list_features = []
        if cur.rowcount > 0:
            for row in rows:
                statictic = Statistic()
                statictic.usename = row[0]
                statictic.num_spectra = row[1]
                stat.append(statictic)
        close_conn(conn)

        return feature_collection
    except stat as e:
        close_conn(conn)
        raise HTTPException(status_code=500, detail=str(e)) 
