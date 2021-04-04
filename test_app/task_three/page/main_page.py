
# 去通讯录页面
from test_app.task_three.basepage import BasePage
from test_app.task_three.page.marker_page import MarkerPage
from appium.webdriver.common.mobileby import MobileBy




class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_markers(self):
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarkerPage(self.driver)