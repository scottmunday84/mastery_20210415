from .json_encoder import JsonEncoder


class Truck(JsonEncoder):
    ID: str
    Capacity: float
    Origin_Latitude: float
    Origin_Longitude: float
    Destination_Latitude: float
    Destination_Longitude: float

    def __init__(self, id, capacity, origin_latitude, origin_longitude, destination_latitude, destination_longitude):
        """
        Initialize a Truck POPO based on the requirement doc.

        :param id:
        :param capacity:
        :param origin_latitude:
        :param origin_longitude:
        :param destination_latitude:
        :param destination_longitude:
        """
        self.ID = id
        self.Capacity = capacity
        self.Origin_Latitude = origin_latitude
        self.Origin_Longitude = origin_longitude
        self.Destination_Latitude = destination_latitude
        self.Destination_Longitude = destination_longitude
