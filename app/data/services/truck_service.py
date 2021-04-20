from sqlalchemy import not_

from app.data.models.truck import Truck
from app.main import db


def save(truck):
    """
    Save a truck.

    :param truck:
    :return:
    """
    db.session.add(truck)
    db.session.commit()


def get_by_id(id):
    """
    Get a truck by ID.

    :param id:
    :return:
    """
    return Truck.query.get(id)


def get_all():
    """
    Get all trucks.

    :return:
    """
    return Truck.query.all()


def get_all_without_shipments():
    """
    Get all trucks without shipments.

    :return:
    """
    return Truck.query.filter(not_(Truck.shipments.any())).all()
