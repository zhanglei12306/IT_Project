import os
import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 启动的包
        desired_caps['appPackage'] = 'com.tencent.wework'
        # 启动的Activity
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # 键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['settings[waitForIdleTimeout'] = 0

        # 只有声明驱动对象我们才可以让手机完成脚本的操作,声明的方法如下:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明对象后会直接启动参数中的应用
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("name, gender, phone", get_data())
    def test_add_members(self, name, gender, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq'  and  @text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/b78']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fuy']").send_keys(phone)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fim").click()
        # 保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert ele == '添加成功'















