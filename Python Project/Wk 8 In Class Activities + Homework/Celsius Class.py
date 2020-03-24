class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        self._temperature = self._temperature * (9 / 5) + 32
        return self._temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        if temperature < -273:
            self._temperature = -273
        else:
            self._temperature = temperature

    temperature = property(get_temperature, set_temperature)