customer = {}

while True: 
    print("Menu: ")
    print("1. Show Record")
    print("2. Add New Customer")
    print("3. Delete Customer:")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Sort Record")
    print("7. Exit")

    ch = int(input("Enter Your Choice "))

    if ch == 1:
        if not customer:
            print("No Record Found")
        else:
            for i in customer:
                print("ID: ",i, "Name: ", customer[i] ) 

    elif ch == 2:
        new_cust =  input("Enter Customer ID: ")
        customer[new_cust] = input("Enter Customer Name: ")
        print("Customer Added")
    
    elif ch == 3:
        del_cust = input("Enter Customer ID: ")
        if  del_cust in customer:
            del customer[del_cust]
            print("Customer Deleted")
        else:
            print("Customer Not Found")
            
    elif ch == 4:
        search_cust = input("Enter Customer ID")
        if search_cust in customer:
            print("ID: ",search_cust , "Name: ", customer[search_cust])
        else:
            print("Customer Not Found")

    elif ch == 5:
        update_cust = input("Enter Customer ID")
        if update_cust in customer:
            customer[update_cust] = input("Enter New Customer Name")
            print("Customer Updated")
        else:
            print("Customer Not Found")

    elif ch == 6:
        customer = sorted(customer.items())
        customer = dict(customer) 
        m
    elif ch == 7:
        break
    else:
        print("Invalid Choice")

