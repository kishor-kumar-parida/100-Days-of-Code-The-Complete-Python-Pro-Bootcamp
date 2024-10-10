import requests
from datetime import datetime

profile_url = "https://pixe.la/@kishor"
graph_url = "https://pixe.la/v1/users/kishor/graphs/kishor1.html"

headers = {
    "X-USER-TOKEN": "kishorparida",
}


#######################################################
# Register as User

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": "kishorparida",
#     "username": "kishor",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#######################################################


#######################################################
# Create Graph

graph_endpoint = "https://pixe.la/v1/users/kishor/graphs"

# graph_params = {
#     "id": "kishor1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

#######################################################


#######################################################
# Posting Graph

# pixel_endpoint = "https://pixe.la/v1/users/kishor/graphs/kishor1"

# pixel_params = {
#     "date": datetime.now().strftime("%Y%m%d"),
#     "quantity": input("How many Km did you cycle today?"),
# }

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

#######################################################


#######################################################
# Update graph

# update_endpoint = f"https://pixe.la/v1/users/kishor/graphs/kishor1/{datetime.now().strftime('%Y%m%d')}"

# new_pixel_data = {"quantity": "4.5"}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# print(response.text)

#######################################################


#######################################################
# Delete graph

delete_endpoint = f"https://pixe.la/v1/users/kishor/graphs/kishor1/{datetime.now().strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)

print(response.text)

#######################################################
