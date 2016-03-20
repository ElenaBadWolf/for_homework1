import pytest
from fixture.applicationforgroup import Applicationgroup


@pytest.fixture(scope="session")
def app(request):
    fixture = Applicationgroup()
    request.addfinalizer(fixture.destroy)
    return fixture