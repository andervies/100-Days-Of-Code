import requests
from datetime import datetime

USER_NAME = "anderslair"
TOKEN = "sksksksksksk"
GRAPH_ID = "lair01"

today = datetime(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day)

graph_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
pixela_endpoint = "https://pixe.la/v1/users"
commit_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

headers = {"X-USER-TOKEN": TOKEN}
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "codeograph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

commit_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Rate your coding practice for today on a scale of 1-10... add 15 for extra spice: "),
    "optionalData": '{"note to self": "I am so proud of myself. Im my own superhero. whuuuuuut!!!"}',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=commit_endpoint, json=commit_config, headers=headers)
print(response.text)

# response = requests.put(url=update_pixel_endpoint, json=commit_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, json=commit_config, headers=headers)
# print(response.text)





