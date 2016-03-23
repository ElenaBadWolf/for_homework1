def test_edit_contact(app):
    app.session.logincon(username="admin",password="secret")
    app.contact.mod_contact()
