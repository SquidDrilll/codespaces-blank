#are you here?

customers = {}
 
while True:
    
    print("1. Show Record")
    print("2. Add New Customer")
    print("3. Delete Customer")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Sort Record")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if not customers:
            print("No records found.")
        else:
            for i in customers:
                print(f'ID: {i}, Name: {customers[i]}')

    if choice == '2':
        new_customer = input('Enter the customer id: ')
        customers[new_customer] = input('Enter the customer name: ')
        print('Customer added.')

    elif choice == '3':
        delete_customer = input('Enter the customer id: ')
        if delete_customer in customers:
            del customers[delete_customer]
            print('Customer deleted.')
        else:
            print('Customer not found.')
            
    elif choice == '4':
        search_customer = input('Enter the customer id: ')
        if search_customer in customers:
            print(f'ID: {search_customer}, Name: {customers[search_customer]}')
        else:
            print('Customer not found.')


    elif choice == '5':
        #asking for the customer id(existing customer) to update its name
        update_customer = input('Enter the customer id: ')
        #checking if the customer id exists
        if update_customer in customers:
            #asking for the new name
            update_name = input('Enter the new name: ')
            #updating the customer name
            customers[update_customer] = update_name
            print('Customer updated.')
        else:
            print('Customer not found.')

    elif choice == '6':
        #sorting the customers by id
        customers = dict(sorted(customers.items()))
        print('Customers sorted by id.')
        
    elif choice == '7':
        break
    
    else:
        print("Invalid choice.")

#i am done guys. wbu 
#lmk when done ill commit changes and give you url wdym
