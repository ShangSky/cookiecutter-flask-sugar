from typing import Any, Iterable, List

import typer
from flask_seek.util import get_objs_in_modules
from MySQLdb import OperationalError as PyMysqlOperationalError
from sqlalchemy import Index
from sqlalchemy.exc import OperationalError

from common.db import Base, engine
from models.base_model import BaseModel

cli = typer.Typer(help="数据库辅助创建cli")


def is_sub(a: Any, b: Any) -> bool:
    if a == BaseModel:
        return False
    try:
        return issubclass(a, b)
    except Exception:
        return False


def iter_models(model_names: List[str]) -> Iterable[BaseModel]:
    yield from get_objs_in_modules(
        model_names,
        BaseModel,
        deep=True,
        func=is_sub,
    )


def iter_model_index(model_names: List[str]) -> Iterable[Index]:
    for model in iter_models(model_names):
        table_args = getattr(model, "__table_args__")
        if table_args:
            for index in table_args:
                if isinstance(index, Index):
                    yield index


@cli.command()
def create_data(
    model_names: List[str] = typer.Argument(..., help="模块名以空格分割,例如:goods contact")
):
    """创建数据库表"""
    typer.echo(list(iter_models(model_names)))
    Base.metadata.create_all(engine)
    typer.echo("创建表成功")
    return "db created!"


@cli.command()
def create_index(
    model_names: List[str] = typer.Argument(..., help="模块名以空格分割,例如:goods contact")
):
    """创建索引"""
    for index in iter_model_index(model_names):
        try:
            index.create(engine)
            typer.echo(f"{index.name}索引创建成功")
        except OperationalError as e:
            orig = e.orig
            if isinstance(orig, PyMysqlOperationalError) and orig.args[0] == 1061:
                typer.echo(f"{index.name}索引已存在")


if __name__ == "__main__":
    cli()
