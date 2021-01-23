import time

from selenium.webdriver.common.by import By

from test_selenium.page.contacts_page import ContactsPage
from test_selenium.page.url_page import BasePage


class AddMembers(BasePage):
    _name = (By.ID, "username")
    _acctid = (By.ID, "memberAdd_acctid")
    _phone = (By.ID, "memberAdd_phone")
    # 添加成员
    def add_members(self, name, acctid, phone):
        # 输入成员信息，点击保存
        # self.find(By.ID, 'username').send_keys('剑圣李白')
        # self.find(By.ID, 'memberAdd_acctid').send_keys('159')
        self.find(*self._name).send_keys(name)
        self.find(*self._acctid).send_keys(acctid)
        self.find(*self._phone).send_keys(phone)
        time.sleep(2)
        # self.find(By.LINK_TEXT, "通过邮件或短信发送企业邀请").click()
        self.find(By.CSS_SELECTOR, '[name=sendInvite]').click()
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactsPage(self.driver)

    def add_members_fail(self, phone):
        # 输入成员信息，点击保存
        self.find(By.ID, 'username').send_keys('剑圣李白')
        self.find(By.ID, 'memberAdd_acctid').send_keys('160')
        self.find(*self._phone).send_keys(phone)
        time.sleep(3)

        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

        return ContactsPage(self.driver)


