from fastapi import HTTPException,status


class UserNotFoundException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User not found!"

class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "User already exists with the given username!"

class InvalidUsernameOrPasswordException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = "username or password is invalid!"