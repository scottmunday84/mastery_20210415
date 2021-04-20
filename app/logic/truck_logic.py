from app.common.models import Truck
from app.data.services import truck_service

MIN_CAPACITY = 0
MAX_CAPACITY = 48000


def validate(truck):
    """
    Validate a shipment based on the requirements. Uses the typical (ok, err) tuple pattern popular in Rust.

    :param truck:
    :return:
    """
    if type(truck.id) != str:
        return False, 'ID is invalid.'

    if type(truck.capacity) not in [int, float]:
        return False, 'Capacity is invalid.'

    if type(truck.origin_latitude) not in [int, float]:
        return False, 'Origin latitude is invalid.'

    if type(truck.origin_longitude) not in [int, float]:
        return False, 'Origin longitude is invalid.'

    if type(truck.destination_latitude) not in [int, float]:
        return False, 'Destination latitude is invalid.'

    if type(truck.destination_longitude) not in [int, float]:
        return False, 'Destination longitude is invalid.'

    if not (MIN_CAPACITY < truck.capacity <= MAX_CAPACITY):
        return False, 'Capacity is not within range.'

    return True, None


def save(truck):
    """
    Save a truck.

    :param truck:
    :return:
    """
    truck_service.save(truck)


def get_by_id(id):
    """
    Get a truck by ID.

    :param id:
    :return:
    """
    truck = truck_service.get_by_id(id)

    return Truck(
        truck.id, truck.capacity,
        truck.origin_latitude, truck.origin_longitude,
        truck.destination_latitude, truck.destination_longitude)


def get_all():
    """
    Get all trucks.

    :return:
    """
    return [Truck(
        truck.id, truck.capacity,
        truck.origin_latitude, truck.origin_longitude,
        truck.destination_latitude, truck.destination_longitude)
        for truck in truck_service.get_all()]


def get_all_without_shipments():
    """
    Get all trucks without shipments.

    :return:
    """
    return [Truck(
        truck.id, truck.capacity,
        truck.origin_latitude, truck.origin_longitude,
        truck.destination_latitude, truck.destination_longitude)
        for truck in truck_service.get_all_without_shipments()]
