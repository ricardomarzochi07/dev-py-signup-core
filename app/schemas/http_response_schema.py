from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class HttpResponseSchema(Generic[T]):

    def __init__(self, status_response: bool = False, status_code: int = 0, data: Optional[T] = None,
                 message: str = None):
        self.status_response: bool = status_response
        self.status_code: int = status_code
        self.data: Optional[T] = data
        self.message: str = message

    def to_dict(self):
        return {
            "data": self.data,
            "message": self.message,
            "status_code": self.status_code,
            "status_response": self.status_response
        }
