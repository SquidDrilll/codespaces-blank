'''
Q.2
Write a menu driven program to perform the following operations in list:
1. Create Empty List
2. Add Single Elements
3. Add n no. of Elements
4. Search Element
5. Modify Element
6. Delete Element
7. Exit
'''


while True:
    print("List Operation Menu ")
    print()
    print("1. Create Empty List")
    print('2. Add Single Elements')
    print("3. Add n no. of Elements")
    print("4. Search Element")
    print("5. Modify Element")
    print("6. Delete Element")
    print("7. Exit")

    ch = int(input("Enter the Choice: "))

    if ch == 1:
        lst = []
        print("list Created")
    
    if ch == 2:
        element=input("Enter The Element: ")
        lst
