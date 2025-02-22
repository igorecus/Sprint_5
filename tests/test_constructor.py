import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, ConstructorLocators
from constants import Constants

@pytest.mark.constructor
class TestConstructor:
    def login_and_navigate(self, driver):
        # Входим через "Личный Кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Переходим в раздел "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)
        ).click()

    def test_constructor_buns(self, driver):
        self.login_and_navigate(driver)
        # Кликаем по вкладке "Булки"
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)
        # Ждём, пока появится активный элемент для вкладки "Булки"
        active_buns = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.BUNS_TAB_ACTIVE)
        )
        assert active_buns.is_displayed(), "Вкладка 'Булки' не активирована"

    def test_constructor_sauces(self, driver):
        self.login_and_navigate(driver)
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        driver.execute_script("arguments[0].click();", sauces_tab)
        active_sauces = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.SAUCES_TAB_ACTIVE)
        )
        assert active_sauces.is_displayed(), "Вкладка 'Соусы' не активирована"

    def test_constructor_fillings(self, driver):
        self.login_and_navigate(driver)
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        driver.execute_script("arguments[0].click();", fillings_tab)
        active_fillings = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.FILLINGS_TAB_ACTIVE)
        )
        assert active_fillings.is_displayed(), "Вкладка 'Начинки' не активирована"
