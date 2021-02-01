from main import db
from datetime import date


class User(db.Model):  # notice that our class extends db.Model
    __tablename__ = 'userregister'  # this is the name we want the table in database to have.
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    dateofbrith = db.Column(db.String(20), unique=False, nullable=True)
    residentialaddress = db.Column(db.String(50), unique=True, nullable=False)
    nationality = db.Column(db.String(50), unique=True, nullable=False)
    nationalidentificationnumber = db.Column(db.String(50), unique=True, nullable=False)


    # represent the object when it is queried for


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    code = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    price_per_unit = db.Column(db.Float, unique=False, nullable=False)
    # The column below i.e. product_inception_date requires import of date i.e. from datetime import date.
    # Also notice that we have set the default value to current date using the function date.today().
    product_inception_date = db.Column(db.Date, nullable=False, default=date.today())

    # represent the object when it is queried for

    def __repr__(self):
        return '<Product {}>'.format(self.id)
