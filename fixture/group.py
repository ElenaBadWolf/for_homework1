

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
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_creation( self ):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_name("new").click()
