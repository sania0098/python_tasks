def write_data():
    with open("std_data.txt",'w') as file:
        entry_data=input("Enter the name :")
        file.write(entry_data + '\n')
        print("data saved successfuly")

def read_data():
    with open("std_data.txt",'r') as file:

        data=file.read()
        return data


while True:
    print("Choose an option:")
    print("1. Write data to file")
    print("2. Read data from file")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        write_data()
    elif choice == '2':
        data = read_data()
        print("Data in file:")
        print(data)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")