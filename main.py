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
            pass
        elif choice == '2':
            pass

        elif choice == '3':
            break


if __name__ == '__main__':
    main()