from TranslateChat import db


class User(db.Model):
    """ USER Model"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable =False)
# TODO: Finish the database portion, 'import psycopg2'
