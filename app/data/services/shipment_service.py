from sqlalchemy import not_

from app.data.models.shipment import Shipment
from app.main import db


def save(shipment):
    """
    Save a shipment.

    :param shipment:
    :return:
    """
    db.session.add(shipment)
    db.session.commit()


def get_by_id(id):
    """
    Get a shipment by ID.

    :param id:
    :return:
    """
    return Shipment.query.get(id)


def get_all():
    """
    Get all shipments.

    :return:
    """
    return Shipment.query.all()


def get_all_without_trucks():
    """
    Get all shipments without trucks.

    :return:
    """
    return Shipment.query.filter(not_(Shipment.trucks.any())).all()
