import allure
import pytest
from pages.address_page import AddressPage
from pages.payment_page import PaymentPage
from pages.login_checkout_page import LoginCheckoutPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def account_page(page):
    return AccountPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def login_checkout_page(page):
    return LoginCheckoutPage(page)

@pytest.fixture
def address_page(page):
    return AddressPage(page)

@pytest.fixture
def payment_page(page):
    return PaymentPage(page)

@pytest.fixture(autouse=True)
def cloudflare_verification(page: Page):
    if page.get_by_text("Verify you are human by completing the action below.").is_visible():
        pytest.skip("SKIPPED: Cloudflare detectado.")

@allure.title("Evidência final automática após teste")
@pytest.fixture(autouse=True)
def take_evidence_automatically(page: Page):
    yield
    try:
        allure.attach(
            page.screenshot(full_page=True),
            name="Evidência Final",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Erro ao tirar evidência final: {e}")

def pytest_bdd_before_scenario(feature, scenario):
    allure.dynamic.title(scenario.name)
    allure.dynamic.feature(feature.name)
    filename = feature.rel_filename.split("/")[-1]
    allure.dynamic.story(filename)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "viewport": {"width": 1920, "height": 1080},
        "device_scale_factor": 1,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": [
            "--disable-blink-features=AutomationControlled",
            "--start-maximized",
            "--no-sandbox",
            "--disable-infobars"
        ]
    }
