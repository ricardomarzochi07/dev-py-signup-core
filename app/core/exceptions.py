class SignupCoreExceptionError(Exception):
    """Base class for JWT validation errors"""
    message_key = "signup_invalid_register"  # default
    status_code = 500

    def __init__(self, *args):
        super().__init__(*args)


class InvalidUserDataError(SignupCoreExceptionError):
    message_key = "invalid_user_data"
    status_code = 400


class ResourceNotFoundError(SignupCoreExceptionError):
    message_key = "resource_not_found"
    status_code = 404


class UserAlreadyExistsError(SignupCoreExceptionError):
    message_key = "user_already_exists"
    status_code = 409


class ExternalServiceError(SignupCoreExceptionError):
    message_key = "external_service_error"
    status_code = 502


class SignupCoreExceptionSuccess(Exception):
    """Base class for JWT validation errors"""
    message_key = "signup_register_success"  # default
    status_code = 200


class UserRegistrationConfirm(SignupCoreExceptionSuccess):
    message_key = "user_registration_confirm"
    status_code = 200
