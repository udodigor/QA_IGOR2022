import pytest
# Дано список з 5 словників. Написати тест, що перевіряє чи всім є 18 років,
# при падінні теста помилка має містити імена всіх неповнолітніх

my_friends = [{"name": "Rost", "age": 22}, {"name": "Bodya", "age": 19}, {"name": "Andrey", "age": 125},
{"name": "Ira", "age": 26}, {"name": "Igor", "age": 33}]

@pytest.mark.parametrize(["name", "age"], [people.values() for people in my_friends])
def test_all_adults(name, age):
    assert age > 18, f"Young_friend: {name}"


# 2. Створити класс з властивостями, що задаються при ініцілізації:
# 1) Параметр login(str). Значення за замовчування - порожня строка.
# 2) Параметр password(str). Значення за замовчуванням - порожня строка.
# 3) Метод sign_in_enabled.  Який повертає True, якщо логін і пароль заповнені і False, якщо хоча б одне з полів пусте
import pytest

class LoginForm:

    def __init__(self, login="", password=""):
        self.login = login
        self.password = password

    def sign_in_successed(self):
        return bool(self.login) and bool(self.password)


def test_default():
    login_form = LoginForm()
    assert not login_form.sign_in_successed(), f"Actual value: {login_form.sign_in_successed()}"


def test_only_login():
    login_form = LoginForm(login="IGOR-UDOD-1234567")
    assert not login_form.sign_in_successed(), f"Actual value: {login_form.sign_in_successed()}"
    print("Заполнено одно поле")


def test_only_password():
    login_form = LoginForm(password="0123456789010")
    assert not login_form.sign_in_successed(), f"Actual value: {login_form.sign_in_successed()}"
    print("Заполнено только поле")


def test_log_and_pass():
    login_form = LoginForm(login="IGORUDOD", password="0123456789010D")
    assert login_form.sign_in_successed(), f"Actual value: {login_form.sign_in_successed()}"
    print("Все поля заполнены")

    login_form.password = ""
    assert not login_form.sign_in_successed(), f"Actual value: {login_form.sign_in_successed()}"
    print("Кнопка не доступна после очистки одного поля")
