class PackingItem:
    def __init__(self, name, packed=False):
        self.name = name
        self.packed = packed


    def to_db_string(self):
        return f'{"+" if self.packed else ""}{self.name}'