from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Applicationgroup():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def returt_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        # submit group creation
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def fill_groups_form(self, group):
        # fill group form
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self):
        # init group creation
        wd = self.wd
        wd.find_element_by_name("new").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/group.php")


    def destroy(self):
         self.wd.quit()
