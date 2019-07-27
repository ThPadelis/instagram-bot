from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(5)
        email = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_posts(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(0, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(5)
            posts = driver.find_elements_by_class_name("eLAPa")
        for post in posts:
            post.click()
            time.sleep(2)
            driver.find_element_by_class_name("fr66n").click()
            time.sleep(2)
            driver.find_element_by_class_name("ckWGn").click()
            time.sleep(5)