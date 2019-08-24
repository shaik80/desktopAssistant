from weather import Weather
weather = Weather()
location = weather.lookup_by_location('bangalore')
condition = location.condition
print('The Current weather in %s is %s The tempeture is %.1f degree' % (condition.text(), (int(condition.temp())-32)/1.8))

