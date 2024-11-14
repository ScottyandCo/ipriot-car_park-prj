from abc import ABC, abstractmethod
#from random import random, randint, choice
from random import *


class Sensor(ABC):
    def __init__(self, sensor_id = None, is_active = True, car_park = None):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        if self.is_active:
            return f"Sensor #{self.sensor_id} is Online"
        else:
            return f"Sensor #{self.sensor_id} is Offline"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        letters = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZZ"]
        return f"1-{choice(letters)}-{format(randint(0, 999), "03d")}"

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class SensorEnter(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"A 🚗 with the license plate '{plate}' is entering the car park.")
# TODO: randomise vehicle type (choice(["🚗","🏍️")
#       manage by using a dict and adding and removing as a k/v pair {plate: emoji}

class SensorExit(Sensor):
    def _scan_plate(self):
        return choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"A 🚗 with the license plate '{plate}' is leaving the car park.")
