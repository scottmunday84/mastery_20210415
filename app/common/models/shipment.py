from .json_encoder import JsonEncoder


class Shipment(JsonEncoder):
    ID: str
    Weight: float
    Origin_Latitude: float
    Origin_Longitude: float
    Destination_Latitude: float
    Destination_Longitude: float

    def __init__(self, id, weight, origin_latitude, origin_longitude, destination_latitude, destination_longitude):
        """
        Initialize a Shipment POPO based on the requirement doc.

        :param id:
        :param weight:
        :param origin_latitude:
        :param origin_longitude:
        :param destination_latitude:
        :param destination_longitude:
        """
        self.ID = id
        self.Weight = weight
        self.Origin_Latitude = origin_latitude
        self.Origin_Longitude = origin_longitude
        self.Destination_Latitude = destination_latitude
        self.Destination_Longitude = destination_longitude
