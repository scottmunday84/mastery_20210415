from pyuniqid import uniqid
from app.data.models.truck_shipment import truck_shipment
from app.main import db
from sqlalchemy import String, Float


class Truck(db.Model):
    id = db.Column(String, primary_key=True)
    capacity = db.Column(Float, default=48000)
    origin_latitude = db.Column(Float)
    origin_longitude = db.Column(Float)
    destination_latitude = db.Column(Float)
    destination_longitude = db.Column(Float)

    shipments = db.relationship('Shipment', secondary=truck_shipment, backref='Truck')

    def get_current_weight(self):
        """
        Get the current weight based on the shipment on the truck.

        :return:
        """
        return sum([shipment.weight for shipment in self.shipments])

    def __init__(self, capacity=None, origin_latitude=None, origin_longitude=None, destination_latitude=None, destination_longitude=None):
        """
        Initialize an immutable truck.

        :param capacity:
        :param origin_latitude:
        :param origin_longitude:
        :param destination_latitude:
        :param destination_longitude:
        """
        self.id = uniqid()
        self.capacity = capacity
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
