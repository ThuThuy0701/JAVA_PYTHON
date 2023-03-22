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
class SearchTest:
    def __init__(self,driver):
        self.driver = driver
    def navigate(self):
        self.driver.get("http://guidebook.seleniumacademy.com/Selectable.html")
        time.sleep(3)
        return self
    def navigate1(self):
        self.driver.get("http://guidebook.seleniumacademy.com/DragMe.html")
        time.sleep(3)
        return self
    def navigate2(self):
        self.driver.get("http://guidebook.seleniumacademy.com/DragAndDrop.html")
        time.sleep(3)
        return self
    def find_element_one(self):
        one = self.driver.find_element(By.NAME,"one")
        return one

    def find_element_three(self):
        three = self.driver.find_element(By.NAME, "three")
        return three
    def find_element_five(self):
        five = self.driver.find_element(By.NAME, "five")
        return five

    def find_element_seven(self):
        seven = self.driver.find_element(By.NAME, "seven")
        return seven

    def find_element_eleven(self):
        eleven = self.driver.find_element(By.NAME, "eleven")
        return eleven

    def find_element_two(self):
        two = self.driver.find_element(By.NAME, "two")
        return two
    def find_element_drap(self):
        drap = self.driver.find_element(By.ID, "draggable")
        return drap
    def find_element_drap1(self):
        drap1= self.driver.find_element(By.ID, "draggable")
        return drap1
    def find_element_drop(self):
        drop = self.driver.find_element(By.ID, "droppable")
        return drop

class test_Script(unittest.TestCase):
    def test_1(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver =='No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        one = elementobject.find_element_one()
        three = elementobject.find_element_three()
        five = elementobject.find_element_five()
        action = Action.key_down(Keys.CONTROL).click(one).click(three).click(five).key_up(Keys.CONTROL).perform()
        time.sleep(2)
    def test_2(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        seven = elementobject.find_element_seven()
        print("X coordinate: ",seven.location_once_scrolled_into_view['x'],"Y coordinate: ",seven.location_once_scrolled_into_view['y'])
        action = Action.move_by_offset(seven.location_once_scrolled_into_view['x']+1,seven.location_once_scrolled_into_view['y']+1).click().perform()
        time.sleep(2)
    def test_3(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        one = elementobject.find_element_one()
        eleven = elementobject.find_element_eleven()
        five = elementobject.find_element_five()
        border =1
        tileWidth = 100
        tileHeight = 80
        action1 = Action.move_by_offset(one.location_once_scrolled_into_view['x'] + border, one.location_once_scrolled_into_view['y'] + border).click().perform()
        action2 = Action.move_by_offset(2 * tileWidth + 4 *border,2*tileHeight+4*border).click().perform()
        action3 = Action.move_by_offset(-2 * tileWidth - 4 * border, -tileHeight - 2 * border).click().perform()
        time.sleep(2)
    def test_4(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        one = elementobject.find_element_one()
        eleven = elementobject.find_element_eleven()
        five = elementobject.find_element_five()
        action = Action.click(one).click(eleven).click(five).perform()
        time.sleep(2)
    def test_5(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        three = elementobject.find_element_three()
        action = Action.move_by_offset(200,20).click_and_hold().move_by_offset(120,0).perform()
        time.sleep(2)
    def test_6(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        three = elementobject.find_element_three()
        action = Action.click_and_hold(three).move_by_offset(120,0).release().perform()
        time.sleep(2)
    def test_7(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        three = elementobject.find_element_three()
        two = elementobject.find_element_two()
        action = Action.click_and_hold(three).release(two).perform()
        time.sleep(2)
    def test_8(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate()
        Action = ActionChains(driver)
        three = elementobject.find_element_three()
        action = Action.move_to_element(three).click_and_hold().move_by_offset(120,0).perform()
        time.sleep(2)
    def test_9(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate1()
        drap = elementobject.find_element_drap()
        Action = ActionChains(driver)
        action  =Action.drag_and_drop_by_offset(drap,300,200).perform()
        time.sleep(2)
    def test_10(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        elementobject = SearchTest(driver)
        elementobject.navigate2()
        drap = elementobject.find_element_drap1()
        drop  = elementobject.find_element_drop()
        Action = ActionChains(driver)
        action = Action.drag_and_drop(drap,drop).perform()
        time.sleep(2)
    def test_11(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        #elementobject = SearchTest(driver)
        driver.get("http://guidebook.seleniumacademy.com/DoubleClick.html")
        db = driver.find_element(By.NAME,"dblClick")
        Action = ActionChains(driver)
        action = Action.double_click(db).perform()
        time.sleep(2)
    def test_12(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        #elementobject = SearchTest(driver)
        driver.get("http://guidebook.seleniumacademy.com/DoubleClick.html")
        db = driver.find_element(By.NAME,"dblClick")
        Action = ActionChains(driver)
        action = Action.move_to_element(db).double_click(db).perform()
        time.sleep(2)
    def test_13(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        # elementobject = SearchTest(driver)
        driver.get("http://guidebook.seleniumacademy.com/ContextClick.html")
        content = driver.find_element(By.ID,"div-context")
        Action = ActionChains(driver)
        action  =Action.context_click(content).click(driver.find_element(By.NAME,"Item 4")).perform()
        time.sleep(2)
    def test_14(self):
        driver = WebDriverMangerFactory.getWebDriverForBrowser('chrome')
        if driver == 'No match':
            raise Exception("No matching browsers found")
        # elementobject = SearchTest(driver)
        driver.get("http://guidebook.seleniumacademy.com/ContextClick.html")
        content = driver.find_element(By.ID, "div-context")
        Action = ActionChains(driver)
        action = Action.move_to_element(content).context_click().click(driver.find_element(By.NAME,"Item 4")).perform()
        time.sleep(2)
def main():
    my_script = test_Script()
    #my_script.test_1()
    #my_script.test_2()
    #my_script.test_3()
    my_script.test_4()
if __name__ == "__main__":
    main()






