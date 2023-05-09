import requests


headers = {'Authorization': 'Bearer 570aee85e2967fa10b4d182973ce793c73e3110b'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Testing the create DONE",
    "price": 50.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())