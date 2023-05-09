import requests

endpoint = "http://localhost:8000/api/products/43535345345/"

get_response = requests.get(endpoint)
print(get_response.json())