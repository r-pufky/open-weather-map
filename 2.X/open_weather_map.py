#
# Python interface for OpenWeatherMap.
#
# This library provides a skeleton API interface for openweathermap.org.
#
# Details of API can be found here: http://openweathermap.org/api
# Weather conditions enumeration: http://openweathermap.org/weather-conditions
#

import json
import urllib2


class OpenWeatherMap(object):
  """ OpenWeatherMap public (free) API interface.
  
  Attributes:
    API_BASE: String base url used for API calls.
  """
  API_BASE = 'http://api.openweathermap.org/data/2.5/'

  def __init__(self, api_key, units='imperial'):
    """ Initialize OpenWeatherMap.

    Args:
      api_key: String API key to use for openweathermap.org.
      units: String units to return results in. Default: imperial.
          [metric, imperial, kelvin].
    """
    self.api_key = api_key
    self.units = units
    if units not in ['metric', 'imperial', 'kelvin']:
      self.units = 'imperial'
    
  def _QueryApi(self, endpoint):
    """ Queries a specific API endpoint and store in local cache.

    Args:
      endpoint: String endpoint to query.
    """
    query = '%s%s&units=%s&APPID=%s' % (self.API_BASE,
                                        endpoint,
                                        self.units,
                                        self.api_key)
    query = urllib2.Request(query)
    data = urllib2.urlopen(query)
    json_data = data.read()
    return json.loads(json_data.decode('utf-8'))

  def GetCurrentWeather(self, city=5809844):
    """ Return dictionary with the current weather data for a given city.

    Args:
      cite: Integer city ID from http://bulk.openweathermap.org/sample/.

    Returns:
      Dictionary containing {'id': Integer weather type,
                             'main': String main weather description,
                             'description': String of weather details,
                             'icon': String coded icon to use,
                             'temp': Integer current temperature,
                             'temp_min': Integer minimum temperature,
                             'temp_max': Integer maximum temperature,
                             'humidity': Integer current humidity}.
    """
    json_data = self._QueryApi('weather?id=%s' % city)
    weather = json_data['weather'][0]
    weather.update(json_data['main'])
    weather.pop('pressure')
    return weather
