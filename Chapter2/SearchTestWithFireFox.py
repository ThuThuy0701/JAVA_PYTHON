import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import unittest
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
class SearchTestWithEdge:
    def __init__(self,driver):
        self.driver = driver
    def navigate(self):
        self.driver.get("http://demo-store.seleniumacademy.com/")
        time.sleep(3)
        return self
    def find_element_search_box(self):
        searchbox = self.driver.find_element(By.NAME,"q")
        return searchbox
    def find_element_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "search-button")
        return button
    def teardown(self):
        self.driver.quit()
class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('firefox')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTestWithEdge(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box()
        searchbox.send_keys("Phones")
        button = elementobject.find_element_button()
        button.click()
        title = driver.title
        self.assertEqual(title, "Search results for: 'Phones'", "Tiêu đề không chính xác")
        elementobject.teardown()





