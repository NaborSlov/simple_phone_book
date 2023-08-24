import re
from typing import Any
from dc import TelephoneLine
from service import ServiceTelephone


class App:
    REG_TEXT = re.compile(r"^[А-Яа-я]+$|^[A-Za-z]+$")
    REG_PHONE = re.compile(r"^\+?[78]?\d{10}$")
    INPUT_DATA = {
        "last_name": "фамилию",
        "first_name": "имя",
        "middle_name": "отчество",
        "organization": "название организации",
        "phone_work": "рабочий телефон",
        "phone_home": "домашний телефон",
    }

    def __init__(self, service: ServiceTelephone) -> None:
        self.service = service

    def get_all(self):
        print_text = ""
        for item in self.service.get_all():
            print_text += "=" * 40 + "\n"
            print_text += item.form_print()

        print(print_text or "В базе данных нет телефонов")

    def add_phone(self):
        data, err = self.input_data()

        if err:
            return

        self.service.add_phone(data)

    def search_phone(self):
        print(
            "Введите данные для поиска, для пропуска введите <далее>\n"
            "для немедленного поиска введите <все>"
        )
        search_data = self.partial_data()
        phone = self.service.search_phone(**search_data)

        print(
            "=" * 20 + "\n" + phone.form_print() if phone else "Пользователь не найден"
        )

    def edit_phone(self):
        print(
            "Введите данные для поиска записи которую вы хотите изменить,\n"
            "для пропуска характеристики введите <далее>\n"
            "для немедленного поиска введите <все>"
        )
        search_data = self.partial_data()
        phone = self.service.search_phone(**search_data)

        if not phone:
            print("Такого пользователя нет в книге")
            return

        print(
            "Найденная запись\n" + "=" * 20 + "\n" + phone.form_print() + "\n"
            "Введите данные которые вы хотите изменить, "
            "для пропуска характеристики введите <далее>\n"
            "для изменения с имеющемся характеристиками введите <все>:"
        )

        partial_data = self.partial_data()
        self.service.edit_phone(phone, partial_data)

    def input_data(self) -> tuple[dict, int]:
        data_input = {}

        for key, value in self.INPUT_DATA.items():
            while True:
                input_data = input(f"Введите {value}:\n")

                if input_data == "выход":
                    return data_input, 1

                if key in ["phone_work", "phone_home"]:
                    if not self.REG_PHONE.match(input_data):
                        print(
                            "Телефон должен быть в формате:\n"
                            "8xxxxxxxxxx\n"
                            "+7xxxxxxxxxx\n"
                            "xxxxxxxxxx\n"
                        )
                        continue
                else:
                    if not self.REG_TEXT.match(input_data):
                        print("Не должно быть цифр и спецзнаков")
                        continue

                data_input[key] = input_data
                break

        return data_input, 0

    def partial_data(self):
        data_search = {}

        for key, value in self.INPUT_DATA.items():
            while True:
                input_data = input(f"Введите {value}:\n")

                if input_data == "далее":
                    break

                if input_data == "все":
                    return data_search

                if key in ["phone_work", "phone_home"]:
                    if not self.REG_PHONE.match(input_data):
                        print(
                            "Телефон должен быть в формате:\n"
                            "8xxxxxxxxxx\n"
                            "+7xxxxxxxxxx\n"
                            "xxxxxxxxxx\n"
                        )
                        continue
                else:
                    if not self.REG_TEXT.match(input_data):
                        print("Не должно быть цифр и спецзнаков")
                        continue

                data_search[key] = input_data
                break

        return data_search
