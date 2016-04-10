# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits +  " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact ( firstname = "", middlename = "", lastname = "", nickname= "" , title= "", company= "", address = "",
                      homephone = "", mobilephone = "", workphone = "", fax = "", email2 = "", email3 = "", homepage = "", byear = "", ayear = "", address2 = "", secondaryphone = "",
        notes = "")]+[
        Contact(firstname = random_string("firstname", 10) , middlename = random_string("middlename",20) ,lastname =random_string("lastname",20), nickname =random_string("nickname",20),
               title = random_string("title",20 ), company=random_string("company",20),address=random_string("address",20),homephone=random_string("homephone",20),
                                                   mobilephone = random_string("mobilephone",20),workphone=random_string("workphone",20), fax=random_string("fax",20),email2=random_string("email2",20),
                email3 = random_string("email3",20), homepage=random_string("homepage",20), byear=random_string("byear",20), ayear=random_string("ayear",20), address2=random_string("adress2",20),
                secondaryphone=random_string("secondaryphone",20), notes=random_string("notes",20))
        for i in range (5)
        ]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])

def test_add_new_contact(app, contact):
    app.session.logincon(username="admin",password="secret")
    old_contacts = app.contact.get_contact_list()
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    app.contact.create(contact)
    app.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))


#def test_add_new_empty_contact(app):
    #app.session.logincon(username="admin",password="secret")
    #app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              # address="", home="", mobile="", work="gdfgfd",
                              # fax="", email2="", email3="kjhkjh", homepage="khjkjh", byear="2005",
                              # ayear="2001", address2="gfdgfdg", phone2="jhjj", notes="gfdgdf", ))
    #app.return_to_home_page()
