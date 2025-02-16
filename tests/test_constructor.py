import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Constants
from locators import MainPageLocators, LoginPageLocators, ConstructorLocators


@pytest.mark.constructor
class TestConstructor:
    def test_constructor_tabs(self, driver):
        # 1. Входим в аккаунт через "Личный Кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # 2. Переходим в раздел "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)
        ).click()

        # 3. Проверка вкладки "Булки"
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']"))
        )

        # 4. Проверка вкладки "Соусы"
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        driver.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']"))
        )

        # 5. Проверка вкладки "Начинки"
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        driver.execute_script("arguments[0].click();", fillings_tab)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']"))
        )
