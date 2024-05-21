from typing import Tuple

import requests
import config

# params - https://www.google.com/?parameter1=10&fb_ads=telegram
# https://www.google.com/?parameter1=10&fb_ads=telegram

# headers requests.post(url='https://www.google.com', headers={"Authorization": "Bearer token"})

# cookies requests.post(url='https://www.google.com', cookies={'cook1': 1})

# auth requests.post(url='https://www.google.com', auth=('username', 'password'))

# timeout seconds requests.post(url='https://www.google.com', timeout=10)

# redirections requests.post(url='https://www.google.com', allow_redirects=True|False)

# proxies
# requests.post(url='https://www.google.com', proxies={
#   'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# })

# response.text
# response.content
# response.json()
# response.headers
# response.url
# response.history
# response.elapsed
# response.status_code
# response.raise_for_status()


header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# response = requests.post(url=config.api.url + "auth", headers=header, json={
#     "username": "aqa_course_20",
#     "password": "password123@"
# })


# assert response.status_code == 200

# if response.status_code != 200:
#     raise Exception


# response = requests.get(url=config.api.url + "booking")
#
# print(response.json())


# '{"id":100,"category":{"id":1,"name":"Linda"},"name":"doggie","photoUrls":["stringphoto"],"tags":[{"id":1,"name":"LindasTag"}],"status":"available"}'

post_json = {
    'name': 'aqa_c',
    'status': 'busy'
}
#
# update_pet_res = requests.post(url=config.api.url + "pet/100", data=post_json,
#                                headers={"Content-Type": "application/x-www-form-urlencoded"})
#
# print(update_pet_res)
#
get_pets = requests.get(url=config.api.url + "pet/100")


assert get_pets.json()['name'] == post_json['name']


