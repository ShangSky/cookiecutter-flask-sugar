from typing import Any, Optional


class Status:
    OK = 200
    ERROR = 500


def resp(
    code: Optional[int] = Status.OK, msg: Optional[str] = "success", data: Any = None
) -> dict:
    return {"code": code, "msg": msg, "data": data}


def error_resp(
    code: int = Status.ERROR, msg: str = "Server Error", data: Any = None
) -> dict:
    return {"code": code, "msg": msg, "data": data}
