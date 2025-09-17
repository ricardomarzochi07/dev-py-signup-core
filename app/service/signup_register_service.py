from abc import ABC, abstractmethod

from app.schemas.http_response_schema import HttpResponseSchema
from app.client.idp_app_service.wso2_schema import UserSchema


class SignupRegisterService(ABC):

    @abstractmethod
    def register_user_idp(self, data: UserSchema, access_token: str) -> HttpResponseSchema:
        pass
