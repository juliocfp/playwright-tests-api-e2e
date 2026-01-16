import pytest
from pages.account_page import AccountPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def account_page(page):
    return AccountPage(page)