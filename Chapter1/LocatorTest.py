import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import unittest
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
class ElementTest:
    def __init__(self,driver):
        self.driver = driver
    def navigate(self):
        self.driver.get("http://demo-store.seleniumacademy.com/")
        time.sleep(3)
        return self
    def find_element_search_box(self):
        searchbox = self.driver.find_element(By.CSS_SELECTOR,"#search")
        return searchbox
    def elementgetTagName(self):
        tagname= self.driver.find_element(By.CLASS_NAME,"global-site-notice")
        return tagname
    def find_element_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "search-button")
        return button
    def find_element_link(self):
        link = self.driver.find_element(By.LINK_TEXT,"MY ACCOUNT")
        return link
    def find_element_partiallink(self):
        partiallink = self.driver.find_element(By.PARTIAL_LINK_TEXT,"PRIVACY")
        return partiallink
    def find_elements(self):
        find_elements=self.driver.find_elements(By.TAG_NAME,"a");
        return find_elements
class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox=elementobject.find_element_search_box()
        searchbox.send_keys("Bags")
        searchbox.submit()
        title = driver.title
        self.assertEqual(title,"Search results for: 'Bags'","tiêu đề không chính xác")
    def test_2(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox=elementobject.find_element_search_box()
        searchbox.send_keys("Electronics")
        button = elementobject.find_element_button()
        button.click()
        title= driver.title
        self.assertEqual(title, "Search results for: 'Electronics'", "tiêu đề không chính xác")
    def test_3(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        myAccountLink=elementobject.find_element_link()
        myAccountLink.click()
        title = driver.title
        self.assertEqual(title, "Customer Login", "tiêu đề không chính xác")
    def test_4(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        orderAndreturns = elementobject.find_element_partiallink()
        orderAndreturns.click()
        title = driver.title
        self.assertEqual(title, "Privacy Policy", "tiêu đề không chính xác")
    def test_5(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        links = elementobject.find_elements()
        print("Found links:", len(links))
        for link in links:
            print(link.text)
    def test_6(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        Xpath= elementobject.find_element_search_box()
        Xpath.send_keys("Bags")
        Xpath.submit()
        title  = driver.title
        self.assertEqual(title, "Search results for: 'Bags'", "tiêu đề không chính xác")
    def test_7(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        Xpath = elementobject.find_element_search_box()
        Xpath.send_keys("Bags")
        Xpath.submit()
        title = driver.title
        self.assertEqual(title, "Search results for: 'Bags'", "tiêu đề không chính xác")




"""def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()"""













