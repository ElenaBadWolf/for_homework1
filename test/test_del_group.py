from model.group import Group

def test_delete_first_group(app):
        app.session.login(username="admin",password="secret")
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.returt_to_groups_page()
        app.group.delete_first_group()
