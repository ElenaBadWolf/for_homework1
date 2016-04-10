from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    app.session.logincon(username="admin",password="secret")
    if app.contact.count()== 0:
       app.contact.create(Contact(firstname="test", middlename="gfgf", lastname="gfgf", nickname="gfg",
                               title="gfg", company="gfg", address="gfgf", home="gf", mobile="gfg",
                               work="gdfgfd",
                               fax="yuy", email2="kjhkhj", email3="kjhkjh", homepage="khjkjh",
                               byear="2005", ayear="2001", address2="gfdgfdg", phone2="jhjj",
                               notes="gfdgdf", ))
    app.contact.mod_contact()




def test_modification_some_contact(app):
    app.session.logincon(username="admin",password="secret")
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="test", middlename="gfgf", lastname="gfgf", nickname="gfg",
                               title="gfg", company="gfg", address="gfgf", homephone="gf", mobilephone="gfg",
                               workphone="gdfgfd",
                               fax="yuy", email2="kjhkhj", email3="kjhkjh", homepage="khjkjh",
                               byear="2005", ayear="2001", address2="gfdgfdg", secondaryphone="jhjj",
                               notes="gfdgdf", ))
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key = Contact.id_or_max)==sorted(new_contacts, key = Contact.id_or_max)