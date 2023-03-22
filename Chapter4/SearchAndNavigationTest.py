import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver import ActionChains, Keys
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
        self.driver.get("http://demo-store.seleniumacademy.com/")
        time.sleep(3)
        return self
    def navigate_back(self):
        self.driver.back()
        return self
    def navigate_forward(self):
        self.driver.forward()
        return self
    def navigate_refresh(self):
        self.driver.refresh()
        return self
    def find_element_search_box(self):
        searchbox = self.driver.find_element(By.NAME,"q")
        return searchbox

    def find_element_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "search-button")
        return button


class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box().send_keys("Phones")
        button = elementobject.find_element_button().click()
        title = driver.title
        self.assertEqual(title,"Search results for: 'Phones'","Tiêu đề không chính xác")
        elementobject.navigate_back()
        elementobject.navigate_forward()
        elementobject.navigate_refresh()
        time.sleep(2)







def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()






