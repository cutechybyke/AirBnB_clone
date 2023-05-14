#!/usr/bin/python3
"""This module for Review class."""

from models.base_model import BaseModel

class Review(BaseModel):
    """For class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
