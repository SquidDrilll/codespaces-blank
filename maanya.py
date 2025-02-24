customers = {}
 
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
        if not customers:
            print("No records found.")
            break
        else:
            for key, value in customers.items():
                print(f"ID: {key}, Name: {value['name']}, Year: {value['year']}")
