'''
requests module allows python to:
- GET data from APIs
- POST data to servers
- send headers, params, JSON
- handle responses
'''

import requests

# GET request
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.headers['Content-Type'])  # application/json; charset=utf-8
# print(response.text)  # response body

data = response.json()  # parse JSON response
# print(data)  # print specific fields

# GET request with parameters
params = {'q': 'requests+language:python'}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.status_code)  # 200
data = response.json()
# print(data['total_count'])  # total repositories found
print(data['items'][0]['name'])  # name of first repository
print(data['items'][0]['html_url'])  # URL of first repository
print(data['items'][0]['description'])  # Description of first repository
print(data['items'][0]['stargazers_count'])  # Stars of first repository
print(data['items'][0]['owner']['login'])  # Owner of first repository


# POST request
data = {
    "username": "testuser",
    "password": "testpass"
}

response = requests.post('https://httpbin.org/post', json=data)
print(response.status_code)  # 200