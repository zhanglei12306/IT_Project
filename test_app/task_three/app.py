from appium import webdriver
# 开机 重启 关机 首页
from test_app.task_three.basepage import BasePage
from test_app.task_three.page.main_page import MainPage


class App(BasePage):
    def start(self):

        if self.driver == None:
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
            # 启动的Activity
            # desired_caps['appActivity'] = '.launch.WwMainActivity'
            # unicode设置(允许中文输入)
            desired_caps['unicodeKeyboard'] = True
            # 键盘设置(允许中文输入)
            desired_caps['resetKeyboard'] = True
            desired_caps['noReset'] = True
            desired_caps['dontStopAppOnReset'] = True
            desired_caps['settings[waitForIdleTimeout'] = 0

            # 只有声明驱动对象我们才可以让手机完成脚本的操作,声明的方法如下:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明对象后会直接启动参数中的应用
            self.driver.implicitly_wait(30)
        else:
            self.driver.launch_app()


    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.close_app()
        self.driver.quit()
        
        return self

    def goto_main(self):
        return MainPage(self.driver)