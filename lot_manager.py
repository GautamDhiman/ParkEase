from Class import Car, ParkingLot

class ParkingLotManager:

    def __init__(self):
        levels = ['A', 'B']
        capacity_per_level = 20

        self.parking_lot = ParkingLot(levels, capacity_per_level)

    def run(self):

        while True:
            command = input("$> ")

            if command.startswith('park'):
                vehicle_identifier = command.split(' ')[1]
                self.__park_vehicle(vehicle_identifier)

            elif command.startswith('get'):
                vehicle_identifier = command.split(' ')[1]
                self.__retrieve_parking_spot(vehicle_identifier)

            elif command.startswith('unpark'):
                vehicle_identifier = command.split(' ')[1]
                self.__unpark_vehicle(vehicle_identifier)
            else:
                break

    def __park_vehicle(self, vehicle_identifier):
        vehicle = Car(vehicle_identifier)
        lot_number = self.parking_lot.park_vehicle(vehicle)

        if lot_number is None:
            print("\nSorry, parking lot is full")
        else:
            print("\n" + str(lot_number))

    def __unpark_vehicle(self, vehicle_identifier):
        result = self.parking_lot.unpark_vehicle(vehicle_identifier)

        if result:
            print("\nVehicle unparked from " + str(result))
        else:
            print("\nVehicle not found")

    def __retrieve_parking_spot(self, vehicle_identifier):
        result = self.parking_lot.retrieve_parking_spot(vehicle_identifier)

        if result:
            print("\n" + str(result))
        else:
            print("\nVehicle not found")
