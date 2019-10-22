from app import app
from config import Config
from db import db
from groups.routes import groups
from users.routes import users


def run_app():
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(groups)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app


if __name__ == '__main__':
    run_app().run(debug=True)
