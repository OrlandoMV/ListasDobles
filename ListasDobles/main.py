from doublelist import DoubleList
from node import Node

class Main:
    def __init__(self):
        self.MyList = DoubleList()

    def run(self):
        while True:
            print("\n===== MENU DOUBLE-LINKED LIST =====")
            print("1. Add")
            print("2. Remove")
            print("3. Show")
            print("4. ReverseShow")
            print("5. Count")
            print("6. Clear")
            print("7. Exit")

            option = input("Select an option: ")

            if option == "1":
                self.AddData()
            elif option == "2":
                self.RemoveData()
            elif option == "3":
                self.ShowData()
            elif option == "4":
                self.ReverseShowData()
            elif option == "5":
                self.btn_count_click()
            elif option == "6":
                self.ClearList()
            elif option == "7":
                print("===================================.")
                print("Completed program.")
                break
            else:
                print("===================================.")
                print("Invalid option.")

    def AddData(self):
        print("===================================.")
        txtData = input("Enter a number: ")
        if txtData == "":
            print("===================================.")
            print("You must enter a number.")
            return

        try:
            data = int(txtData)
        except ValueError:
            print("===================================.")
            print("Invalid entry, enter an integer.")
            return

        if self.MyList.exists(data):
            print("===================================.")
            print("The data already exists in the list.")
            return

        n = Node(data)
        self.MyList.add(n)
        print("===================================.")
        print("Successfully added.")

    def RemoveData(self):
        print("===================================.")
        txtData = input("Enter the number to delete: ")
        if txtData == "":
            print("===================================.")
            print("You must enter a number.")
            return

        try:
            data = int(txtData)
        except ValueError:
            print("===================================.")
            print("Invalid entry, enter an integer.")
            return

        if not self.MyList.exists(data):
            print("===================================.")
            print("Data does not exist in list.")
            return

        self.MyList.remove(data)
        print("===================================.")
        print("Data successfully removed.")

    def ShowData(self):
        datas = self.MyList.show()
        print("===================================.")
        print("\nList content:")
        print(datas)

    def ReverseShowData(self):
        datas = self.MyList.reverse_show()
        print("===================================.")
        print("\nContents of the list in reverse:")
        print(datas)

    def btn_count_click(self):
        count = self.MyList.count()
        print("===================================.")
        print(f"The list contains {count} elements.")

    def ClearList(self):
        self.MyList.clear()
        print("===================================.")
        print("List cleaned correctly.")

if __name__ == "__main__":
    app = Main()
    app.run()
