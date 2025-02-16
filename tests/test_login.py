import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Constants
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, PasswordRecoveryLocators


@pytest.mark.login
class TestLogin:
    def test_login_via_main_page(self, driver):
        # Вход через кнопку "Войти в аккаунт" на главной странице
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_login_via_personal_cabinet(self, driver):
        # Вход через кнопку "Личный Кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_login_via_registration_form(self, driver):
        # На странице регистрации переходим по ссылке "Войти" для перехода на форму авторизации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_login_via_password_recovery(self, driver):
        # На странице авторизации переходим по ссылке "Восстановить пароль", затем возвращаемся по ссылке "Войти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PasswordRecoveryLocators.LOGIN_LINK)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
