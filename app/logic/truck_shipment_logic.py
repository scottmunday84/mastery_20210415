from openrouteservice import client, Client
from openrouteservice.optimization import Vehicle, Shipment, ShipmentStep

from app.common import ORS_API_KEY
from app.data.services import truck_shipment_service, truck_service, shipment_service
from app.main import app

MIN_WEIGHT = 0
MAX_WEIGHT = 8000


def validate(truck, shipment):
    """
    Validate a truck/shipment based on the requirements. Uses the typical (ok, err) tuple pattern popular in Rust.

    :param truck:
    :param shipment:
    :return:
    """
    if truck is None:
        return False, 'Truck not found.'

    if shipment is None:
        return False, 'Shipment not found.'

    if len(shipment.trucks) == 1:
        return False, 'Shipment already attached to a truck.'

    if truck.get_current_weight() + shipment.weight > truck.capacity:
        return False, 'Shipment is higher than the truck\'s capacity.'

    return True, None


def optimize(max_time_window=115200):
    """
    Using ORS, optimizes the routes between the trucks and the shipments.

    :param max_time_window:
    :return:
    """
    truck_shipment_service.delete_truck_shipments()
    trucks = truck_service.get_all()
    shipments = shipment_service.get_all()
    ors_vehicles = [Vehicle(
        id=index,
        start=[truck.origin_longitude, truck.origin_latitude],
        end=[truck.destination_longitude, truck.destination_latitude],
        skills=[1, 2],
        capacity=[truck.capacity],
        time_window=[0, max_time_window]) for index, truck in enumerate(trucks)]
    ors_shipments = [Shipment(
        pickup=ShipmentStep(
            id=index,
            location=[shipment.origin_longitude, shipment.origin_latitude]),
        delivery=ShipmentStep(
            id=index,
            location=[shipment.destination_longitude, shipment.destination_latitude]),
        skills=[1],
        amount=[shipment.weight],
        priority=1) for index, shipment in enumerate(shipments)]

    ors_client = Client(key=app.config[ORS_API_KEY])
    result = client.optimization(ors_client, vehicles=ors_vehicles, shipments=ors_shipments)

    for route in result['routes']:
        truck = trucks[route['vehicle']]
        pickup_ids = [step['id'] for step in route['steps'] if step['type'] == 'pickup']

        for pickup_id in pickup_ids:
            truck.shipments.append(shipments[pickup_id])

        truck_service.save(truck)
