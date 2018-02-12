#!/usr/bin/python3
from datetime import datetime
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
