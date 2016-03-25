from model.group import Group


def test_modify_group_name(app):
        app.open_home_page_group()
        app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
        app.open_home_page_group()
        app.group.modify_first_group(Group(header="New header"))
