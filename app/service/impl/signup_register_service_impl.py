from app.client.idp_app_service.wso2_schema import UserSchema, Name, Email
from app.client.idp_app_service.wso2is_client import Wso2isClient
from app.schemas.http_response_schema import HttpResponseSchema
from app.schemas.signupsubmit_request_schema import SignupSubmitRequest
from app.service.signup_register_service import SignupRegisterService
from buddybet_logmon_common.logger import get_logger
from app.core.environment_config import AppConfig


class SignupRegisterServiceImpl(SignupRegisterService):
    logger = get_logger()

    def __init__(self, config: AppConfig):
        self.env_var = config.signup_core_env

    def register_user_idp(self, user_oidc_data: SignupSubmitRequest, token: str) -> HttpResponseSchema:
        self.logger.info("Execute Request - register_user_idp")
        try:
            # Crear instancia de SignupCoreServiceSchema solo con atributos comunes
            user_idp_data = UserSchema(
                userName=self.env_var.domain_idp_register+user_oidc_data.username,
                password=user_oidc_data.password,
                name=Name(
                    givenName=user_oidc_data.firstName,
                    familyName=user_oidc_data.lastName
                ),
                emails=[Email(
                    primary=True,
                    value=user_oidc_data.email,
                    type="home")]
            )

            client = Wso2isClient()
            response = client.post_register_user_in_idp(
                data=user_idp_data,
                access_token=token,
                url=self.env_var.idp_service_url
            )
            # Validación centralizada
            return response
        except Exception as e:
            self.logger.error(f"Error register_user_idp: {e}")
            return HttpResponseSchema(
                status_response=False,
                status_code=500,
                data=None,
                message=f"Unhandled exception: {str(e)}"
            )