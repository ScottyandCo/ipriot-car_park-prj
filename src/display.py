class Display:
    def __init__(self, display_id = None, message = "", is_on = False, car_park = None):
        self.display_id = display_id or []
        self.message = message
        self.is_on = is_on or []
        self.car_park = car_park or []

    def __str__(self):
        return f"Display #{self.display_id}: {self.message}"

    def update(self, message):
        for key, value in message.items():
            print(f"{key}: {value}")
