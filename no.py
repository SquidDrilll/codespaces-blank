'''customer = {}

while True:
    print("Menu:")
    print("1. Show Record")
    print("2. Add New Customer")
    print("3. Delete Customer")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Sort Record")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        if not customer:
            print("No records found.")
        else:
            for key, value in customer.items():
                print(f"ID: {key}, Name: {value['name']}, Year: {value['year']}")
    
    elif choice == '2':
        new_customer = eval(input("Enter new customer details as a dictionary: "))
        customer.update(new_customer)
        print("Customer added.")
        
    elif choice == '3':
        customer_id = input("Enter Customer ID to delete: ")
        if customer_id in customer:
            del customer[customer_id]
            print("Customer deleted.")
        else:
            print("Customer ID not found.")
        
    elif choice == '4':
        customer_id = input("Enter Customer ID to search: ")
        if customer_id in customer:
            print(f"ID: {customer_id}, Name: {customer[customer_id]['name']}, Year: {customer[customer_id]['year']}")
            print("Customer found.")
        else:
            print("Customer ID not found.")
        
    elif choice == '5':
        customer_id = input("Enter Customer ID to update: ")
        if customer_id in customer:
            updated_info = eval(input("Enter updated details as a dictionary: "))
            customer[customer_id].update(updated_info)
            print("Customer updated.")
        else:
            print("Customer ID not found.")
        
    elif choice == '6':
        sorted_customers = dict(sorted(customer.items()))
        for key, value in sorted_customers.items():
            print(f"ID: {key}, Name: {value['name']}, Year: {value['year']}")
        
    elif choice == '7':
        break
        
    else:
        print("Invalid choice. Please try again.")


           
 2ND QUESTION HERE


my_list = []  # Start with an empty list

while True:
    print("List Operations Menu:")
    print("1. Create Empty List")
    print("2. Add Single Element")
    print("3. Add n no. of Elements")
    print("4. Search Element")
    print("5. Modify Element")
    print("6. Delete Element")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':  # Create Empty List
        my_list = []
        print("List cleared.")

    elif choice == '2':  # Add Single Element
        element = input("Enter element to add: ")
        my_list.append(element)

    elif choice == '3':  # Add n no. of Elements
        numelements = int(input("Enter number of elements to add: "))
        for in range(num_elements):
            element = input("Enter element: ")
            my_list.append(element)

    elif choice == '4':  # Search Element
        element = input("Enter element to search: ")
        if element in my_list:
            print("Element found at index:", my_list.index(element))
        else:
            print("Element not found.")

    elif choice == '5':  # Modify Element
        index = int(input("Enter index to modify: "))
        if 0 <= index < len(my_list):
            element = input("Enter new element: ")
            my_list[index] = element
        else:
            print("Invalid index.")

    elif choice == '6':  # Delete Element
        element = input("Enter element to delete: ")
        if element in my_list:
            my_list.remove(element)
        else:
            print("Element not found.")

    elif choice == '7':  # Exit
        break

    else:
        print("Invalid choice.")
        '''

customer = {}

while True:
    menu = "\nMenu:\n1. Show Record\n2. Add New Customer\n3. Delete Customer\n4. Search Record\n5. Update Record\n6. Sort Record\n7. Exit"
    print(menu)
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        if len(customer) == 0:
            print("No records found!")
        else:
            for id, details in customer.items():
                print("Customer ID:", id)
                print("Name:", details['Name'])
                print("Age:", details['Age'])
                print("Email:", details['Email'])
                print("--------")
                
    elif choice == "2":
        id = input("Enter Customer ID: ")
        if id in customer:
            print("Customer ID already exists.")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            email = input("Enter Email: ")
            customer[id] = {'Name': name, 'Age': age, 'Email': email}
            print("Customer added successfully!")

    elif choice == "3":
        id = input("Enter Customer ID to delete: ")
        if id in customer:
            del customer[id]
            print("Customer deleted successfully!")
        else:
            print("Customer ID not found.")

    elif choice == "4":
        id = input("Enter Customer ID to search: ")
        if id in customer:
            details = customer[id]
            print("Customer ID:", id)
            print("Name:", details['Name'])
            print("Age:", details['Age'])
            print("Email:", details['Email'])
        else:
            print("Customer ID not found.")
            
    elif choice == "5":
        id = input("Enter Customer ID to update: ")
        if id in customer:
            name = input("Enter new Name: ")
            age = input("Enter new Age: ")
            email = input("Enter new Email: ")
            customer[id] = {'Name': name, 'Age': age, 'Email': email}
            print("Customer record updated successfully!")
        else:
            print("Customer ID not found.")
            
    elif choice == "6":
        sorted_ids = sorted(customer.keys())
        if len(sorted_ids) > 0:
            for id in sorted_ids:
                details = customer[id]
                print("Customer ID:", id)
                print("Name:", details['Name'])
                print("Age:", details['Age'])
                print("Email:", details['Email'])
                print("--------")
        else:
            print("No records to sort.")

    elif choice == "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please enter a valid number between 1 and 7.")

        