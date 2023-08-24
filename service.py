from dc import TelephoneLine
from store import DaoTelephone


class ServiceTelephone:
    def __init__(self, dao: DaoTelephone | None = None) -> None:
        self.dao = dao

    def get_all(self):
        phones = self.dao.read_phones()
        return phones

    def add_phone(self, data) -> None:
        item = TelephoneLine(**data)
        self.dao.add_phone(item)

    def edit_phone(self, phone: TelephoneLine, edit_data: dict) -> None:
        phones = list(self.dao.read_phones())

        for key, value in edit_data.items():
            phone = phones[phones.index(phone)]
            setattr(phone, key, value)

        self.dao.write_phones(phones)

    def search_phone(self, **kwargs):
        phones = self.dao.read_phones()
        for key, item in kwargs.items():
            phones = filter(lambda x: getattr(x, key) == item, phones)

        try:
            phone = next(phones)
        except StopIteration:
            return None
        else:
            return phone
