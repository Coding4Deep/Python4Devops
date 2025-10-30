# import requests

# def get_weather(city):
#     """Fetch weather info from a live API"""
#     response = requests.get(f"https://api.weather.com/{city}")
#     data = response.json()
#     return data["temperature"]


from unittest.mock import Mock

api = Mock()

api.get_user.return_value = {"name": "Alice"}
result = api.get_user(1)

assert result == {"name": "Alice"}
api.get_user.assert_called_once_with(1)
