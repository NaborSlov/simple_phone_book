from dataclasses import dataclass


@dataclass
class TelephoneLine:
    """
    Класс для записей из телефонной книги
    """
    last_name: str
    first_name: str
    middle_name: str
    organization: str
    phone_work: str
    phone_home: str

    def form_write(self) -> str:
        """Подготовка данных из объекта записи к, записи в телефонную книгу

        Returns:
            str: отформатированная строка
        """
        format_res = ":".join(
            [
                self.last_name,
                self.first_name,
                self.middle_name,
                self.organization,
                self.phone_work,
                self.phone_home,
            ]
        )

        return format_res + "\n"

    def form_print(self) -> str:
        """Подготовка данных из объекта записи к выводу в консоль

        Returns:
            str: отформатированная строка
        """
        return (
            "Ф.И.О. - {0} {1} {2}\n"
            "Организация - {3}\n"
            "Рабочий телефон - {4}\n"
            "Домашний телефон - {5}\n"
        ).format(
            self.last_name,
            self.first_name,
            self.middle_name,
            self.organization,
            self.phone_work,
            self.phone_home,
        )
