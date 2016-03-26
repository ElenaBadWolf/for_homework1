from model.contact import Contact

def test_edit_contact(app):
    app.session.logincon(username="admin",password="secret")
    if app.contact.count()== 0:
       app.contact.create(Contact(firstname="test", middlename="gfgf", lastname="gfgf", nickname="gfg",
                               title="gfg", company="gfg", address="gfgf", home="gf", mobile="gfg",
                               work="gdfgfd",
                               fax="yuy", email2="kjhkhj", email3="kjhkjh", homepage="khjkjh",
                               byear="2005", ayear="2001", address2="gfdgfdg", phone2="jhjj",
                               notes="gfdgdf", ))
       app.return_to_home_page()
    app.contact.mod_contact()
