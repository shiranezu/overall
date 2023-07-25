import random
class Order:
    def __init__(self, order_id, items, aname ):
        self.order_id = order_id
        self.items = items
        self.aname = aname
        self.order_status = 'pending'

class Order_fufillment_system:
    def __init__(self):
        self.new_order = []
        self.__ids = []

    def generate_order_id(self):
        id = random.randint(1, 100)
        if id in self.__ids:
            id = random.random(1, 100)
        return id


    def place_order(self, name, item) -> str:  
        order_id = self.generate_order_id()
        order = Order(order_id, name, item)
        self.new_order.append(order) 
        return order_id 

    
    def process_order(self, order_id: str) -> None:
        if order_id in self.new_order:
            order_id = self.new_order[order_id]
        self.order_status = 'processing'


    def ship_order(self, order_id: str) -> None:
        if order_id in self.new_order:
            order_id = self.new_order[order_id]
        self.order_status ='shipped'
            
    def deliver_order(self, order_id: str) -> None:
        if order_id in self.items:
            order_id = self.items[order_id]
            self.order_status = 'delivered'

    def get_order_status(self, order_id: str) -> str:
        if order_id in self.items:
            order= self.new_order[order_id]
            return order.status
        else:
            return ' Invalid ID, please try again'
        
users = Order_fufillment_system()
def main():
    while True:
        print('Select an option')
        print('1. place order')
        print('2. process order')
        print('3. ship order')
        print('4.deliver order')
        print('5. get order status')
        print()
        response = int(input(''))
        
        if response == 1:
            name = input('enter your name: ')
            item = input('What will you like to order: ')
            users.place_order(name, item)
            print(' order placed successfully')
        elif response == 2:
            if len(users.new_order) == 0:
                print('No user in the list')
            else:
                id = (input('enter your id: '))
                for user in users.new_order:
                    if user.order_id == id:
                        if user.order_status == 'Processing':
                            print('Order Already Processing')
                        else:
                            users.process_order(user)
                            print('Order Processing')
                        break
                else:
                    print('Could not find order to process')
        elif response == 3:
            if len(users.new_order) == 0:
                print('No user in the list')
            else:
                id = (input('enter your id: '))
                for user in users.new_order:
                    if user.order_id == id:
                        if user.order_status == 'Processing':
                            print('Order Already Processing')
                        else:
                            users.ship_order_order(user)
                            print('Order shipped successfully 😊')
                        break
                else:
                    print('sorry, but we could not find the order that you requested')
                    
        elif response == 4:
            if len(users.new_order) == 0:
                print('No user in the list')
            else:
                id = (input('enter your id: '))
                for user in users.new_order:
                    if user.order_id == id:
                        if user.order_status == 'Processing':
                            print('Order Already Processing')
                        else:
                            users.deliver_order(user)
                            print('Order will be delivered soon 😊.')
                        break
                else:
                    print('Order cannot be delivered')
        elif response == 5:
            name = (input('enter your name'))
            for user in users:
                if user.aname == name:

                    print(user.get_order_status())
                
main()