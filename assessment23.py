import argparse
import mysql.connector as sql
import datetime

class Error(Exception):
    pass

class Product:
    def __init__(self, productID, name, category, price, stock_quantity):
        self.productID = productID
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity


class Customer:
    # def __init__(self,) -> None:
    #     self.db = online_shopping()
    def __init__(self, customerID, name, Email, Shipping_address):
        self.customerID = customerID
        self.name = name
        self.Email = Email
        self.Shipping_address = Shipping_address

class Order:
    def __init__(self, orderID, order_date, customerID, total_amount):
        self.orderID = orderID
        self.order_date = order_date
        self.customerID = customerID
        self.total_amount = total_amount

class Online_shopping:
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

    def display_order_history(self, order_id):
        self.__cursor.execute(f'SELECT * FROM {self.ordersT} WHERE order_id = {order_id}')
        return self.__cursor.fetchall()
    
    def close(self):
        self.__db.close()




def main():
    users = Online_shopping()

    while True:
        print("""Welcome to SuperMart - Your Online Shopping Destination!

1. Browse products
2. Add a product to cart
3. View cart
4. Place an order
5. View order history
6. Register as a new customer
7. Update customer information
8. Exit"""
)
        choice = input("Please enter your choice: ")

        if choice == '1':
            print("""--- Available Products ---
Product ID: 1 | Name: Laptop | Category: Electronics | Price: $800.00 | Stock Quantity: 10
Product ID: 2 | Name: T-shirt | Category: Clothing | Price: $20.00 | Stock Quantity: 50
Product ID: 3 | Name: Book | Category: Books | Price: $15.00 | Stock Quantity: 100""")
        
        elif choice == "2":
            product = (input("Enter product name: "))
                
                # def add_new_product(self, product):
            for _product in users.add_product():
                if _product[1] == product.name:
                    raise Error
            else:
                users.add_product(product)

        elif choice == "3":
                return users.display_product()
        
        elif choice == "4":
            order = (input('enter your order: '))
            for _order in users.new_order():
                if _order[0] == order.orderID:
                    raise Error
            else:
                return users.new_order()
            
        elif choice == '5':
            for _order in users.new_order():
                if _order[2] == order.customerID:
                    raise Error
            else:
                return users.display_order_history()
            
        elif choice == '6':
            customer = (input('Enter your name: '))
            for _customer in users.add_customer():
                if _customer[1] == customer.name:
                    raise Error
            else:
                users.add_customer(customer)

        elif choice == '7':
            for _customer in users.add_product():
                if _customer[1] == customer.name:
                    raise Error
            else:
                users.update_product(customer)

        elif choice == '8':
            exit()

main()