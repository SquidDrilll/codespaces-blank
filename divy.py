customer = {}

while True:
    print("Menu")
    print("1. Show record")
    print("2. Add new Customer")
    print("3. Kill/Delete Customer")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Sort Record")
    print("7. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        if not customer:
            print("No customers found.")
        else:
            for key, value in customer.items():
                print(f"{key} : {value}") #(key, ":", value )

    elif ch == "2":
        name = input("Enter the customer name: ")
        details = input("Enter the customer ID: ")
        customer[name] = details

    elif ch == "3":
        name = input("Enter the customer to be deleted: ")
        if name in customer:
            del customer[name]
            print("Customer has been deleted")
        else:
            print("ERROR 404: Customer not found.")

    elif ch == "4":
        name = input("Enter the customer name to search: ")
        if name in customer:
            print(f"{name} : {customer[name]}") #(name, ":", customer[name])
        else:
            print("ERROR 404: Customer not found")

    elif ch == "5":
        name = input("Enter the customer name: ")
        if name in customer:
            details = input("Enter NEW ID: ")
            customer[name] = details
        else:
            print("ERROR 404: Customer not found")

    elif ch == "6":
        customer = dict(sorted(customer.values()))
        for value, key in customer:
            print(f"{key} : {value}")

    elif ch == "7":
        break

    else:
        print("Invalid choice")
    
#with this one yes
#everyone done?
#