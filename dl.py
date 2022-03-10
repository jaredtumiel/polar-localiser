from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

LIB_SIZE = 821 #num objects in bookshelf (last "enhanced-table-checkbox-XXX")

driver = webdriver.Firefox()
driver.get("https://app.getpolarized.io")
actionChains = ActionChains(driver)

base_el = "enhanced-table-checkbox-"
for i in range(LIB_SIZE + 1):
    elem = driver.find_element_by_id("{}{}".format(base_el,i))
    actionChains.context_click(elem).perform()
    time.sleep(0.1)
    dl = driver.find_element_by_css_selector("li.MuiButtonBase-root:nth-child(9) > div:nth-child(2) > span:nth-child(1)")
    dl.click()
    time.sleep(0.1)


