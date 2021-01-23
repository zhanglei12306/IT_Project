from selenium.webdriver.common.by import By

from test_selenium.page.add_members_page import AddMembers

from test_selenium.page.url_page import BasePage


class MainPage(BasePage):



    # 通讯录 添加人员
    def goto_cntacts(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        return AddMembers(self.driver)

    # 通讯录 添加部门
    def goto_cntacts_department(self):
        self.find(By.ID, 'menu_contacts').click()
        from test_selenium.page.contacts_page import ContactsPage
        return ContactsPage(self.driver)



