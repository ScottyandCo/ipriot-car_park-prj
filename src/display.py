class Display:
    def __init__(self, display_id = None, message = "", is_on = False, car_park = None):
        self.display_id = display_id or []
        self.message = message
        self.is_on = is_on
        self.car_park = car_park or []

    def __str__(self):
        return f"Display #{self.display_id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            self.message = value
            # print(f"{key}: {value}")
