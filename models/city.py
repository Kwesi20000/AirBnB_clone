#!/usr/bin/python3
"""This module defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represents a city.

    Attributes:
        state_id (str): The state's id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
