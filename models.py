from db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    created = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    group_id = db.Column(db.String, db.ForeignKey('groups.name'), nullable=False)
    group = db.Column(db.String)

    def __init__(self, username, group_id, group):
        self.username = username
        self.group_id = group_id
        self.group = group


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String(500))
    users = db.relationship('User', backref='groups', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}'
