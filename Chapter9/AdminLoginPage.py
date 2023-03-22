from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AllPostsPage import AllPostsPage


class AdminLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://demo-blog.seleniumacademy.com/wp/wp-admin")
        self.email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user_login")))
        self.password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user_pass")))
        self.submit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "wp-submit")))

    def login(self, username, pwd):
        self.email.clear()
        self.email.send_keys(username)
        self.password.clear()
        self.password.send_keys(pwd)
        self.submit.click()
        return AllPostsPage(self.driver)
