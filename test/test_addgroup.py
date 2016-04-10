# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group (name = "", header = "", footer = "")]+[
        Group(name = random_string("name", 10) , header = random_string("header",20) ,footer =random_string("footer",20))
        for i in range (5)
        ]

@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])

def test_test_addgroup(app, group):
        app.session.login(username="admin",password="secret")
        app.open_home_page_group()
        old_groups = app.group.get_group_list()
        app.group.init_creation()
        app.group.fill_form(group)
        app.group.submit_creation()
        app.group.return_to_groups_page()
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)

#def test_add_empty_group(app):
        #app.session.login(username="admin",password="secret")
        #app.open_home_page_group()
        #old_groups = app.group.get_group_list()
        #group = Group(name="", header="", footer="")
        #app.group.init_creation()
        #app.group.fill_form(group)
        #app.group.submit_creation()
        #app.group.returt_to_groups_page()
        #new_groups = app.group.get_group_list()
        #assert len(old_groups) + 1 == len(new_groups)
        #old_groups.append(group)
        #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key =Group.id_or_max)

