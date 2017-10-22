# open-weather-map
Python OpenWeatherMap API Interface.

This is a skeleton library that provides Python classes for use with the
[Open Weather Map API](http://openweathermap.org/api). This is not a complete
implementation, and only features which are used have been implemented.

Enumerated weather conditions can be found here: http://openweathermap.org/weather-conditions

# Python 2.X and 3.X Support
Compatible libraries for both 2.X and 3.X python are in respective directories
Import/use the right directory for the respective version of Python you are
using.


# Usage

```python
import open_weather_map
owm = open_weather_map.OpenWeatherMap('API KEY')
owm.GetCurrentWeather()
```
