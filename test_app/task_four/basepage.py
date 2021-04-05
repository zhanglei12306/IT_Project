import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_app.task_four.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_send(self, locator, text):
        return self.find(locator).send_keys(text)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        return self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def run_steps(self, page_path, operation):
        # yaml 的读取
        with open(page_path, 'r', encoding="utf-8") as f:
            data = yaml.load(f)
            print(data)
            print('*' * 100)
        # 支持 PO 下多个操作
        steps = data[operation]
        print(steps)
        # 遍历每一个动作
        for step in steps:
            print('*'*100)
            # print(step)
            action = step['action']
            # 如果动作是 find_and_click ，就调用 basepage 中的 find_and_click
            if action == "find_and_click":
                # 调用 find_and_click 并且传入相应参数
                self.find_and_click(step['locator'])
            elif action == "find_and_send":
                self.find_and_send(step['locator'], step['content'])