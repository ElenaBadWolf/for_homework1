# -*- coding: utf-8 -*-
import pytest
from group import Group
from applicationforgroup import Applicationgroup





@pytest.fixture
def app(request):
    fixture = Applicationgroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_addgroup(app):
        app.open_home_page()
        app.login(username = "admin",password= "secret")
        app.init_group_creation()
        app.fill_groups_form(Group(name="test", header="test",footer= "test"))
        app.submit_group_creation()
        app.returt_to_groups_page()
        app.logout()


def test_add_empty_group(app):
        app.open_home_page()
        app.login(username = "admin",password= "secret")
        app.init_group_creation()
        app.fill_groups_form(Group(name="", header="",footer= ""))
        app.submit_group_creation()
        app.returt_to_groups_page()
        app.logout()





