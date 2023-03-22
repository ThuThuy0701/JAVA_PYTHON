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
        searchbox = self.driver.find_element(By.NAME,"q")
        return searchbox
    def elementgetTagName(self):
        tagname= self.driver.find_element(By.CLASS_NAME,"global-site-notice")
        return tagname
    def find_element_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "search-button")
        return button
class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox=elementobject.find_element_search_box()
        print("Name of the box is:",searchbox.get_attribute("name"))
        print("Id of the box is:", searchbox.get_attribute("id"))
        print("Class of the box is:", searchbox.get_attribute("class"))
        print("Palceholder of the box is:", searchbox.get_attribute("placeholder"))
    def test_2(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box()
        searchbox.send_keys("Phones")
        searchbox.submit()
        title = driver.title
        self.assertEqual(title,"Search results for: 'Phones'","Tiêu đề không chính xác")
    def test_3(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        #searchbox = elementobject.find_element_search_box()
        action = ActionChains(driver)
        act= elementobject.find_element_search_box()
        action.click(act).key_down(Keys.SHIFT).send_keys("phones").perform()
        act.submit()
        title = driver.title
        self.assertEqual(title, "Search results for: 'PHONES'", "Tiêu đề không chính xác")
    def test_4(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        # searchbox = elementobject.find_element_search_box()
        action = ActionChains(driver)
        act = elementobject.find_element_search_box()
        action.click(act).key_down(Keys.SHIFT).send_keys("phones").perform()
        act.clear()
        time.sleep(2)
    def test_5(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        # searchbox = elementobject.find_element_search_box()
        action = ActionChains(driver)
        act = elementobject.find_element_search_box()
        action.click(act).key_down(Keys.SHIFT).send_keys("phones").perform()
        act.submit()
        time.sleep(2)
    def test_6(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box()
        print("Font of the box is:",searchbox.value_of_css_property("font-family"))
    def test_7(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box()
        print("location of the box is:",searchbox.location)
        print("Size of the box is:", searchbox.size)
    def test_8(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        tagname = elementobject.elementgetTagName()
        print("Complete text is:",tagname.text)
    def test_9(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        button=elementobject.find_element_button()
        print("Html tag of the button is:",button.tag_name)
    def test_10(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = ElementTest(driver)
        elementobject.navigate()
        searchbox = elementobject.find_element_search_box()
        print("Search buttpn is displayed:",searchbox.is_displayed())
        print("Search buttpn is enabled:", searchbox.is_enabled())
        print("Search buttpn is selected:", searchbox.is_selected())
def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()






