def test_delete_first_group(app):
        app.open_home_page_group()
        app.group.delete_first_group()
