from http import HTTPStatus

from fastapi import HTTPException


class CustomException(Exception):
    status_code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        if message:
            self.message = message


class UserAlreadyExists(HTTPException):
    def __init__(self, username: str):
        detail = f"User '{username}' already exists"
        super().__init__(status_code=400, detail=detail)
