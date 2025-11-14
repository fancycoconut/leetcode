class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = []

        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.0
        output.append(kelvin)
        output.append(fahrenheit)
        return output
