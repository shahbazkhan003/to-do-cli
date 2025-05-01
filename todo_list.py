class TODO:
    def __init__(self):
        self.tasks = []
        
    def add_task(self):
        task_name = input("\nEnter the task name: ")
        self.tasks.append(task_name)
        print(f"Added Task '{task_name}' Successfully\n")
    def view_task(self):
        print("\n--View Task--")
        if not self.tasks:
            print("No Task Available")
        else:
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}. {task}\n")
    def update_task(self):
        updated_task_name = input("\nEnter the task name to update: ")
        if updated_task_name in self.tasks:
            new_task_name = input("Enter the new task name: ")
            ind = self.tasks.index(updated_task_name)
            self.tasks[ind] = new_task_name
            print(f"Updated '{new_task_name} Task Successfully\n")
        else:
            print(f"\nTask '{updated_task_name}' Not Found..")
    def delete_task(self):
        del_task = input("Enter the task name to delete: ")
        if del_task in self.tasks:
            self.tasks.remove(del_task)
            print(f"Delete '{del_task}' Task Successfully...\n")
        else:
                print(f"\nTask '{del_task}' Not Found..")  
    @staticmethod
    def show_menu():
        print("\n--Welcome TO-DO-LIST App--")
        print(" 1.Add Task \n 2.View Task \n 3.Update Task \n 4.Delete Task \n 5.Exit")  
    def run(self):
        print("--Welcome TO-DO-LIST App--")
        while True:
            print(" 1.Add Task \n 2.View Task \n 3.Update Task \n 4.Delete Task \n 5.Exit")
            choice = input("Enter your choice(1-5):")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting The App ... Goodbye!")
                break
            else:
                print("Invalid Choice")
if __name__ == "__main__":
    s1 = TODO()
    s1.show_menu()
    s1.run()