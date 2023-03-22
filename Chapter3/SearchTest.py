import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import unittest
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
        self.driver.get("http://demo-store.seleniumacademy.com/")
        time.sleep(3)
        return self
    def find_element_search_box(self):
        searchbox = self.driver.find_element(By.NAME,"q")
        return searchbox

    def find_element_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "search-button")
        return button
    def find_elements(self):
        elements = self.driver.find_elements(By.XPATH, "//h3[@class='product-name']/a")
        return elements
class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        searchbox=elementobject.find_element_search_box()
        searchbox.send_keys("Phones")
        button = elementobject.find_element_button()
        button.click()
        title = driver.title
        self.assertEqual(title, "Search results for: 'Phones'", "Tiêu đề không chính xác")
        searchItems = elementobject.find_elements()
        print(len(searchItems))
        languages = ("English","German","French")
        for language in languages:
            print(language.upper())
        product=Product()
        product1 = Product("MADISON OVEREAR HEADPHONES", 125.00)
        print("Name:",product1.name,"Price:",product1.price)
        product2 = Product("MADISON EARBUDS", 35.00)
        print("Name:", product2.name,"Price:",product2.price)
        product3 = Product("MP3 PLAYER WITH AUDIO", 185.00)
        print("Name:", product3.name,"Price:",product3.price)







def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()






