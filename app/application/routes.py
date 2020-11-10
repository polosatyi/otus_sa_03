# -*- coding: utf-8 -*-
import os
from copy import deepcopy
from flask import current_app as app, request, jsonify
from cerberus import Validator
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound
from .schemas import USER_SCHEMA
from .models import db, User


def user_to_dict(user):
    return {c.name: getattr(user, c.name) for c in user.__table__.columns}


@app.route("/health/")
def health():
    return '{"status": "OK"}'


@app.route("/version/")
def version():
    return '{"version": "0.2.0"}'


@app.route("/")
def hello():
    greeting = os.environ.get("GREETING", "Hello world")
    return greeting + " from " + os.environ.get("HOSTNAME", "localhost") + "!"


@app.route("/user", methods=["POST"])
def create_user():
    request_data = request.get_json()
    v = Validator(USER_SCHEMA, purge_unknown=True)
    if v.validate(request_data):
        user = User(**v.normalized(request_data))
        db.session.add(user)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            return {"code": 2, "message": "duplicate user", }, 400
        return {"id": user.id}, 200
    else:
        return {
            "code": 1,
            "message": "invalid request parameters",
            "errors": v.errors, }, 400


@app.route("/user/<int:user_id>", methods=['GET'])
def read_user(user_id):
    try:
        user = db.session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        return {"code": 3, "message": "user not found", }, 404
    return jsonify(
        {c.name: getattr(user, c.name) for c in user.__table__.columns}), 200


@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    try:
        user = db.session.query(User).filter_by(id=user_id).one()    
    except NoResultFound:
        return {"code": 3, "message": "user not found", }, 404
    request_data = request.get_json()

    # we can update any column
    put_schema = deepcopy(USER_SCHEMA)
    for key, value in put_schema.items():
        value.pop("required", None)

    v = Validator(put_schema, purge_unknown=True)
    if v.validate(request_data):
        for key, value in v.normalized(request_data).items():
            setattr(user, key, value)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            return {"code": 2, "message": "duplicate user", }, 400
    else:
        return {
            "code": 1,
            "message": "invalid request parameters",
            "errors": v.errors, }, 400
    return jsonify(
        {c.name: getattr(user, c.name) for c in user.__table__.columns}), 200


@app.route("/user/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    try:
        user = db.session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        return {"code": 3, "message": "user not found", }, 404
    db.session.delete(user)
    db.session.commit()
    return {"code": 0, "message": "success", }, 200


@app.route("/user", methods=["GET"])
def read_users():
    users = db.session.query(User).all()
    response = []
    for user in users:
        response.append(user_to_dict(user))
    return jsonify(response), 200


@app.route("/metrics", methods=["GET"])
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()
