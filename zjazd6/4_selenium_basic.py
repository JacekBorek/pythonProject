from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime


driver = webdriver.Chrome()

driver.get('https://www.booking.com/dealspage.html?aid=2094309;campaign_id=Late%20Escape&label=Late%20Escape23')
print(f'Nazwa strony {driver.title}')
sleep(2)
button1_accept = driver.find_element('id','onetrust-accept-btn-handler')
button1_accept.click()
search_field = driver.find_element('id',"ss")
search_field.send_keys('Wyspy kanaryjskie')
search_field.send_keys(Keys.ENTER)

teraz = datetime.datetime.now()
filename = teraz.strftime('screenshot-%H_%M_%S.png')
driver.get_screenshot_as_file(filename)

# button2_accept = driver.find_element('name','ghost click')
# button2_accept.submit()
sleep(3)

driver.quit()
