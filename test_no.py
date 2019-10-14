
import requests

session = requests.session()

url =  "https://www.nobroker.in/property/buy/2-BHK-apartment-for-sale-in-Srinivas-Nagar-hyderabad/ff8081816c42591a016c42929d575010/detail"
params = None
data = None
headers = {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "content-type": "application/x-www-form-urlencoded; charset=utf-8",
      "Host": "www.nobroker.in",
      "Pragma": "no-cache"
    }
session.headers = headers
response = session.get(url = url, data = data, params = params, proxies = None)

print(response)
#print(response.text)




