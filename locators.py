from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Личный кабинет" для перехода в личный кабинет
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Ссылка "Конструктор" для перехода в раздел конструктора
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers для перехода в конструктор по клику
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

class RegistrationPageLocators:
    # Поле "Имя" для ввода имени пользователя при регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле "Email" для ввода электронной почты при регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль" для ввода пароля при регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка "Зарегистрироваться" для отправки формы регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Элемент для отображения сообщения об ошибке (например, некорректный пароль)
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Ссылка "Войти" для перехода на форму авторизации с формы регистрации
    LOGIN_LINK = (By.LINK_TEXT, "Войти")

class LoginPageLocators:
    # Надпись "Вход" на странице авторизации (после выхода из аккаунта)
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    # Поле "Email" для ввода электронной почты при авторизации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль" для ввода пароля при авторизации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка "Войти" для отправки формы авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Восстановить пароль" для перехода на форму восстановления пароля
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

class PasswordRecoveryLocators:
    # Ссылка "Войти" для возврата к форме авторизации с формы восстановления пароля
    LOGIN_LINK = (By.LINK_TEXT, "Войти")

class PersonalCabinetLocators:
    # Кнопка "Выход" для выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class ConstructorLocators:
    # Вкладка "Булки" в разделе конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    # Вкладка "Соусы" в разделе конструктора
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    # Вкладка "Начинки" в разделе конструктора
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    # Локаторы для активного состояния вкладок
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")