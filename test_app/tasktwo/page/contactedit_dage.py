from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_app.tasktwo.page.basepage import BasePage


class ContactEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_name(self, name):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/b78']").send_keys(name)
        return self

    def edit_gender(self, gender):
        loc = (MobileBy.XPATH, "//*[@text='男']")
        elem = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(loc))
        elem.click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        return self

    def edit_phone(self, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fuy']").send_keys(phone)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fim").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/fim"))
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ie7").click()
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        from test_app.tasktwo.page.manualinputadd_page import ManualInputAdd
        return ManualInputAdd(self.driver)