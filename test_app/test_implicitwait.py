import time
from appium import webdriver
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
        self.driver.quit()

    def test_find(self):
        '''
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框里面输入"阿里巴巴"
        4.在搜索结果里面选择"阿里巴巴”，然后进行点击
        5.获取这只上香港阿里巴巴的股价,并判断这只股价的价格>200
        :return:
        '''
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'  and  @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element(By.XPATH, "com.xueqiu.android:id/current_price").text)
        print(current_price)
        assert current_price > 200

    def test_attar(self):
        '''
        案例
        打开[雪球]应用首页
        定位首页的搜索框
        判断搜索框的是否可用,并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入: alibaba
        判断[阿里巴巴]是否可见
        如果可见，打印”搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        '''
        elem_find = self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search')
        elem = elem_find.is_enabled()
        print(elem)
        print(elem_find.text)
        print(elem_find.location)
        print(elem_find.size)
        if elem == True:
            elem_find.click()
            elem_ali = self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            el_displayed = elem_ali.get_attribute('displayed')
            print(elem_ali.get_attribute('displayed'))
            if el_displayed == 'true':
                print('搜索成功')
            else:
                print('搜索失败')


    def test_huadong(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_st = int(height * 4/5)
        y_en = int(height * 1/5)
        print(window_rect)
        # self.driver.swipe(width, height, x1, y1, 3000)
        # 滑动
        action.press(x=x1, y=y_st).move_to(x=x1, y=y_en).wait(2000).release().perform()

    def test_jiedian(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'  and  @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element(By.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)
        assert current_price > 200


    def test_myinfo(self):
        '''
        1，点击我的进入到个人信息页面
        2,点击登录，进入到登录页面
        3,输入用户名，输入密码,
        4，点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('789')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()


    def test_find_huadong(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scolIntoView(new UiSelector().text("ice_招行谷子地").instance(0))').click()

    def test_wait(self):
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'  and  @text='阿里巴巴']").click()
        locator = (By.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        # current_price = float(self.driver.find_element(*locator).text)
        # print(current_price)
        # assert current_price > 200
        ele = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locator)).text
        print(ele)
        assert float(ele) > 200





