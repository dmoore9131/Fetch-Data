import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'Request failed: {e}')
    exit(1)

data = response.json()

for post in data:
    print(post)
