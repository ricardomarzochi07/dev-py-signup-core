from fastapi import APIRouter, Depends
from app.core.environment_config import AppConfig
from app.core.settings_config import load_config
from buddybet_logmon_common.logger import get_logger
from app.schemas.signupsubmit_request_schema import SignupSubmitRequest
from app.service.impl.signup_register_service_impl import SignupRegisterServiceImpl
from buddybet_idpsecure.fastapi_authorization import FastAPIAuthorization
from buddybet_idpsecure.user_claims import UserClaims
from buddybet_transactionmanager.http.transaction_http import HttpResponseSchema

router = APIRouter()
logger = get_logger()


# auth_dependency = FastAPIAuthorization()


@router.post("/signup/user",
             response_model_exclude_none=True,
             summary="Valida Token JWT",
             responses={200: {"description": "Success", },
                        403: {"description": "Forbidden.", },
                        404: {"description": "Not Found.", },
                        500: {"description": "Error Internal.", }, }, )
async def post_register_user(data: SignupSubmitRequest,
                             user: UserClaims = Depends(FastAPIAuthorization()),
                             config: AppConfig = Depends(load_config)):
    logger.info("Execute Request - signup_submit")
    print(" +++++++++++++ USER SUB ++++++ ", user.sub)
    print(" +++++++++++++ USER  TOKEN ++++++ ", user.token)
    try:
        signup_service = SignupRegisterServiceImpl(config)
        response = signup_service.register_user_idp(user_oidc_data=data, token=user.token)
        return response
    except Exception as e:
        logger.error(f"Error register_user_idp: {e}")
        return HttpResponseSchema(
            status_response=False,
            status_code=500,
            data=None,
            message=f"Unhandled exception: {str(e)}"
        )
