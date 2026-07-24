#!/usr/bin/env python3
from pydantic import BaseModel, Field
import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(ge=3, le=10)
    name: str = Field(ge=1, le=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(datetime.datetime)
