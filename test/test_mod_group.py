from model.group import Group

def test_mod_group(app):
        app.open_home_page_group()
        app.session.login(username = "admin",password= "secret")
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.return_to_groups_page()
        app.group.mod_group()