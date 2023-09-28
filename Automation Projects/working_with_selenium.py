from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://accounts.google.com/v3/signin/identifier?hl=en-GB&ifkv=AYZoVheq_qjQbkbDt0MJb_bCAWkzjh8qpkp0CqPBXAuWTct6y1ctndbnJjQh328zy0JX3ccxMoCX0A&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S588219906%3A1695894846539180&theme=glif')
getting_form = browser.find_element(by=By.ID, value="identifierId")
getting_form.send_keys('philballer41@gmail.com')

button = browser.find_element(by=By.TAG_NAME, value="button")
button.click()


browser.implicitly_wait(8)


"""getting_password = browser.find_element(by=By.ID, value="password")
getting_password.send_keys("$Philballer_41$")
pass_button = browser.find_element(by=By.TAG_NAME, value="button")
pass_button.click()
browser.implicitly_wait(5)

browser.forward()"""

print('The program ran successfully')
