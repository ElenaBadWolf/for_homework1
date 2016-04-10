from model.group import Group
from random import randrange


def test_delete_some_group(app):
        app.session.logincon(username="admin",password="secret")
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.return_to_groups_page()
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        app.group.delete_group_by_index(index)
        assert len(old_groups) - 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index:index+1] = []
        assert old_groups == new_groups




def test_delete_first_group(app):
        app.session.logincon(username="admin",password="secret")
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.return_to_groups_page()
        old_groups = app.group.get_group_list()
        app.group.delete_first_group()
        assert len(old_groups) - 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[0:1] = []
        assert old_groups == new_groups