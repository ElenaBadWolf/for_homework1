from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
         try:
             self.wd.current_url
             return True
         except:
             return False


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")


    def open_home_page_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/group.php")


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()