from buddybet_logmon_common.logger import get_logger
from buddybet_transactionmanager.http.transaction_http import HttpClient
from buddybet_transactionmanager.schemas.http_response_schema import HttpResponseSchema
from app.client.idp_app_service.wso2is_paths import IdpPaths
from app.client.idp_app_service.wso2_schema import UserSchema
from app.core.exceptions import InvalidUserDataError, ResourceNotFoundError, ExternalServiceError, \
    UserAlreadyExistsError
from typing import Optional


class Wso2isClient:
    logger = get_logger()

    async def post_register_user_in_idp(self, data: UserSchema, access_token: str, url_base: str) -> HttpResponseSchema:
        self.logger.info("Execute Request - post_register_user")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        try:
            client = HttpClient(url_base, cert=None, verify=False)
            response = client.post(path=IdpPaths.SCIM2_USER,
                                   json_data=data.model_dump(),
                                   headers=headers)

            if response.data is None:
                self.logger.error("No se recibió respuesta del servicio IDP.")
                raise ExternalServiceError("Respuesta nula del IDP")

            if not response.status_response:
                if response.status_code == 400:
                    raise InvalidUserDataError()
                elif response.status_code == 404:
                    raise ResourceNotFoundError()
                elif response.status_code == 409:
                    await self._parse_response_code_409_http(response.data)
                else:
                    raise ExternalServiceError()
            return response

        except UserAlreadyExistsError:
            self.logger.warning("The user is already registered in the system..")
            raise
        except Exception as e:
            self.logger.error("Error de red al comunicar con Alta de Clientes", exc_info=True)
            raise ExternalServiceError() from e

    async def _parse_response_code_409_http(self, data: Optional[dict]):

        detail = data.get("detail", "") if data else ""
        if "already exists in the system" in detail:
            raise UserAlreadyExistsError()
        else:
            self.logger.error(f"Error inesperado al registrar usuario: {detail}")
            raise ExternalServiceError()
