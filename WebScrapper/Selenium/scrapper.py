import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

#driver.quit() for closing the entire browser
#for getting the title of the page
print(driver.title)

'''driver.close()#for tab closing
'''
search=driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
#print(driver.page_source)
    
time.sleep(5)
driver.quit()