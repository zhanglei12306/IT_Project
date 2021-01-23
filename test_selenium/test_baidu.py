from selenium import webdriver
import time
import json


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
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()


        time.sleep(8)
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts68"]/div/div[2]/div/div[4]/div/form/div[2]/div[5]/div/div[2]/label/input').click()



    def test_login(self):
        self.driver.get('https://www.baidu.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '[class="index_head_info_pCDownloadBtn"]').click()
        self.driver.find_element(By.ID, 'kw').send_keys('python')
        time.sleep(3)
        self.driver.find_element(By.linkText("百度一下")).click()




