import argparse
import mysql.connector as sql
import datetime

class online_shopping:
    def __init__(self) -> None:
        self.__db = sql.Connect(
            host = 'localhost',
            user = 'root',
            password = 'aoKi2006!', 
            database = 'online_shopping',
        )
        self.productT = 'Product'
        self.customerT = 'customer'
        self.ordersT = 'orders'
        self.order_itemT = 'order_item'
        self.__cursor = self.__db.cursor()


    def add_product(self, product):
        self.__cursor.execute(f'INSERT INTO {self.productT} (Name, Category, Price, stock_quantity) VALUES (%s, %s, %s, %s)', (product.name, product.category, product.price, product.stock_quantity))      
        self.__db.commit()

    def remove_product(self, product):
        self.__cursor.execute(f'DROP FROM {self.productT} (Name, Category, Price, stock_quantity) WHERE VALUES (%s, %s, %s, %s)', (product.name, product.category, product.price, product.stock_quantity))      
        self.__db.commit()
    
    def update_product(self, id, new_price, new_stock_quantity):
        self.__cursor.execute(f'UPDATE {self.productT} SET price = "{new_price}", stock_quantity = "{new_stock_quantity}" WHERE productID = {id}"')
        self.__db.commit()

    def display_product(self):
        self.__cursor.execute(f'SELECT * FROM {self.presentT}')
        return self.__cursor.fetchall()
    
    def add_customer(self, customer):
        self.__cursor.execute(f'INSERT INTO {self.customerT} (Name, Email, Shipping_address) VALUES (%s, %s, %s)', (customer.Name, customer.Email, customer.Shipping_address))      
        self.__db.commit()

    def update_customer(self, id, new_email, new_address):
        self.__cursor.execute(f'UPDATE {self.customerT} SET Email = "{new_email}", Shipping_address = "{new_address}" WHERE customerID = {id}"')
        self.__db.commit()

    def display_customers(self):
        self.__cursor.execute(f'SELECT * FROM {self.customerT}')
        return self.__cursor.fetchall()
    

    def new_order(self, order):
        self.__cursor.execute(f'INSERT INTO {self.ordersT} (customerID, total_amount) VALUES (%s, %s)', (order.customerID, order.total_amount))      
        self.__db.commit()

    def display_order__history(self, order_id):
        self.__cursor.execute(f'SELECT * FROM {self.ordersT} WHERE order_id = {order_id}')
        return self.__cursor.fetchall()
    

    