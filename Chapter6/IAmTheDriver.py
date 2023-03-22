from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from IAmTheEventListener import IAmTheEventListener

driver = webdriver.Chrome()
event_listener = IAmTheEventListener()
event_firing_driver = EventFiringWebDriver(driver, event_listener)
event_firing_driver.get("http://www.google.com")
event_firing_driver.get("http://www.facebook.com")
event_firing_driver.back()