import pytest
from fixture.application import Application
import json
target = None
import os.path

@pytest.fixture
def app(request):
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    fixture=Application(browser= browser, base_url = target['baseUrl'])
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "firefox")
    parser.addoption("--target", action="store", default = "target.json")