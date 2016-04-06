from model.group import Group

def test_delete_first_group(app):
        app.session.logincon(username="admin",password="secret")
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.returt_to_groups_page()
        old_groups = app.group.get_group_list()
        app.group.delete_first_group()
        app.open_home_page()
        assert len(old_groups) - 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[0:1] = []
        assert old_groups == new_groups