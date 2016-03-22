def test_delete_first_contact(app):
    app.session.logincon(username="admin",password="secret")
    app.contact.delete_first_contact()
