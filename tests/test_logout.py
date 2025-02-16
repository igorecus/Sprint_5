import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import Constants
from locators import MainPageLocators, LoginPageLocators, PersonalCabinetLocators


@pytest.mark.logout
class TestLogout:
    def test_logout(self, driver):
        # 1. Выполняем вход через "Личный Кабинет"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # 2. После входа пользователь перенаправляется на главную страницу.
        # Нажимаем снова на "Личный Кабинет", чтобы открыть меню профиля.
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)
        ).click()

        # 3. Нажимаем на кнопку "Выход"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BUTTON)
        ).click()

        # 4. Проверяем, что на странице авторизации отображается надпись "Вход"
        login_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER)
        )
        assert login_header.is_displayed(), "Надпись 'Вход' не отображается после выхода из аккаунта"
