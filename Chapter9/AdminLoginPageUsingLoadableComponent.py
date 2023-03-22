import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminLoginPageUsingLoadableComponent(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://demo-blog.seleniumacademy.com/wp/wp-admin"
        self.email = (By.ID, "user_login")
        self.password = (By.ID, "user_pass")
        self.submit = (By.ID, "wp-submit")

    def login(self, username, pwd):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email))
        self.driver.find_element(*self.email).send_keys(username)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.submit).click()
        return AllPostsPage(self.driver)

    def load(self):
        self.driver.get(self.url)

    def is_loaded(self):
        return "wp-admin" in self.driver.current_url



