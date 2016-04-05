# -*- coding: utf-8 -*-
from model.group import Group



def test_test_addgroup(app):
        app.session.login(username="admin",password="secret")
        app.open_home_page_group()
        old_groups = app.group.get_group_list()
        group = Group(name="test", header="test", footer="test")
        app.group.init_creation()
        app.group.fill_form(group)
        app.group.submit_creation()
        app.group.returt_to_groups_page()
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)

def test_add_empty_group(app):
        app.session.login(username="admin",password="secret")
        app.open_home_page_group()
        old_groups = app.group.get_group_list()
        group = Group(name="", header="", footer="")
        app.group.init_creation()
        app.group.fill_form(group)
        app.group.submit_creation()
        app.group.returt_to_groups_page()
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)

