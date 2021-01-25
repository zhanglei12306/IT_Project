

# 手动输入添加
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

from test_app.tasktwo.page.basepage import BasePage
from test_app.tasktwo.page.contactedit_dage import ContactEditPage


class ManualInputAdd(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_menmebere_info(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ContactEditPage(self.driver)

    def goto_toast(self):
        ele = self.find_and_get_text((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        print(ele)
        return ele

