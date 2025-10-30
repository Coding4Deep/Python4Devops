from unittest.mock import Mock
from weather import get_weather

# Create a fake object
api = Mock()

# Define what happens when we call its method
api.get_weather.return_value = {"temperature": 25}

# Use it
result = api.get_weather("London")
print(result)  # {'temperature': 25}

# Verify the call
api.get_weather.assert_called_once_with("London")
