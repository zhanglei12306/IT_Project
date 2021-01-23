from selenium.webdriver.common.by import By

from test_selenium.page.contacts_page import ContactsPage
from test_selenium.page.url_page import BasePage


class DepartmentPage(BasePage):

    # 添加部门
    def add_department(self):

        self.find(By.CSS_SELECTOR, '[name=name]').send_keys('销售部')
        # time.sleep(3)
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        # 先定位弹框  再取弹框内容
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688853816204003_anchor"]').click()
        # 父子节点查询
        self.find(By.CSS_SELECTOR, ".qui_dialog_foot a:nth-child(1)").click()
        return ContactsPage(self.driver)




