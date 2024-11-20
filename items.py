from connection.connection import ConnectionDB


class Item:
    def __init__(self, id: int, name: str, quantity: int, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    @staticmethod
    def log_stock_change(item_id, action, old_quantity, new_quantity):
        try:
            ConnectionDB.execute_query(f"""INSERT INTO logs (item_id, action, old_quantity, new_quantity)
        VALUES ({item_id}, {action}, {old_quantity}, {new_quantity});""").close()
            print("Logged successfully")
        except Exception as e:
            print("ERROR", e)

    def update_stock(self, change):
        old_quantity = self.quantity
        self.quantity += change
        action = 'Update Stock'
        self.log_stock_change(self.id, action, old_quantity, self.quantity)

    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


class PhysicalItem(Item):
    def __init__(self, id, name, quantity, price, weight, dimensions):
        super().__init__(id, name, quantity, price)
        self.weight = weight
        self.dimensions = dimensions

    def get_info(self):
        info = super().get_info()
        info.update({"weight": self.weight, "dimensions": self.dimensions})
        return info


class DigitalItem(Item):
    def __init__(self, id, name, quantity, price, file_size, download_link: str):
        super().__init__(id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def get_info(self):
        info = super().get_info()
        info.update({"file_size": self.file_size, "download_link": self.download_link})
        return info
