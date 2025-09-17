from pydantic import BaseModel

from typing import List
from pydantic import BaseModel, EmailStr
import json


class Name(BaseModel):
    givenName: str
    familyName: str


class Email(BaseModel):
    primary: bool
    value: EmailStr
    type: str


class UserSchema(BaseModel):
    userName: str
    password: str
    name: Name
    emails: List[Email]

    # Método para convertir el DTO a dict
    def to_dict(self):
        return self.dict()

    # Método para convertir el DTO a JSON
    def to_json(self):
        return self.json()

    # Método de clase para crear el DTO desde un JSON string
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(**data)
