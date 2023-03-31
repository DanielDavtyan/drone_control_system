from http import HTTPStatus


class GenericError(Exception):
    def __init__(self, message: str = None, error_code: int = None):
        super().__init__(message)
        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.error_message = message

    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = 1000
    error_message = "An unknown error occurred"


class InvalidParameters(GenericError):
    status_code = HTTPStatus.BAD_REQUEST
    error_code = 1002
    error_message = "One or more of the received parameters is invalid"
