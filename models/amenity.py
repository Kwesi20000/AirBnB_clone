#!/usr/bin/python3
"""This module defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
