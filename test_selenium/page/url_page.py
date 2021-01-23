import json
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage:

    _base_url = ''
    def __init__(self, driver:WebDriver=None):

        self.driver = ''
        if driver is None:
            self.driver = webdriver.Chrome()
            self.cookies_login()

        else:
            self.driver = driver
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # self.test_login()

    def cookies_login(self):
        # 以文件的形式打开文件
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件的形式打开文件
        with open("cookies.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 添加 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(6)
        # self.driver.find_element(By.CSS_SELECTOR, '[id="menu_customer"]').click()

    def test_login(self):
        self._driver.get('https://work.weixin.qq.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '[class="index_head_info_pCDownloadBtn"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '[class="index_top_operation_loginBtn"]').click()

        time.sleep(10)
        # 获取  cookie
        cookies = self._driver.get_cookies()
        # 以文件流的形式打开文件
        with open("cookie.json", "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)
        self._driver.find_element(By.CSS_SELECTOR, '[id="menu_contacts"]').click()

    def find(self, by, loactor):
        return self.driver.find_element(by, loactor)
