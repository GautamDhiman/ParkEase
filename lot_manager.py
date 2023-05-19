from Class import Car, ParkingLot

class ParkingLotManager:

    def __init__(self):
        levels = ['A', 'B']
        capacity_per_level = 20

        self.parking_lot = ParkingLot(levels, capacity_per_level)

    def run(self):

        while True:
            print("\n1. Park vehicle")
            print("2. Get lot number for vehicle")
            print("3. unpark vehicle")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                vehicle_identifier = input("Enter vehicle identifier: ")
                vehicle = Car(vehicle_identifier)
                lot_number = self.parking_lot.park_vehicle(vehicle)

                if lot_number is None:
                    print("\nSorry, parking lot is full")
                else:
                    print("\n" + str(lot_number))

            elif choice == '2':
                vehicle_identifier = input("Enter vehicle identifier: ")
                result = self.parking_lot.retrieve_parking_spot(vehicle_identifier)

                if result:
                    print("\n" + str(result))
                else:
                    print("\nVehicle not found")

            elif choice == '3':
                vehicle_identifier = input("Enter vehicle identifier: ")
                result = self.parking_lot.unpark_vehicle(vehicle_identifier)

                if result:
                    print("\nVehicle unparked from " + str(result))
                else:
                    print("\nVehicle not found")
            else:
                break
