from flask_seek import seek
from flask_sugar import Sugar

import config


def create_app():
    app = Sugar(__name__)
    app.config.from_object(config)
    seek(app, blueprint_modules=["api"], decorator_modules=["common"])
    return app


app = create_app()


if __name__ == "__main__":
    app.run()
