from pathlib import Path
from datetime import datetime
from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates = None, sensors = None, displays = None, log_file = Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Location - {self.location},\nCapacity - {self.capacity}"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        available_bays = int(self.capacity - len(self.plates))
        if available_bays < 0:
            return 0
        else:
            return available_bays

    def update_displays(self):
        message = {"available_bays": self.available_bays, "temperature": 42}
        for display in self.displays:
            display.update(message)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as log:
            log.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\t{plate} {action}\n")
