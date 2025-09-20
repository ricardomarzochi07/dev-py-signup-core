from abc import ABC, abstractmethod
from app.schemas.http_response_schema import HttpResponseSchema
from app.schemas.signupsubmit_request_schema import SignupSubmitRequest


class SignupRegisterService(ABC):

    @abstractmethod
    async def register_user_idp(self, user_oidc_data: SignupSubmitRequest, token: str) -> HttpResponseSchema:
        pass