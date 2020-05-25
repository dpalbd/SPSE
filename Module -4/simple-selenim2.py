#https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python
#https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver
#https://stackoverflow.com/questions/31530335/selenium-webdriver-vs-mechanize

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
driver.get("http://google.com/")
print ("Headless Firefox Initialized")

