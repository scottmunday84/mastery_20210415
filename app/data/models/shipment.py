from pyuniqid import uniqid

from app.data.models.truck_shipment import truck_shipment
from app.main import db
from sqlalchemy import String, Float


class Shipment(db.Model):
    id = db.Column(String, primary_key=True)
    weight = db.Column(Float, default=8000)
    origin_latitude = db.Column(Float)
    origin_longitude = db.Column(Float)
    destination_latitude = db.Column(Float)
    destination_longitude = db.Column(Float)

    trucks = db.relationship('Truck', secondary=truck_shipment, backref='Shipment')

    def __init__(self, weight, origin_latitude, origin_longitude, destination_latitude, destination_longitude):
        """
        Initialize an immutable shipment.

        :param weight:
        :param origin_latitude:
        :param origin_longitude:
        :param destination_latitude:
        :param destination_longitude:
        """
        self.id = uniqid()
        self.weight = weight
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
