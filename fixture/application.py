from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessioncontact import SessionHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.sessioncontact = SessionHelper(self)
        self.contact = ContactHelper

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")



    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()