# File name where tasks are stored
my_task = "list.txt"

# Reads List
def read_list():
    try:
        with open(my_task, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Write list
def write_list(my_list):
    with open(my_task, "w") as f:
        f.writelines(f"{item}\n" for item in my_list)

# Adds task
def add_task(task):
    my_list = read_list()
    my_list.append(task)
    write_list(my_list)

# Removes task
def remove_task(index):
    my_list = read_list()
    if 0 <= index <= len(my_list):  # Check if index is within valid range
        del my_list[index]  # Adjusted to use 0-based index
        write_list(my_list)
    else:
        print("Invalid index.")

# Main function
def main():
    print("Welcome to list manager!!")

    while True:
        print("\nMenu:")
        print("Type 'read' to read your task list")
        print("Type 'add' to add any task in your list")
        print("Type 'remove' to remove any task from your list")
        print("Type 'exit' to leave the list manager")

        command = input("Enter your command:")

        if command == "read":
            my_list = read_list()
            if not my_list:
                print("Task list is empty.")
            else:
                for index, item in enumerate(my_list):
                    print(f"{index+1}. {item}")

        elif command == "add":
            task = input("Enter your task:")
            add_task(task)
            print("Task added successfully!!")

        elif command == "remove":
            try:
                index = int(input("Enter the index of the task you want to remove:"))
                remove_task(index)
            except ValueError:
                print("Please enter a valid index.")

        elif command == "exit":
            print("Thank you for using list manager!!")
            break
        else:
            print("Please have a valid command...")

if __name__ == "__main__":
    main()
