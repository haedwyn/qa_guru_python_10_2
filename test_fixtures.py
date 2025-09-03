import pytest

@pytest.fixture


@pytest.fixture
def login_page(browser):
    print ("Страница логина")
    pass


@pytest.fixture
def user():
    print ("Юзер")
    return "username" , "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"