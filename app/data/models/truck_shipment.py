from sqlalchemy import String

from app.main import db

truck_shipment = db.Table(
    'truck_shipment',
    db.Column('truck_id', String, db.ForeignKey('truck.id')),
    db.Column('shipment_id', String, db.ForeignKey('shipment.id'), unique=True))
