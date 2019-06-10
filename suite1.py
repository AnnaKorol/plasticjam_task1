from selenium import webdriver
import os


currentDirPath = os.path.dirname(os.path.realpath(__file__))

currentDriver = webdriver.Chrome()

currentDriver.get("http://the-internet.herokuapp.com/")

formAuthenticationLinkLocator = currentDriver.find_elements_by_xpath('//a[text()="Form Authentication"]')[0]
formAuthenticationLinkLocator.click()

formAuthenticationLocator = currentDriver.find_elements_by_xpath('//*[@id="content"]')[0]

emailInputLocator = currentDriver.find_elements_by_xpath('//input[@type="text"]')[0]
emailInputLocator.send_keys('tomsmith')

passwordInputLocator = currentDriver.find_elements_by_xpath('//input[@type="password"]')[0]
passwordInputLocator.send_keys('SuperSecretPassword!')

submitBtnLocator = currentDriver.find_elements_by_xpath('//button[@type="submit"]')[0]
submitBtnLocator.submit()

currentDriver.get_screenshot_as_file(currentDirPath + r'/test_output/result.png')

currentDriver.close()
