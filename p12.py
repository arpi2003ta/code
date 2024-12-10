class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        # Ensure that the temperature is not below absolute zero
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

# Example usage
temp = Temperature()

try:
    temp.celsius = -300  # This will raise an exception
except ValueError as e:
    print(e)

temp.celsius = 25  # Valid temperature
print(f"Temperature set to {temp.celsius}°C")
