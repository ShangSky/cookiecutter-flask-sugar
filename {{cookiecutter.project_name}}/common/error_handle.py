from flask_seek import ff
from flask_sugar import RequestValidationError
from loguru import logger
from werkzeug.exceptions import HTTPException

from common.response import error_resp, resp


@ff.errorhandler(RequestValidationError)
def valid_error_handle(e: RequestValidationError) -> dict:
    return resp(code=400, msg="参数错误", data=e.errors)


@ff.errorhandler(HTTPException)
def http_error_handle(e: HTTPException) -> dict:
    return resp(code=e.code, msg=e.description)


@ff.errorhandler(Exception)
def server_error_handle(e: Exception) -> dict:
    logger.exception("Server Error")
    return error_resp()
