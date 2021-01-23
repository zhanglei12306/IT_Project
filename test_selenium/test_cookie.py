from selenium import webdriver
import time
import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestQywx:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     time.sleep(20)
    #     self.driver.quit()

    def test_cookie(self):
    #
    #     time.sleep(10)
    #     # 获取  cookie
    #     cookies = self.driver.get_cookies()
    #     # 以文件流的形式打开文件
    #     with open("cookie.json", "w") as f:
    #         # 存储 cookie 到 cookie.json
    #         json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        # 以文件的形式打开文件
        with open("testcase/cookies.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 添加 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.ID, 'menu_contacts').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        #
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[name=name]').send_keys('销售部')
        # bg = self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name')
        # ActionChains(self.driver).move_to_element(bg).perform()
        #
        # time.sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853816204003_anchor"]').click()
        #
        # time.sleep(3)
        # self.driver.find_element(By.CSS_SELECTOR, '.ww_btn_Blue').click()

        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list").click()

        self.driver.find_element(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853816204003_anchor"]').click()
    #
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()





    def test_login(self):
        self.driver.get('https://work.weixin.qq.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '[class="index_head_info_pCDownloadBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[class="index_top_operation_loginBtn"]').click()

        time.sleep(10)
        # 获取  cookie
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        with open("testcase/cookies.json", "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)
        self.driver.find_element(By.CSS_SELECTOR, '[id="menu_contacts"]').click()


