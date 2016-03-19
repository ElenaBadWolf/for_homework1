# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.sessioncontact.login(username="admin",password="secret")
    app.contact.create(Contact(firstname="fghjfgfgfg", middlename="gfgf", lastname="gfgf", nickname="gfg",
                               title="gfg", company="gfg", address="gfgf", home="gf", mobile="gfg",
                               work="gdfgfd",
                               fax="yuy", email2="kjhkhj", email3="kjhkjh", homepage="khjkjh",
                               byear="2005", ayear="2001", address2="gfdgfdg", phone2="jhjj",
                               notes="gfdgdf", ))
    app.return_to_home_page()

def test_add_new_empty_contact(app):
    app.sessioncontact.login(username="admin",password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="gdfgfd",
                               fax="", email2="", email3="kjhkjh", homepage="khjkjh", byear="2005",
                               ayear="2001", address2="gfdgfdg", phone2="jhjj", notes="gfdgdf", ))
    app.return_to_home_page()