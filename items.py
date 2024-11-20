class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

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

    # def update_stock(self, change):
    #     old_quantity = self.quantity
    #     self.quantity += change
    #     self.log_stock_change(self.id, 'Update Stock', old_quantity, self.quantity)


class DigitalItem(Item):
    def __init__(self, id, name, quantity, price, file_size, download_link: str):
        super().__init__(id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def get_info(self):
        info = super().get_info()
        info.update({"file_size": self.file_size, "download_link": self.download_link})
        return info

    # def update_stock(self, change):
    #     old_quantity = self.quantity
    #     self.quantity += change
    #     self.log_stock_change(self.id, 'Update Stock', old_quantity, self.quantity)
