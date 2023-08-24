from dc import TelephoneLine


class DaoTelephone:
    def __init__(self, path: str) -> None:
        self.path = path

    def read_phones(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return map(self.split_line, f.readlines())

    @staticmethod
    def split_line(line: str) -> TelephoneLine:
        res = line.strip().split(":")
        return TelephoneLine(*res)

    def write_phones(self, items: list[TelephoneLine]) -> None:
        write_text = "".join((x.form_write() for x in items))
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(write_text)

    def add_phone(self, items: TelephoneLine) -> None:
        write_text = items.form_write()
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(write_text)
