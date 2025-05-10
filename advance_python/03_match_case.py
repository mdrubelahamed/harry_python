def http_status(status):
    match status:
        case 100:
            return "Continue."
        case 200:
            return "Ok."
        case 301:
            return "Moved Permanently."
        case 400:
            return "Bad Request."
        case 401:
            return "Unauthorized."
        case 403:
            return "Forbidden."
        case 404:
            return "Not Found."
        case 500:
            return "Internal Server Error."
        case _:
            return "Unknown status."


# print(http_status(301))  # Moved Permanently.
# print(http_status(404))  # Not Found.
# print(http_status(5309509349))  # Unknown status.

# Create a Python program that takes a weather condition as input and provides appropriate recommendations based on the condition using the match case statement.
def weather_condition(temp):
    match temp:
        case temp if temp < 20:
            return "Weather is cold."
        case temp if 20 <= temp < 30:
            return "Weather is good."
        case temp if temp >= 30:
            return "Weather is hot."
        case _:
            return "Temperature is out of range. Please enter a temperature between -273.15 and 100 degrees Celsius."


# print(weather_condition(-11))
# print(weather_condition(20))
# print(weather_condition(30))
# print(weather_condition(40))
