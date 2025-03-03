# Автоматизированное тестирование Stellar Burgers

## Описание проекта

Этот проект предназначен для автоматизированного тестирования веб-приложения **Stellar Burgers** с использованием **Selenium WebDriver** и **PyTest**. Тесты покрывают основные функции сервиса:

- Регистрация
- Авторизация (вход)
- Переход в личный кабинет
- Переход из личного кабинета в конструктор
- Раздел «Конструктор» (булки, соусы, начинки)
- Выход из аккаунта

Все тесты хранятся в папке `tests/`, при этом каждая функциональность вынесена в отдельный файл:
1. **test_registration.py** — тесты регистрации  
2. **test_login.py** — тесты авторизации (входа)   
3. **test_constructor.py** — тесты для раздела «Конструктор»  
5. **test_logout.py** — тесты выхода из аккаунта

> Обратите внимание, что для удобства в вашем проекте имена файлов могут отличаться, но важно соблюдать принцип «одна функциональность — один файл».

## Стек технологий

- **Python** 3+
- **Selenium WebDriver**
- **PyTest**

## Установка и настройка

1. **Клонировать репозиторий**:
   ```bash
   git clone <ссылка на репозиторий>
   cd Sprint_5
   ```
2. **Создать виртуальное окружение и установить зависимости**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # для Windows
   pip install -r requirements.txt
   ```
3. **Установить веб-драйверы** (Chrome, Firefox):
   - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - [GeckoDriver (для Firefox)](https://github.com/mozilla/geckodriver/releases)

## Запуск тестов

Для запуска всех тестов:
```bash
pytest tests/
```

Если нужно указать конкретный браузер:
```bash
pytest --browser=chrome  # или firefox
```

## Структура проекта

```bash
Sprint_5/
├── tests/
│   ├── test_registration.py  # Тесты на регистрацию
│   ├── test_login.py         # Тесты на авторизацию
│   ├── test_logout.py       # Тесты на выход
│   ├── test_constructor.py   # Тесты на конструктор
├── locators.py               # Все локаторы в одном месте
├── conftest.py               # Общие фикстуры (WebDriver и т. д.)
├── constants.py              # Константы (URL, тестовые данные)
├── README.md
├── .gitignore
├── requirements.txt
```

- **tests/**: В каждом файле свои тесты для одной функциональности, при этом тесты сгруппированы по классам.
- **locators.py**: Описание локаторов.
- **conftest.py**: Общие фикстуры для инициализации/завершения Selenium.
- **constants.py**: Содержит основные константы, такие как URL стенда, тестовые логин/пароль, текстовые сообщения и т.д.
- **requirements.txt**: Список зависимостей.
- **.gitignore**: Файлы и папки, которые не коммитим (например, `venv/`).

## Автор

[Игорь Трофимов]

