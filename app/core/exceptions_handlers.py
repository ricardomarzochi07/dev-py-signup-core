# exceptions_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from buddybet_transactionmanager.http.transaction_http import HttpResponseSchema

from app.core.exceptions import SignupCoreExceptionError, SignupCoreExceptionSuccess
from app.core.i18n_instance import i18n
from http import HTTPStatus
from typing import TypeVar

T = TypeVar('T')


def register_exception_handlers(app):
    @app.exception_handler(SignupCoreExceptionError)
    async def signup_core_exception_handler(request: Request, exc: SignupCoreExceptionError):
        message = i18n.gettext(exc.message_key)
        response_schema = HttpResponseSchema(
            status_response=False,
            status_code=exc.status_code,
            message=message,
            data=None
        )
        return JSONResponse(status_code=exc.status_code, content=response_schema.dict())


def build_success_response(e: SignupCoreExceptionSuccess, data: T) -> HttpResponseSchema:
    message = i18n.gettext(e.message_key)
    return HttpResponseSchema(
        status_response=True,
        data=data,
        status_code=HTTPStatus.OK.value,
        message=message
    )
