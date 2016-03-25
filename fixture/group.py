class GroupHelper:
    def __init__(self, app):
        self.app = app

    def returt_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def submit_creation( self ):
        # submit group creation
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_form( self, group ):
        # fill group form
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group.footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group(wd)
        # submit deletion
        wd.find_element_by_name("delete").click()

    def select_first_group(self, wd):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def init_creation(self):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def mod_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").send_keys("changes")
        wd.find_element_by_name("update").click()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.select_first_group(wd)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()

