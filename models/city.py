#!/usr/bin/python3
"""
This conatins the class city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is City class that inherets from BaseModel
    """
    state_id = ""
    name = ""
