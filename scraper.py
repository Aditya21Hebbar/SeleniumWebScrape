import requests

grab_url='https://www.swiggy.com/restaurants'

response = requests.get(grab_url)

print('status code',response.status_code)
print('Output', response.text[:1000])