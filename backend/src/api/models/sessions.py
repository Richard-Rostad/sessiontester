from api.utils.database import db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    year = db.Column(db.Integer)
    content = db.Column(db.String)
    def __init__(self, title, year, content=None):
        self.title = title
        self.year = year
        self.content = content
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
class SessionSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Session
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    content = fields.String()