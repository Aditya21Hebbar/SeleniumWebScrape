import requests

grab_url='https://food.grab.com/sg/en/restaurants'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(grab_url,headers=headers)

print('status code',response.status_code)
print('Output',response.text[:100])