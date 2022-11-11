#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.sessions import Session,SessionSchema
from api.utils.database import db

session_routes = Blueprint("session_routes", __name__)


@session_routes.route('/', methods=['POST'])
def create_session():
    try:
        data = request.get_json()
        session_schema = SessionSchema()
        session, error = SessionSchema.load(data)
        result = session_schema.dump(session.create()).data
        return response_with(resp.SUCCESS_201, value={"session": result})
    except Exception as e:
        print (e)
        return response_with(resp.INVALID_INPUT_422)


@session_routes.route('/', methods=['GET'])
def get_session_list():
    fetched = Session.query.all()
    session_schema = SessionSchema(many=True, only=['author_id','title', 'year'])
    sessions, error = session_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"sessions": sessions})


@session_routes.route('/<int:id>', methods=['GET'])
def get_session_detail(id):
    fetched = Session.query.get_or_404(id)
    session_schema = SessionSchema()
    sessions, error = session_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"sessions": sessions})

@session_routes.route('/<int:id>', methods=['PUT'])
def update_session_detail(id):
    data = request.get_json()
    get_session = session.query.get_or_404(id)
    get_session.title = data['title']
    get_session.year = data['year']
    db.session.add(get_session)
    db.session.commit()
    session_schema = SessionSchema()
    session, error = session_schema.dump(get_session)
    return response_with(resp.SUCCESS_200, value={"session": session})

@session_routes.route('/<int:id>', methods=['PATCH'])
def modify_session_detail(id):
    data = request.get_json()
    get_session = session.query.get_or_404(id)
    if data.get('title'):
        get_session.title = data['title']
    if data.get('year'):
        get_session.year = data['year']
    db.session.add(get_session)
    db.session.commit()
    session_schema = SessionSchema()
    session, error = session_schema.dump(get_session)
    return response_with(resp.SUCCESS_200, value={"session": session})

@session_routes.route('/<int:id>', methods=['DELETE'])
def delete_session(id):
    get_session = Session.query.get_or_404(id)
    db.session.delete(get_session)
    db.session.commit()
    return response_with(resp.SUCCESS_204)