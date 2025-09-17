from pydantic import BaseModel


class AppConfigEnvironment(BaseModel):
    idp_service_url: str
    domain_idp_register: str


class AppConfig(BaseModel):
    signup_core_env: AppConfigEnvironment
