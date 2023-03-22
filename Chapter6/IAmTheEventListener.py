from selenium.webdriver.support.events import AbstractEventListener

class IAmTheEventListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before Navigate To: " + url + " and Current url is: " + driver.current_url)

    def after_navigate_to(self, url, driver):
        print("After Navigate To: " + url + " and Current url is: " + driver.current_url)

    def before_navigate_back(self, driver):
        print("Before Navigate Back. Right now I'm at " + driver.current_url)

    def after_navigate_back(self, driver):
        print("After Navigate Back. Right now I'm at " + driver.current_url)
