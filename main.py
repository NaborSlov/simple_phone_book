#!/usr/bin/python3

from app import App
from store import DaoTelephone
from service import ServiceTelephone
from dc import TelephoneLine
import sys


PATH_TXT = "./db_telephone.txt"


def setting_app(path: str) -> App:
    """Настройка программы

    Args:
        path (str): путь до телефонной книги

    Returns:
        App: Объект приложения
    """
    dao_tel = DaoTelephone(path)
    service = ServiceTelephone(dao_tel)
    return App(service)


def main():
    app = setting_app(PATH_TXT)
    print(
        "Привет пользователь!\n" "Чтобы посмотреть доступные команды введите <помощь>"
    )
    while True:
        command = input("Введите команду: ").strip()
        match command:
            case "помощь":
                print(
                    "выход - выход из программы\n"
                    "всех - получить все телефоны\n"
                    "добавить - добавить телефон в книгу\n"
                    "изменить - редактировать телефон в книге\n"
                    "найти - найти телефон в книге\n"
                )
            case "выход":
                print("До свидания пользователь!")
                sys.exit(0)
            case "всех":
                app.get_all()
            case "добавить":
                app.add_phone()
            case "найти":
                app.search_phone()
            case "изменить":
                app.edit_phone()
            case _:
                print(
                    "Я не знаю такой команды\n" "Для просмотра команд введите <помощь>"
                )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nДо свидания пользователь!")
        sys.exit(0)
