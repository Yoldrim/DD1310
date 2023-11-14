class PackingList:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.items = []

    def to_db_string(self):
        arr = []
        for item in self.items:
            arr.append(item.to_db_string())
        return f'{self.name};{self.date}\n{";".join(arr)}'
