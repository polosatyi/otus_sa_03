# -*- coding: utf-8 -*-
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(63), unique=True, nullable=False)
    first_name = db.Column(db.String(127), nullable=True)
    last_name = db.Column(db.String(127), nullable=True)
    email = db.Column(db.String(127), unique=True, nullable=False)
    phone = db.Column(db.String(31), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
