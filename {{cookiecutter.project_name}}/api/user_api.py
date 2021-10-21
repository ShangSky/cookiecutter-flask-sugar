from flask_sugar import Blueprint
from pydantic import BaseModel

from common.db import Session
from common.response import resp
from models.user_model import User

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.get("/")
def user_list():
    with Session() as session:
        users = session.query(User).limit(10).all()
    return resp(data=[{"name": u.name, "age": u.age, "id": u.id} for u in users])


class UserInfo(BaseModel):
    name: str
    age: int
    id: int


@user_bp.post("/")
def create_user(info: UserInfo):
    with Session() as session:
        user = User(name=info.name, age=info.age, id=info.id)
        session.add(user)
        session.commit()
    return resp()
