from app.common.models import Shipment
from app.data.services import shipment_service

MIN_WEIGHT = 0
MAX_WEIGHT = 8000


def validate(shipment):
    """
    Validate a shipment based on the requirements. Uses the typical (ok, err) tuple pattern popular in Rust.

    :param shipment:
    :return:
    """
    if type(shipment.id) != str:
        return False, 'ID is invalid.'

    if type(shipment.weight) not in [int, float]:
        return False, 'Weight is invalid.'

    if type(shipment.origin_latitude) not in [int, float]:
        return False, 'Origin latitude is invalid.'

    if type(shipment.origin_longitude) not in [int, float]:
        return False, 'Origin longitude is invalid.'

    if type(shipment.destination_latitude) not in [int, float]:
        return False, 'Destination latitude is invalid.'

    if type(shipment.destination_longitude) not in [int, float]:
        return False, 'Destination longitude is invalid.'

    if not (MIN_WEIGHT < shipment.weight <= MAX_WEIGHT):
        return False, 'Weight is not within range.'

    return True, None


def save(shipment):
    """
    Save a shipment.

    :param shipment:
    :return:
    """
    shipment_service.save(shipment)


def get_by_id(id):
    """
    Get a shipment by ID.

    :param id:
    :return:
    """
    shipment = shipment_service.get_by_id(id)

    return Shipment(
        shipment.id, shipment.weight,
        shipment.origin_latitude, shipment.origin_longitude,
        shipment.destination_latitude, shipment.destination_longitude)


def get_all():
    """
    Get all shipments.

    :return:
    """
    return [Shipment(
        shipment.id, shipment.weight,
        shipment.origin_latitude, shipment.origin_longitude,
        shipment.destination_latitude, shipment.destination_longitude)
        for shipment in shipment_service.get_all()]


def get_all_without_trucks():
    """
    Get all shipments without trucks.

    :return:
    """
    return [Shipment(
        shipment.id, shipment.weight,
        shipment.origin_latitude, shipment.origin_longitude,
        shipment.destination_latitude, shipment.destination_longitude)
        for shipment in shipment_service.get_all_without_trucks()]
