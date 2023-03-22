import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver import ActionChains, Keys
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
class WebDriverMangerFactory:
    def getWebDriverForBrowser(browsername):
        if browsername=='chrome':
            return webdriver.Chrome()
        if browsername=='firefox':
            return webdriver.Firefox()
        if browsername=='edge':
            return webdriver.Edge()
        else:
            return "No match"
class SearchTest:
    def __init__(self,driver):
        self.driver = driver
    def navigate(self):
        self.driver.get("http://guidebook.seleniumacademy.com/Frames.html")
        time.sleep(3)
        return self
    def frame1(self):
        frame1 =self.driver.switch_to.frame("frameOne")
        return frame1
    def framedefault(self):
        return self.driver.switch_to.default_content()
    def frame2(self):
        frame2 =self.driver.switch_to.frame("frameTwo")
        return frame2
    def find_element1(self):
        element = self.driver.find_element(By.NAME,"1")
        return element

    def find_element2(self):
        element = self.driver.find_element(By.NAME, "2")
        return element


class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        elementobject.frame1()
        firstField = elementobject.find_element1()
        firstField.send_keys("I'm Frame One")
        #Action = ActionChains(driver)
        #Action.key_up(Keys.TAB).perform()
        elementobject.framedefault()
        elementobject.frame2()
        secondField = elementobject.find_element2()
        secondField.send_keys("I'm Frame Two")
        time.sleep(2)







def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()






