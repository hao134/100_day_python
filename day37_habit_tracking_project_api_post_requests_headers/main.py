import requests
from datetime import datetime, timedelta

USERNAME = "shihhao"
TOKEN = "qbiqfquhroqroiwjr3434"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "qbiqfquhroqroiwjr3434",
    "username": "shihhao",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
    "date": "20220321",
    "quantity":12,
}

headers = {
    "X-USER-TOKEN":TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime.today() - timedelta(days = 1)
print(yesterday)


pixel_data = {
    "date":yesterday.strftime("%Y%m%d"),
    "quantity":"17.0",
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)