
from appium import webdriver
from selenium.webdriver.common.by import By

from hamcrest import *


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
        # desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        # 只有声明驱动对象我们才可以让手机完成脚本的操作,声明的方法如下:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明对象后会直接启动参数中的应用
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_get_attribute(self):

        ele = self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search')
        print(ele.get_attribute('resource-id'))

        # self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'  and  @text='阿里巴巴']").click()
        # current_price = float(self.driver.find_element(By.XPATH, "com.xueqiu.android:id/current_price").text)
        # print(current_price)
        # assert current_price > 200

    def test_hamcrest(self):
        # 相等
        # assert_that(10, equal_to(10))
        # assert_that(10, equal_to(19), '不相等')
        # 相加
        # assert_that(10, close_to(9, 1))
        # 包含
        assert_that("asd fgh jkl", contains_string("fgh"))









