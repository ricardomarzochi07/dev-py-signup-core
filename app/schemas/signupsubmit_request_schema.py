from pydantic import BaseModel


class SignupSubmitRequest(BaseModel):
    firstName: str
    lastName: str
    gender: str
    email: str
    username: str
    password: str
