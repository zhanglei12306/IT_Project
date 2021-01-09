from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


class TestQywx:

    def setup(self):

        # 复用已开的浏览器  chrome --remote-debugging-port=9222
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)


    # def teardown(self):
    #     time.sleep(5)
    #     self.driver.quit()

    def test_login(self):
        # self.driver.get('https://work.weixin.qq.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '[class="index_head_info_pCDownloadBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu_customer"]').click()


