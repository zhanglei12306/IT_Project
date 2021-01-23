import time

from selenium.webdriver.common.by import By

from test_selenium.page.url_page import BasePage


class ContactsPage(BasePage):
    # 添加成员
    def add_members(self):
        pass


    # 添加部门
    def add_departments(self):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        from test_selenium.page.add_departmentp_page import DepartmentPage
        return DepartmentPage(self.driver)



    def get_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        print(name_list)

        return name_list

    def get_list_department(self):
        """
        返回通讯录页面的部门信息
        :return:
        """
        time.sleep(5)
        name_department_list = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        print(name_department_list)
        department_list = []
        for department in name_department_list:
            print(department.text)
            department_list.append(department.text)
        # print(department_list)
        return department_list

