# ParkEase
Parking Lot app

## Getting Started
```bash
git clone
cd ParkEase
python3 main.py
```

## Supported features
- park
- retrieve parking spot by vehicle number
- unpark vehicle

## Commands
```bash
- park <vehicle_identifier> ## assign slot to vehicle
- get <vehicle_identifier> ## get assigned slot for vehicle
- unpark <vehicle_identifier> ## remove vehicle from slot
```

## project structure
```
├── README.md
├── main.py
├── lot_manager.py
├── Class
│   ├── __init__.py
│   ├── lot.py
│   ├── car.py
│   ├── vehicle.py