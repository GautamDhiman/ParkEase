
class ParkingLot:
    def __init__(self, levels, capacity_per_level):
        self.levels = {}
        self.vehicle_parking_dict = {}
        self.free_spots = {}
        self.start_spot_count_dict = {'A': 1, 'B': capacity_per_level+1}

        for level in levels:
            self.levels[level] = [None] * capacity_per_level
            self.free_spots[level] = capacity_per_level

    def park_vehicle(self, vehicle):
        for level, parking_spots in self.levels.items():
            start_spot = self.start_spot_count_dict[level]
            for i, spot in enumerate(parking_spots):
                if spot is None:
                    self.levels[level][i] = vehicle
                    vehicle.set_lot_number(start_spot + i)
                    self.vehicle_parking_dict[vehicle.identifier] = {'level': level, 'spot': start_spot + i}
                    self.free_spots[level] -= 1
                    return {'level': level, 'spot': start_spot + i}

        return None

    def retrieve_parking_spot(self, vehicle_identifier):

        if vehicle_identifier in self.vehicle_parking_dict:
            return self.vehicle_parking_dict[vehicle_identifier]
        else:
            return None


    def unpark_vehicle(self, vehicle_identifier):

        if vehicle_identifier in self.vehicle_parking_dict:
            parking_info = self.vehicle_parking_dict[vehicle_identifier]
            level = parking_info['level']
            spot = parking_info['spot']
            diff = self.start_spot_count_dict['A'] - self.start_spot_count_dict['B']

            self.levels[level][spot%diff - 1] = None
            del self.vehicle_parking_dict[vehicle_identifier]
            self.free_spots[level] += 1

            return {'level': level, 'spot': spot}
        else:
            return False

    def get_free_spots(self):
        return self.free_spots
