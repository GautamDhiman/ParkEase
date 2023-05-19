
class Vehicle:

    def __init__(self, identifier, vehicle_type, assigned_lot=None):
        self.identifier = identifier
        self.vehicle_type = vehicle_type
        self.assigned_lot = assigned_lot

    def get_lot_number(self):
        return self.assigned_lot

    def set_lot_number(self, lot_number):
        self.assigned_lot = lot_number


