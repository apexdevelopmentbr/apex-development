from base64 import b64encode
from typing import Any
from json import dumps

class ResponseEntity:

    CORS_HEADERS = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "OPTIONS, PATCH, GET, POST, PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
    }

    def __init__(self, status_code: int, body: Any, headers: dict[str, Any]=None):
        self.status_code = status_code
        self.body = body if isinstance(body, (dict, list, str)) else dumps(body, ensure_ascii=False)
        self.headers = {**self.CORS_HEADERS,
                        **(headers or {})}

    def to_lambda_response(self):
        return {
            "headers": self.headers,
            "statusCode": self.status_code,
            "body": self.body
        }

class Response:

    @staticmethod
    def ok(body:Any=None, headers: Any=None):
        return ResponseEntity(200, body, headers)

    @staticmethod
    def created(body:Any=None, headers: Any=None):
        return ResponseEntity(201, body, headers)

    @staticmethod
    def accepted(body:Any=None, headers: Any=None):
        return ResponseEntity(202, body, headers)

    @staticmethod
    def no_content(headers:Any=None):
        return ResponseEntity(204, None, headers)

    @staticmethod
    def bad_request(body:Any=None, headers:Any=None):
        return ResponseEntity(400, body, headers)

    @staticmethod
    def unathorized(body:Any=None, headers:Any=None):
        return ResponseEntity(401, body, headers)

    @staticmethod
    def forbidden(body:Any=None, headers:Any=None):
        return ResponseEntity(403, body, headers)

    @staticmethod
    def not_found(body:Any=None, headers:Any=None):
        return ResponseEntity(404, body, headers)

    @staticmethod
    def method_not_allowed(body:Any=None, headers:Any=None):
        return ResponseEntity(405, body, headers)

    @staticmethod
    def conflict(body:Any=None, headers:Any=None):
        return ResponseEntity(409, body, headers)

    @staticmethod
    def unprocessable_entity(body:Any=None, headers:Any=None):
        return ResponseEntity(422, body, headers)

    @staticmethod
    def failed_request(body:Any, status_code:int):
        return ResponseEntity(status_code, body)

    @staticmethod
    def internal_server_error(body:Any=None, headers:Any=None):
        return ResponseEntity(500, body, headers)

    @staticmethod
    def service_unavailable(body:Any=None, headers:Any=None):
        return ResponseEntity(503, body, headers)

    @staticmethod
    def base64_file(body: bytes, headers: Any=None):
        return ResponseEntity(200, {
            "encoding": "base64",
            "data": b64encode(body).decode("utf-8")
        }, headers)
