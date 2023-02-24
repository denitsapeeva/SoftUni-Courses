def forecast(*args):
    my_weather = {}
    sunny_weather = {}
    cloudy_weather = {}
    rainy_weather = {}
    result = ''
    for a in args:
        location = a[0]
        weather = a[1]
        if weather == "Sunny":
            sunny_weather[location] = weather
        elif weather == "Rainy":
            rainy_weather[location] = weather
        elif weather == "Cloudy":
            cloudy_weather[location] = weather
    sunny_weather = sorted(sunny_weather.items(), key=lambda x: x[0])
    for a in sunny_weather:
        my_weather[a[0]] = a[1]
    cloudy_weather = sorted(cloudy_weather.items(), key=lambda x: x[0])
    for a in cloudy_weather:
        my_weather[a[0]] = a[1]
    rainy_weather = sorted(rainy_weather.items(), key=lambda x: x[0])
    for a in rainy_weather:
        my_weather[a[0]] = a[1]
    for key, value in my_weather.items():
        result += f'{key} - {value}\n'

    return result

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
