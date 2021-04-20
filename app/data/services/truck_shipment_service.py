from app.data.models import truck_shipment
from app.main import db


def delete_truck_shipments():
    """
    Clear out all truck shipments; this is the only mutable data in the system.

    :return:
    """
    db.session.query(truck_shipment).delete()
    db.session.commit()
