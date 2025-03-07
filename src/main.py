class ListManager:
    def __init__(self):
        self.myList = [x for x in range(1, 11)]

    def search_item(self, item):
        return f"The item {item} was {'found' if item in self.myList else 'not found'} in the list."

    def remove_item(self, position):
        try:
            removed_item = self.myList.pop(position)
            return f"The item {removed_item} was removed from the list."
        except IndexError:
            return "Invalid index! Please try again with a valid index."

    def replace_element(self, position, new_value):
        try:
            self.myList[position] = new_value
            return f"Element at position {position} has been replaced with {new_value}."
        except IndexError:
            return "Invalid index! Please try again with a valid index."

    def check_empty(self):
        return "The list is empty." if not self.myList else "The list is not empty."

    def insert_element(self, position, new_value):
        try:
            self.myList.insert(position, new_value)
            return f"Item {new_value} has been inserted at position {position}."
        except IndexError:
            return "Invalid index! Please try again with a valid index."

    def return_size(self):
        return f"The size of the list is {len(self.myList)}."

    def display_list(self):
        return f"Current list: {self.myList}"


def main():
    manager = ListManager()
    
    while True:
        print("\nOptions:")
        print("1. Search item")
        print("2. Remove item")
        print("3. Replace element")
        print("4. Insert element")
        print("5. Check if list is empty")
        print("6. Get list size")
        print("7. Display list")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = int(input("Enter item to search: "))
            print(manager.search_item(item))
        elif choice == "2":
            position = int(input("Enter position to remove: "))
            print(manager.remove_item(position))
        elif choice == "3":
            position = int(input("Enter position to replace: "))
            new_value = int(input("Enter new value: "))
            print(manager.replace_element(position, new_value))
        elif choice == "4":
            position = int(input("Enter position to insert: "))
            new_value = int(input("Enter value to insert: "))
            print(manager.insert_element(position, new_value))
        elif choice == "5":
            print(manager.check_empty())
        elif choice == "6":
            print(manager.return_size())
        elif choice == "7":
            print(manager.display_list())
        elif choice == "8":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()