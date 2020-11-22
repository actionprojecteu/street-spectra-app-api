from enum import Enum
from pydantic import BaseModel, validator, root_validator, Field
from pydantic.types import conint
from typing import List, Optional, Union, Dict
from datetime import datetime
from uuid import uuid4
from api.utils.geojson import Feature, FeatureCollection

class Infos(BaseModel):
    info_code: str = ""
    info_desc: str = ""


class Restriction(BaseModel):
    id: int = 0
    user: str = ""
    token_user: str = ""
    lon_origin: float = 0
    lat_origin: float = 0
    lon_dest: float = 0
    lat_dest: float = 0
    restricted: bool = True
    description: str = ""

class ResponseRestriction(BaseModel):
    geojson: Feature = ""

class ResponseRestrictions(BaseModel):
    geojson: FeatureCollection = ""

class Statistics(BaseModel):
    statistic: List = []

class Statistic(BaseModel):
    username: str = ""
    num_spectra: int = 0
