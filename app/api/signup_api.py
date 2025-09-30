from fastapi import APIRouter, Depends
from app.core.environment_config import AppConfig
from app.core.exceptions import UserRegistrationConfirm
from app.core.exceptions_handlers import build_success_response
from app.core.settings_config import load_config
from buddybet_logmon_common.logger import get_logger
from app.schemas.signupsubmit_request_schema import SignupSubmitRequest
from app.service.impl.signup_register_service_impl import SignupRegisterServiceImpl
from buddybet_idpsecure.authorization.fastAPI_auth import FastAPIAuthorization
from buddybet_idpsecure.model.user_claims import UserClaims

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
    signup_service = SignupRegisterServiceImpl(config)
    response = await signup_service.register_user_idp(user_oidc_data=data, token=user.token)
    return build_success_response(e=UserRegistrationConfirm, data=response)
