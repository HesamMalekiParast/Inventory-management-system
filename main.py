class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class PhysicalItem(Item):
    def __init__(self, name, quantity, price, weight, dimensions):
        super().__init__(name, quantity, price)
        self.weight = weight
        self.dimensions = dimensions

    def update_stock(self):
        pass

    def get_info(self):
        pass


class DigitalItem(Item):
    def __init__(self, name, quantity, price, file_size, download_link):
        super().__init__(name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def update_stock(self):
        pass

    def get_info(self):
        pass
