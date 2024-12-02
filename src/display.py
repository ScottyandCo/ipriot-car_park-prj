class Display:
    def __init__(self, display_id, car_park, message="", is_on=False):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display #{self.display_id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            # test if the data item is able to be an int and display the bays available message using that int,
            # otherwise display the string value as it has been entered.
            try:
                value = int(value)
                self.message = f"There are currently {value} bays available"
            except:
                self.message = value
