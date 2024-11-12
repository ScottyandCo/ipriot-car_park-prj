class Sensor:
    def __init__(self, sensor_id = None, is_active = True, car_park = None):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        if self.is_active:
            return f"Sensor #{self.sensor_id} is Online"
        else:
            return f"Sensor #{self.sensor_id} is Offline"

class SensorEnter(Sensor):
    ...

class SensorExit(Sensor):
    ...
