from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AddNewPostPage import AddNewPostPage
from DeletePostPage import DeletePostPage
from DeletePostPage import DeletePostPage
from EditPostPage import EditPostPage


class AllPostsPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://demo-blog.seleniumacademy.com/wp/wp-admin/edit.php")
        self.posts_container = self.driver.find_element(By.ID, "the-list")
        self.search_posts = self.driver.find_element(By.ID, "post-search-input")
        self.view_by_categories = self.driver.find_element(By.ID, "cat")
        self.add_new_post = self.driver.find_element(By.LINK_TEXT, "Add New")

    def create_a_new_post(self, title, description):
        self.add_new_post.click()
        new_post = AddNewPostPage(self.driver)
        new_post.add_new_post(title, description)

    def edit_a_post(self, present_title, new_title, description):
        self.go_to_particular_post_page(present_title)
        edit_post = EditPostPage(self.driver)
        edit_post.edit_post(new_title, description)

    def delete_a_post(self, title):
        self.go_to_particular_post_page(title)
        delete_post = DeletePostPage(self.driver)
        delete_post.delete()



    def get_all_posts_count(self):
        posts_list = self.posts_container.find_elements(By.TAG_NAME, "tr")
        return len(posts_list)

    def go_to_particular_post_page(self, title):
        all_posts = self.posts_container.find_elements(By.CLASS_NAME, "title")
        for ele in all_posts:
            if ele.text == title:
                actions = ActionChains(self.driver)
                actions.move_to_element(ele).click(
                    self.driver.find_element(By.CSS_SELECTOR, ".edit>a")
                ).perform()
                break
