class CustomerManager:
    def __init__(self):
        self.customers = {}

    def showrecords(self):
        print(f"Customers: {self.customers}")

    def add_new(self, customer_id, name):
        self.customers[customer_id] = name
    
    def del_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} has been deleted.")
        else:
            print(f"Customer {customer_id} not found.")
    
    def search_customer(self, customer_id):
        if customer_id in self.customers:
            print(self.customers[customer_id])
        else:
            print(f"Customer {customer_id} not found.")

    def update_info(self, customer_id, newname):
        if customer_id in self.customers:
            self.customers[customer_id] = newname
            print("Record updated.")
        else:
            print(f"Customer {customer_id} not found.")

    def sort_records(self):
        self.customers = dict(sorted(self.customers.items()))

manager = CustomerManager()
    
manager.add_new(1, 'divy')
manager.add_new(4, 'squidgy')
manager.add_new(3, 'heroduckypookie')

manager.showrecords()
manager.sort_records()
manager.showrecords()
manager.search_customer(3)
#now it works like a default function in python
#cuz every function in python like sort() etc are indeed classes









    






























                                                                                                                                            