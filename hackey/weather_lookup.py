from weather import Weather

weather = Weather()
    
def convert_farenheit_to_celsius(f):
    c = (f-32)/1.8
    return str(round(c,1))
    
def get_weather_for_city(city_name):
    location = weather.lookup_by_location(city_name)
    condition = location.condition()
    temp = convert_farenheit_to_celsius(float(condition.temp()))
    text_response = "Weather in "+city_name+" today: " + condition.text() + " with a temperature of " + temp + "c"
    return text_response
