
class ParkingLot:
    def __init__(self, levels, capacity_per_level):
        self.levels = {level: [None] * capacity_per_level for level in levels}
        self.vehicle_parking_dict = {}
        self.free_spots = {level: capacity_per_level for level in levels}

    def park_vehicle(self, vehicle):
        for level, parking_spots in self.levels.items():
            for i, spot in enumerate(parking_spots):
                if spot is None:
                    self.levels[level][i] = vehicle
                    vehicle.set_lot_number(i + 1)
                    self.vehicle_parking_dict[vehicle.identifier] = {'level': level, 'spot': i + 1}
                    self.free_spots[level] -= 1
                    return {'level': level, 'spot': i + 1}

        return None

    def retrieve_parking_spot(self, vehicle_identifier):
        pass

    def unpark_vehicle(self, vehicle_identifier):
        pass

    def get_free_spots(self):
        return self.free_spots
