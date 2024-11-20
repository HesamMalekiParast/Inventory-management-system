from connection.connection import ConnectionDB
from items import PhysicalItem, DigitalItem


class Inventory:

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE IF NOT EXISTS inventory (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            type VARCHAR(50) NOT NULL,
            weight DECIMAL(10, 2),
            dimensions VARCHAR(255),
            file_size DECIMAL(10, 2),
            download_link VARCHAR(255),
            date_added TIMESTAMP DEFAULT NOW());""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_item_physical(item):
        try:
            physical = 'Physical'
            ConnectionDB.execute_query(f"""
            INSERT INTO inventory (id, name, quantity, price, type, weight, dimensions)
            VALUES ({item.id}, {item.name}, {item.quantity}, {item.price}, {physical}, {item.weight}, {item.dimensions});
            """).close()
            print(f"Item inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_item_digital(item):
        try:
            digital = 'Digital'
            ConnectionDB.execute_query(f"""INSERT INTO inventory (id, name, quantity, price, type, file_size, download_link)
            VALUES ({item.id}, {item.name}, {item.quantity}, {item.price}, {digital}, {item.file_size}, {item.download_link});
            """).close()
            print(f"Item inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def update_stock(id, new_quantity):
        try:
            ConnectionDB.execute_query(f"""UPDATE inventory SET quantity = {id} WHERE id = {new_quantity};""").close()
            print(f"Updated ({id}) stock with new quantity ({new_quantity}) successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_all_items():
        try:
            return ConnectionDB.execute_query(f"""SELECT * FROM inventory;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def find_low_stock(threshold):
        try:
            return ConnectionDB.execute_query(f"""SELECT * FROM inventory WHERE quantity < {threshold};""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def total_stock_value():
        try:
            return ConnectionDB.execute_query(f"""SELECT SUM(quantity * price) AS total_value FROM inventory;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def find_by_type(item_type):
        try:
            return ConnectionDB.execute_query(f"""SELECT * FROM inventory WHERE type = {item_type};""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def average_price():
        try:
            return ConnectionDB.execute_query(f"""SELECT AVG(price) AS average_price FROM inventory;""").fetchone()[0]
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def delete_item_by_id(id):
        try:
            ConnectionDB.execute_query(f"""DELETE FROM inventory WHERE id = {id};""").close()
            print(f"({id}) Item deleted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def update_price(id, new_price):
        try:
            ConnectionDB.execute_query(f"""UPDATE inventory SET price = {id} WHERE id = {new_price};""").close()
            print(f"Item ({id}) price updated with new price ({new_price}) successfully ")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_oldest_items():
        try:
            return ConnectionDB.execute_query(f"""SELECT * FROM inventory ORDER BY date_added ASC LIMIT 10;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_all_logs():
        try:
            return ConnectionDB.execute_query(f"""SELECT * FROM logs;""").fetchall()
        except Exception as e:
            print("ERROR", e)


if __name__ == "__main__":
    Inventory.create_table()
    physical_item = PhysicalItem(1, 'Table', 5, 150.00, 20.5, '120x60x75')
    digital_item = DigitalItem(2, 'Ebook', 50, 15.99, 2.5, 'https://example.com/ebook')

    Inventory.insert_item_physical(physical_item)
    Inventory.insert_item_digital(digital_item)

    # physical_item.update_stock(10)
    # digital_item.update_stock(-5)

    print(Inventory.retrieve_all_logs())
