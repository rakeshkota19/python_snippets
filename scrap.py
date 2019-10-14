from bs4 import BeautifulSoup
import requests
import os
import sys



response = requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")

bs = BeautifulSoup(response.text, 'lxml')

#print(bs.prettify())

dd = "contactOwnerBtnff8081816b324adc016b35a7933f2dfb"
de = "contactOwnerBtnff80818168e6f4200168e73a1b8926c2"

print(dd[15:-1])


dd = "rakesh in ko,fe"
print(dd.split()[1].split(",")[0])


if 1==1:
	print('fd')
	