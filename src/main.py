import random
from datetime import datetime
from car_park import CarPark
from display import Display
from sensor import SensorEnter, SensorExit

# Create objects required for the car park
car_park = CarPark(100, "Moondalup", log_file="moondalup.txt")
entry_sensor = SensorEnter(1, car_park, True)
exit_sensor = SensorExit(2, car_park, True)
display = Display(1, car_park, "Welcome to Moondalup", True)


def register_components(*args):
    """
    Registers components to the car_park
    Will call car_park.register for any number of components entered as parameters when the register_components function
    is called.
    :param args: any number of individual components required for the car_park
    """
    for i in args:
        car_park.register(i)


# write config of CarPark to JSON file
car_park.write_config()


def welcome_message():
    """
    Print a welcome message with information about the car park and current conditions.
    """
    temperature = random.randint(21, 38)
    weather = random.choice(["sunny ☀️", "overcast 🌤️", "raining 🌧️"])
    time = datetime.now().strftime("%H:%M")
    print("\n" + "|" + "*" * 60)
    print(f"| {display.message}.\n| Our maximum capacity is {car_park.capacity} vehicles.\n| It is currently {time}, "
          f"{temperature}c and {weather}.")
    print("*" * 61)

# def message(car_park):
#     print(f"The car park currently has {car_park.available_bays} bays available")


def enter_car_park():
    """
    Send a specific number of vehicles trough Entry Sensor. The number is defined by the range(int)
    Print capacity information before the vehicle enters the car park.
    """
    for i in range(10):
        print()
        entry_sensor.detect_vehicle()
        print(display.message)


def exit_car_park():
    """
    Send a specific number of vehicles trough Exit Sensor. The number is defined by the range(int)
    Print updated capacity information after the vehicle leaves the car park.
    """
    for i in range(2):
        print()
        exit_sensor.detect_vehicle()
        print(display.message)


def main():
    register_components(entry_sensor, exit_sensor, display)
    welcome_message()
    enter_car_park()
    exit_car_park()


if __name__ == "__main__":
    main()
