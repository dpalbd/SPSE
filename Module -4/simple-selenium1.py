#should be start with startx

#https://stackoverflow.com/questions/44598996/message-geckodriver-executable-needs-to-be-in-path-but-it-already-is
#https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
#https://stackoverflow.com/questions/40188699/webdriverexception-message-geckodriver-executable-needs-to-be-in-path/40268086
#https://stackoverflow.com/questions/47782650/selenium-common-exceptions-sessionnotcreatedexception-message-unable-to-find-a/47785513
#https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path/40208762#40208762
#https://stackoverflow.com/questions/37761668/cant-open-browser-with-selenium-after-firefox-update/37765661#37765661
#https://stackoverflow.com/questions/43272919/difference-between-webdriver-firefox-marionette-webdriver-gecko-driver/43920453
#https://stackoverflow.com/questions/44530302/how-can-geckodriver-firefox-work-without-marionette-running-python-selenium-3
#use selenium 


#pip install selenium
#
# Download geckodriver
#https://github.com/mozilla/geckodriver/releases

#cp geckodriver /usr/local/bin/ 
#ls -la /usr/local/bin/geckodriver 
#-rwxr-xr-x 1 root staff 6409830 XX XX 10:23 /usr/local/bin/geckodriver


#!/usr/bin/env python


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('http://google.com/')
#browser.quit()
