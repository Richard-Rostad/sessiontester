from api.utils.database import db
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    tester = db.Column(db.String(32))
    duration = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    content = db.Column(db.UnicodeText)
    def __init__(self, title, tester,completed=False, content=None):
        self.title = title
        self.tester = tester
        self.completed = completed
        self.content = content
        
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
class SessionSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Session
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    tester = fields.String(required=True)
    completed = fields.Boolean()
    duration = fields.Integer()
    content = fields.Raw()
