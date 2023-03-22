from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditPostPage:
    def __init__(self, driver):
        self.driver = driver
        print(driver.current_url)

    new_post_content_frame = (By.ID, "content_ifr")
    new_post_content_body = (By.ID, "tinymce")
    new_post_title = (By.ID, "title")
    new_post_publish = (By.ID, "publish")

    def edit_post(self, title, desc_content):
        new_post_title = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_post_title))
        new_post_title.click()
        new_post_title.clear()
        new_post_title.send_keys(title)
        self.driver.switch_to.frame(self.driver.find_element(*self.new_post_content_frame))
        new_post_content_body = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_post_content_body))
        new_post_content_body.clear()
        new_post_content_body.send_keys(desc_content)
        self.driver.switch_to.default_content()
        new_post_publish = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_post_publish))
        new_post_publish.click()
