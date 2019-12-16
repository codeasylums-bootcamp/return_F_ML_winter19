from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


print("Post Status on facebook: ")


usr=input('Enter Email Id:')  
pwd=getpass('Enter Password:')  

driver.get('https://www.facebook.com/')
print ("Opened facebook...")
a = driver.find_element_by_id('email')
a.send_keys(usr)
print ("Email Id entered...")
b = driver.find_element_by_id('pass')
b.send_keys(pwd)
print ("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
sleep(1)

driver.get('https://www.facebook.com/events/birthdays/') 
  
wish = 'Happy Birthday !'
  
element = driver.find_elements_by_xpath("//*[@id='u_0_11']") 
  
cnt = 0
  
for el in element:
    cnt += 1
    element_id = str(el.get_attribute('id')) 
    XPATH = '//*[@id ="' + element_id + '"]'
    post_field = driver.find_element_by_xpath(XPATH) 
    post_field.send_keys(wish) 
    post_field.send_keys(Keys.RETURN) 
    print("Birthday Wish posted for friend" + str(cnt)) 
  






		

