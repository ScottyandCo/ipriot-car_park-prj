import unittest
from sensor import SensorEnter, SensorExit
from car_park import CarPark

class SensorTest(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = SensorEnter(999, True, CarPark())
        self.exit_sensor = SensorExit(945, True, CarPark())

    def test_entry_sensor(self):
        self.assertIsInstance(self.entry_sensor, SensorEnter)
        self.assertEqual(self.entry_sensor.sensor_id, 999)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.entry_sensor.detect_vehicle()


    def test_exit_sensor(self):
        self.assertIsInstance(self.exit_sensor, SensorExit)
        self.assertEqual(self.exit_sensor.sensor_id, 945)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)
        self.assertEqual(self.exit_sensor.update_car_park("TEST-952"), None)


