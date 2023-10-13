#!/usr/bin/python3
"""
This conatins the class reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is Review class that inherets from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
