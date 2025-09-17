from app.schemas.http_response_schema import HttpResponseSchema


class ResponseValidatorHelper:

    @staticmethod
    def validate_http_response(response) -> HttpResponseSchema:

        if response is None:
            return HttpResponseSchema(
                status_response=False,
                status_code=500,
                data=None,
                message="Error Service Not Operation"
            )

        if response.status_code in (200, 201):
            return HttpResponseSchema(
                status_response=True,
                status_code=response.status_code,
                data=None,
                message="Error Service Not Operation"
            )

        return HttpResponseSchema(
            status_response=False,
            status_code=response.status_code,
            data=None,
            message=response.text
        )
