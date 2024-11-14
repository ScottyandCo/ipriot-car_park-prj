import random
from datetime import datetime
from car_park import CarPark
from display import Display
from sensor import SensorEnter, SensorExit

# Create objects required for the car park
car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
entry_sensor = SensorEnter(1,True, car_park)
exit_sensor = SensorExit(2,True, car_park)
display = Display(1, "Welcome to Moondalup", True, car_park)

# write config of CarPark to JSON file
car_park.write_config()

temperature = random.randint(21,38)
weather = random.choice(["sunny ☀️", "overcast 🌤️", "raining 🌧️"])
time = datetime.now().strftime("%H:%M")


def welcome_message(car_park, display):
    """
    Print a welcome message with information about the car park and current conditions.
    :param car_park: the CarPark() object to access methods
    :param display: the Display() object to access methods
    """
    print("\n" + "|" + "*" * 60)
    print(f"| {display.message}.\n| Our maximum capacity is {car_park.capacity} vehicles.\n| It is currently {time}, {temperature}c and {weather}.")
    print("*" * 61)

def message(car_park):
    print(f"The car park currently has {car_park.available_bays} bays available")

def enter_car_park(car_park, sensor):
    """
    Send a specific number of vehicles trough Entry Sensor. The number is defined by the range(int)
    Print capacity information before the vehicle enters the car park.
    :param car_park: the CarPark() object to access methods
    :param sensor: the SensorEnter() object to access methods
    """
    for i in range(10):
        print()
        message(car_park)
        sensor.detect_vehicle()

def exit_car_park(car_park, sensor):
    """
    Send a specific number of vehicles trough Exit Sensor. The number is defined by the range(int)
    Print an updated capacity information after the vehicle leaves the car park.
    :param car_park: the CarPark() object to access methods
    :param sensor: the SensorExit() object to access methods
    """
    for i in range(2):
        print()
        sensor.detect_vehicle()
        message(car_park)

def main():
    welcome_message(car_park, display)
    enter_car_park(car_park, entry_sensor)
    exit_car_park(car_park, exit_sensor)

if __name__ == "__main__":
    main()