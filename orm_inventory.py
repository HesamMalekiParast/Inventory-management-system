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
            type VARCHAR(50) NOT NULL, -- 'Physical' or 'Digital'
            weight DECIMAL(10, 2), -- NULL for DigitalItem
            dimensions VARCHAR(255), -- NULL for DigitalItem
            file_size DECIMAL(10, 2), -- NULL for PhysicalItem
            download_link TEXT, -- NULL for PhysicalItem
            date_added TIMESTAMP DEFAULT NOW());""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_item_physical(item):
        try:
            ConnectionDB.execute_query(f"""
            INSERT INTO inventory (name, quantity, price, type, weight, dimensions)
            VALUES ({item.name}, {item.quantity}, {item.price},{"digital"},{item.weight}, {item.dimensions});
            """)
            ConnectionDB.close_db()
            print(f"Item inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_item_digital(item):
        try:
            ConnectionDB.execute_query(f"""
            INSERT INTO inventory (name, quantity, price, type, file_size, download_link)
            VALUES ({item.name}, {item.quantity}, {item.price}, {"Physical"}, {item.file_size}, {item.download_link});
            """)
            ConnectionDB.close_db()
            print(f"Item inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def update_stock(id, new_quantity):
        try:
            ConnectionDB.execute_query(f"""UPDATE inventory SET quantity = {id} WHERE id = {new_quantity};""")
            ConnectionDB.close_db()
            print(f"Updated ({id}) stock with new quantity ({new_quantity}) successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_all_items():
        try:
            ConnectionDB.execute_query(f"""SELECT * FROM inventory;""")
            ConnectionDB.close_fetch_all()
            print("Retrieve all items successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def find_low_stock(threshold):
        try:
            ConnectionDB.execute_query(f"""SELECT * FROM inventory WHERE quantity < {threshold};""")
            ConnectionDB.close_fetch_all()
            print(f"Found stock lower than {threshold} successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def total_stock_value():
        try:
            ConnectionDB.execute_query(f"""SELECT SUM(quantity * price) AS total_value FROM inventory;""")
            ConnectionDB.close_fetch_all()
            print("Found total stock value successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def find_by_type(item_type):
        try:
            ConnectionDB.execute_query(f"""SELECT * FROM inventory WHERE type = {item_type};""")
            ConnectionDB.close_fetch_all()
            print(f"Items type ({item_type}) found successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def average_price():
        try:
            ConnectionDB.execute_query(f"""SELECT AVG(price) AS average_price FROM inventory;""")
            ConnectionDB.close_fetch_one()
            print("Found total stock value successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def delete_item_by_id(id):
        try:
            ConnectionDB.execute_query(f"""DELETE FROM inventory WHERE id = {id};""")
            ConnectionDB.close_db()
            print(f"({id}) Item deleted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def update_price(id, new_price):
        try:
            ConnectionDB.execute_query(f"""UPDATE inventory SET price = {id} WHERE id = {new_price};""")
            ConnectionDB.close_db()
            print(f"Item ({id}) price updated with new price ({new_price}) successfully ")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_oldest_items():
        try:
            ConnectionDB.execute_query(f"""SELECT * FROM inventory ORDER BY date_added ASC LIMIT 10;""")
            ConnectionDB.close_fetch_all()
            print("Found total stock value successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def retrieve_all_logs():
        try:
            ConnectionDB.execute_query(f"""SELECT * FROM logs;""")
            ConnectionDB.close_fetch_all()
            print("Found total stock value successfully")
        except Exception as e:
            print("ERROR", e)


if __name__ == "__main__":
    Inventory.create_table()
    physical_item = PhysicalItem(1, "Table", 5, 150.00, 20.5, "120x60x75")
    digital_item = DigitalItem(2, "Ebook", 50, 15.99, 2.5, "http://example.com/ebook")

    Inventory.insert_item_physical(physical_item)
    Inventory.insert_item_digital(digital_item)

    physical_item.update_stock(10)
    digital_item.update_stock(-5)

    # Fetch and display logs
    print(Inventory.retrieve_all_logs())
