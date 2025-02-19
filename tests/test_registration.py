import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators
from constants import Constants


def generate_unique_email():
    """Генерация уникального email"""
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"testuser_05_{random_digits}@example.com"


@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, driver):
        # Переход в "Личный Кабинет" и далее в форму регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )

        # Заполнение формы регистрации с использованием данных
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(Constants.NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Ожидание перехода на страницу авторизации (проверка наличия поля Email)
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        # Явный assert – проверяем, что поле отображается
        assert email_input.is_displayed(), "Поле Email не отображается после регистрации"

    def test_registration_invalid_password(self, driver):
        # Регистрация с некорректным паролем (менее 6 символов)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(Constants.NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Ожидание появления сообщения об ошибке
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert "Некорректный пароль" in error_element.text, "Ошибка для некорректного пароля не отображается"
