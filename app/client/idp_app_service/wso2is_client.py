from buddybet_logmon_common.logger import get_logger
from buddybet_transactionmanager.http.transaction_http import HttpClient
from buddybet_transactionmanager.http.transaction_http import HttpResponseSchema
from app.client.idp_app_service.wso2is_paths import IdpPaths
from app.client.idp_app_service.wso2_schema import UserSchema


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
            return client.post(path=IdpPaths.SCIM2_USER,
                               json_data=data.model_dump(),
                               headers=headers)
        except Exception as e:
            self.logger.error("Unexpected error while preparing or sending request", exc_info=True)
            return HttpResponseSchema(
                status_response=False,
                status_code=500,
                data=None,
                message=f"Unhandled exception: {str(e)}"
            )
