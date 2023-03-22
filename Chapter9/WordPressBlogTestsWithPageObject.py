import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from AdminLoginPage import AdminLoginPage
import unittest

class WordPressBlogTestsWithPageObject(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_add_new_post(self):
        username = "admin"
        password = "$$SUU3$$N#"
        self.driver.get('http://demo-blog.seleniumacademy.com/wp/wp-admin')
        login_page = AdminLoginPage(self.driver)
        all_posts_page = login_page.login(username, password)
        all_posts_page.create_a_new_post("Creating New Post using PageObjects","Its good to use PageObjects")
    def test_edit_post(self):
        username = "admin"
        password = "$$SUU3$$N#"
        self.driver.get('http://your-wordpress-site.com/wp-admin')
        login_page = AdminLoginPage(self.driver)
        all_posts_page = login_page.login(username, password)
        all_posts_page.edit_a_post("Creating New Post using PageObjects",
                                   "Editing Post using PageObjects",
                                   "Test framework low maintenance")
    def test_delete_post(self):
        username = "admin"
        password = "$$SUU3$$N#"
        self.driver.get('http://your-wordpress-site.com/wp-admin')
        login_page = AdminLoginPage(self.driver)
        all_posts_page = login_page.login(username, password)
        all_posts_page.delete_a_post("Editing Post using PageObjects")
    def test_post_Count(self):
        self.driver.get('http://demo-blog.seleniumacademy.com/wp/wp-admin')
        email = self.driver.find_element(By.ID,"user_login")
        pwd = self.driver.find_element(By.ID,"user_pass")
        submit = self.driver.find_element(By.ID,"wp-submit")
        email.send_keys("admin")
        pwd.send_keys("$$SUU3$$N#")
        submit.click()
        self.driver.get("http://demo-blog.seleniumacademy.com/wp/wp-admin/edit.php")
        postsContainer = self.driver.find_element(By.ID,"the-list")
        postsList = postsContainer.find_elements(By.TAG_NAME,"tr")
        self.assertEqual(len(postsList),1,"Không chính xác")



