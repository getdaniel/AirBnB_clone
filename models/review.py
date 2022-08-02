#!/usr/bin/python3
""" Defines Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents Review class.

    Attributes:
        place_id (str): The id of the Place object.
        user_id (str): The id of the User object.
        text (str): Text about review.
    """
    place_id = ""
    user_id = ""
    text = ""
