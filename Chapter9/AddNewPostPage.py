import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddNewPostPage:
    def __init__(self,driver):
        self.driver = driver
        self.new_post_content_frame = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content_ifr")))
        self.new_post_content_body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tinymce")))
        self.new_post_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
        self.new_post_publish = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "publish")))
    def add_new_post(self,title,desc_content):
        self.new_post_title.click()
        self.new_post_title.send_keys(title)
        self.driver.switch_to().frame(self.new_post_content_frame)
        self.new_post_content_body.send_keys(desc_content)
        self.driver.switch_to().defaultContent()
        self.new_post_publish.click()


