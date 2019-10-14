
import requests


#url =  "https://www.nobroker.in/property/buy/2-BHK-apartment-for-sale-in-Srinivas-Nagar-hyderabad/ff8081816c42591a016c42929d575010/detail"
url = "https://www.nobroker.in/property/commercial/buy/Office-in-Begumpet-hyderabad/ff8081816c3625f1016c3788bd57373b/detail"
params = None
data = None

response = requests.get(url = url, data = data, params = params, proxies = None)

print(response.text)
#print(response.text)




