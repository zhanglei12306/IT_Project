import os


import pytest
import yaml
from appium import webdriver
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def get_data():
    path = os.path.dirname(__file__) + "/task_add_members.yml"
    with open(path, encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        print(datas)
        # 获取文件中key为datas的数据
        add_datas = datas["adds"]
        print(add_datas)
        return add_datas

class TestCase:
    def setup(self):
        # server 启动参数
        desired_caps = {}

        # 设备信息
        # 平台的名称
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '6.0.1'
        # 设备号
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 启动的包
        # desired_caps['appPackage'] = 'com.tencent.wework'
        # # 启动的Activity
        # desired_caps['appActivity'] = '.launch.WwMainActivity'
        # unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # 键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        # 只有声明驱动对象我们才可以让手机完成脚本的操作,声明的方法如下:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明对象后会直接启动参数中的应用
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_close']").click()
        # self.driver.quit()
    @pytest.mark.parametrize("searchkey, types, current_price", [('阿里巴巴', 'BABA', 250), ('小米集团-W', '01810', 29)])
    def test_wait(self, searchkey, types, current_price):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name'  and  @text='{searchkey}']").click()
        locator = (By.XPATH, f"//*[@text='{types}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        # current_price = float(self.driver.find_element(*locator).text)
        # print(current_price)
        # assert current_price > 200
        ele = float(WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locator)).text)
        print(ele)
        # assert float(ele) > 200
        assert_that(ele, close_to(current_price, current_price*0.1))

    @pytest.mark.parametrize("searchkey, types, current_price", get_data())
    def test_wait(self, searchkey, types, current_price):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(By.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name'  and  @text='{searchkey}']").click()
        locator = (By.XPATH, f"//*[@text='{types}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        # current_price = float(self.driver.find_element(*locator).text)
        # print(current_price)
        # assert current_price > 200
        ele = float(WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locator)).text)
        print(ele)
        # assert float(ele) > 200
        assert_that(ele, close_to(current_price, current_price*0.1))



