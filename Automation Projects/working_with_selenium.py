from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&passive=1209600&ifkv=AXo7B7UpD0FT30PySPigoDANa3ydZG9IaLCdzzqU3X4WZoa5c3erjM99iBml2JOJ8jSrUf_Mla4z&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
getting_form = browser.find_element(by=By.ID, value="identifierId")
getting_form.send_keys('philballer41@gmail.com')

button = browser.find_element(by=By.TAG_NAME, value="button")
button.click()

browser.forward()

"""button = browser.find_element(by=By.CSS_SELECTOR, value="input.password")
button.click()"""

print('The program ran successfully')
