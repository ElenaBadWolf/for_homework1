from model.group import Group
from random import randrange

def test_modify_group_name(app):
        app.session.login(username = "admin",password= "secret")
        app.open_home_page_group()
        if app.group.count() == 0:
           app.open_home_page_group()
           app.group.init_creation()
           app.group.fill_form(Group(name="test"))
           app.group.submit_creation()
           app.group.return_to_groups_page()
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        app.group.modify_group_by_index(Group(name="name"),index)
        app.open_home_page_group()
        assert len(old_groups)  == app.group.count()
        new_groups = app.group.get_group_list()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)


#def test_modify_group_header(app):
        app.session.login(username = "admin",password= "secret")
        app.open_home_page_group()
        old_groups = app.group.get_group_list()
        group = Group (name = "New group")
        group.id = old_groups[0].id
        app.group.modify_first_group(Group(header="New header"))
        new_groups = app.group.get_group_list()
        assert len(old_groups)  == len(new_groups)
        new_groups = app.group.get_group_list()
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)


