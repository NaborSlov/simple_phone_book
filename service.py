from dc import TelephoneLine
from store import DaoTelephone


class ServiceTelephone:
    def __init__(self, dao: DaoTelephone | None = None) -> None:
        self.dao = dao

    def get_all(self) -> map:
        """Получение всех записей из телефонной книги

        Returns:
            map: итератор с объектами из телефонной книги TelephoneLine
        """
        phones = self.dao.read_phones()
        return phones

    def add_phone(self, data: dict) -> None:
        """Добавление новой записи в телефонную книгу

        Args:
            data (dict): словарь с данными новой записи
        """
        item = TelephoneLine(**data)
        self.dao.add_phone(item)

    def edit_phone(self, phone: TelephoneLine, edit_data: dict) -> None:
        """Изменение записи из телефонной книги

        Args:
            phone (TelephoneLine): запись которая будет изменена
            edit_data (dict): данные которые будут изменены
        """
        phones = list(self.dao.read_phones())

        for key, value in edit_data.items():
            phone = phones[phones.index(phone)]
            setattr(phone, key, value)

        self.dao.write_phones(phones)

    def search_phone(self, **kwargs):
        """Поиск телефонной записи по заданным данным

        Returns:
            _type_: поля по которым будет проводиться поиск
        """
        phones = self.dao.read_phones()
        for key, item in kwargs.items():
            phones = filter(lambda x: getattr(x, key).lower() == item.lower(), phones)

        try:
            phone = next(phones)
        except StopIteration:
            return None
        else:
            return phone
