#!/usr/bin/python3
""" base_model module """
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
