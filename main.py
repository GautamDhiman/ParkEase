
from Class import Car, ParkingLot

def main():

    levels = ['A', 'B']
    capacity_per_level = 20

    parking_lot = ParkingLot(levels, capacity_per_level)

    while True:
        print("1. Park vehicle")
        print("2. Get lot number for vehicle")
        print("3. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            vehicle_identifier = input("Enter vehicle identifier: ")
            vehicle = Car(vehicle_identifier)
            lot_number = parking_lot.park_vehicle(vehicle)

            if lot_number is None:
                print("\nSorry, parking lot is full")
            else:
                print("\nVehicle parked at level: {}, spot: {}".format(lot_number['level'], lot_number['spot']))

        elif choice == '2':
            vehicle_identifier = input("Enter vehicle identifier: ")
            result = parking_lot.retrieve_parking_spot(vehicle_identifier)

            if result:
                print("\n" + result)
            else:
                print("\nVehicle not found")

        elif choice == '3':
            break


if __name__ == '__main__':
    main()