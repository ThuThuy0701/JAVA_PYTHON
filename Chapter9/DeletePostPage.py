import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DeletePostPage:
    def __init__(self, driver):
        self.driver = driver
        print(driver.current_url)

    move_to_trash_locator = (By.LINK_TEXT, "Move to Trash")

    def delete(self):
        wait = WebDriverWait(self.driver, 10)
        move_to_trash = wait.until(EC.visibility_of_element_located(self.move_to_trash_locator))
        move_to_trash.click()
