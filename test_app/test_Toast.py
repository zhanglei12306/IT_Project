import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


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
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
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
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//* [@text='Search']").click()
        # print(self .driver .page_ source)
        # print(self.driver. find_ element (MobileBy.XPATH，"//* [@class= 'android. widget. Toast' ]")。text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains (@text, 'Clicked popup')]").text)
