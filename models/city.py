#!/usr/bin/python3
""" Defines  city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents class.

    Attributes:
        state_id (str): The id of the state.
        name (str): The name of the state.
    """
    state_id = ""
    name = ""
