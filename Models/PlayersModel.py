from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class PlayersModel(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    from_ = db.Column(db.Integer, nullable=True)
    to_ = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String, nullable=True)
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    college = db.Column(db.String, nullable=True)

    def __init__(self, name, from_, to_, position,height,weight,birthday,college):
        self.name = name
        self.from_ = from_
        self.to_ = to_
        self.position = position
        self.height = height
        self.weight = weight
        self.birthday = birthday
        self.college = college