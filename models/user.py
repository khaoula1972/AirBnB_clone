#!/usr/bin/python3
"""
This conatins the class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is User class that inherets from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
