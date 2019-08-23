import requests

url = 'http://172.19.0.7:8067/metrics'

response = requests.get(url)

print response.content
