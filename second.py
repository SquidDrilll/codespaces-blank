#write a menu driven program to perform the following operations in list:
#1. Create Empty List
#2. Add Single Element
#3. Add n no. of Elements
#4. Search Element
#5. Modify Element
#6. Delete Element
#7. Exit

my_list = []

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
        print("List created.")
        
    elif choice == '2':  # Add Single Element
        element = input("Enter element to add: ")
        my_list.append(element)

    elif choice == '3':  # Add n no. of Elements
        numelements = int(input("Enter number of elements to add: "))
        for i in range(num_elements):
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

    elif choice == '6':  # Delete Element
        element = input("Enter element to delete: ")
        if element in my_list:
            my_list.remove(element)


    elif choice == '7':  # Exit
        break
    
    else:
        print("Invalid choice.")
        