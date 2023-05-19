
class ParkingLot:
    def __init__(self, levels, capacity_per_level):
        self.levels = {level: [None] * capacity_per_level for level in levels}
        self.vehicle_parking_dict = {}
        self.free_spots = {level: capacity_per_level for level in levels}

    def park_vehicle(self, vehicle):
        pass

    def retrieve_parking_spot(self, vehicle_identifier):
        pass

    def unpark_vehicle(self, vehicle_identifier):
        pass

    def get_free_spots(self):
        return self.free_spots
