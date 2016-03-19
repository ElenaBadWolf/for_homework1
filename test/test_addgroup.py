# -*- coding: utf-8 -*-
import pytest
from fixture.applicationforgroup import Applicationgroup
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Applicationgroup()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_addgroup(app):
        app.open_home_page()
        app.session.login(username = "admin",password= "secret")
        app.init_group_creation()
        app.fill_groups_form(Group(name="test", header="test",footer= "test"))
        app.submit_group_creation()
        app.returt_to_groups_page()
        app.session.logout()

def test_add_empty_group(app):
        app.open_home_page()
        app.session.login(username = "admin",password= "secret")
        app.init_group_creation()
        app.fill_groups_form(Group(name="", header="",footer= ""))
        app.submit_group_creation()
        app.returt_to_groups_page()
        app.session.logout()





