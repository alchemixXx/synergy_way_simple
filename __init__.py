from app import app
from config import Config
from users.routes import users
from groups.routes import courses


def run_app():
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(courses)
    return app


if __name__ == '__main__':
    run_app().run(debug=True)
