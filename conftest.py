import pytest
from fixture.application import Application
import json
target = None

@pytest.fixture
def app(request):
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    fixture=Application(browser= browser, base_url = target['baseUrl'])
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "firefox")
    parser.addoption("--target", action="store", default = "target.json")