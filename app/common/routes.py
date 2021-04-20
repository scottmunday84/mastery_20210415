import json
from operator import methodcaller

from flask import request


def register_routes(app):
    """
    Register the routes.

    :param app:
    :return:
    """
    from app.logic import truck_shipment_logic, truck_logic, shipment_logic
    from app.data.models.truck import Truck
    from app.data.models.shipment import Shipment
    from app.data.services import truck_service, shipment_service

    @app.route('/truck', methods=['POST'])
    def create_truck():
        """
        Create a new, immutable truck.

        :return:
        """
        body = request.get_json()
        truck = Truck(**body)
        (ok, error) = truck_logic.validate(truck)

        if not ok:
            return error, 400

        truck_logic.save(truck)

        return truck.id, 200

    @app.route('/shipment', methods=['POST'])
    def create_shipment():
        """
        Create a new, immutable shipment.

        :return:
        """
        body = request.get_json()
        shipment = Shipment(**body)
        (ok, error) = shipment_logic.validate(shipment)

        if not ok:
            return error, 400

        shipment_logic.save(shipment)

        return shipment.id, 200

    @app.route('/truck/shipment', methods=['PUT'])
    def create_truck_shipment():
        """
        Create a new truck shipment. Ideally, use optimize instead.

        :return:
        """
        body = request.get_json()
        truck_id = body['truck_id']
        shipment_id = body['shipment_id']
        truck = truck_service.get_by_id(truck_id)
        shipment = shipment_service.get_by_id(shipment_id)

        (ok, error) = truck_shipment_logic.validate(truck, shipment)
        if not ok:
            return error, 400

        truck.shipments.append(shipment)
        truck_logic.save(truck)

        return '', 204

    @app.route('/trucks', methods=['GET'])
    def get_trucks():
        """
        Get all trucks.

        :return:
        """
        return json.dumps(truck_logic.get_all(), default=methodcaller('json'))

    @app.route('/trucks/no_shipments', methods=['GET'])
    def get_trucks_without_shipments():
        """
        Get all trucks without any shipments.

        :return:
        """
        return json.dumps(truck_logic.get_all_without_shipments(), default=methodcaller('json'))

    @app.route('/shipments', methods=['GET'])
    def get_shipments():
        """
        Get all shipments.

        :return:
        """
        return json.dumps(shipment_logic.get_all(), default=methodcaller('json'))

    @app.route('/shipments/no_trucks', methods=['GET'])
    def get_shipments_without_trucks():
        """
        Get all shipments without any trucks.

        :return:
        """
        return json.dumps(shipment_logic.get_all_without_trucks(), default=methodcaller('json'))

    @app.route('/trucks/shipments/optimize', methods=['GET'])
    def optimize_truck_shipments():
        """
        Optimize the trucks shipments (pickup/delivery) based on an average time allotted to the trucks on the road.

        :return:
        """
        max_time_window = request.args.get('max_time_window')
        truck_shipment_logic.optimize() \
            if max_time_window is None \
            else truck_shipment_logic.optimize(int(max_time_window))

        return '', 204
