from selenium import webdriver
import time
import json


from selenium.webdriver.common.by import By


class TestQywx:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_cookie(self):
        # 获取  cookie
        # cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        # with open("cookie.json", "w") as f:
            # 存储 cookie 到 cookie.json
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        # 以文件的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 添加 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu_customer"]').click()

    def test_login(self):
        # self.driver.get('https://work.weixin.qq.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '[class="index_head_info_pCDownloadBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu_contacts"]').click()


