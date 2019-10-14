
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Keys provide keys present in keyboard like functionkeys


driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

target = "lk"
string = "mental"

elem = driver.find_element_by_className("_3u328 copyable-text selectable-text")


contactname = "_3NWy8"

driver.close()

