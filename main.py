# todos = []

while True:
    user_action = input("Type add, show, edit, delete or exit:")
    user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a To do:") + "\n"

            # file = open("Files/todos.txt", 'r')
            # todos = file.readlines()
            # file.close()

            # Alternate way to open file by using WITH CONTEXT manager
            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open("Files/todos.txt", 'w')
            # file.writelines(todos)
            # file.close()

            # Alternate way to open file by using WITH CONTEXT manager
            with open("Files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show':
            with open("Files/todos.txt", 'r') as file:
                todos = file.readlines()

            # ist method to remove \n new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            # for index, item in enumerate(new_todos):
            #     row = f"{index + 1}-{item}"
            #     print(row)

            # 2nd method Using List Comprehensions-Use to modify item in list

            # new_todos = [item.strip("\n") for item in todos]
            #
            # for index, item in enumerate(new_todos):
            #     row = f"{index + 1}-{item}"
            #     print(row)

            # 3rd method
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Enter the todo item to Edit:"))
            number = number - 1

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Type new todo item:")
            todos[number]=new_todo + "\n"

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'delete':
            number = int(input("Enter item to delete:"))

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            index=number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"The item {todo_to_remove} is remove from the list"
            print(message)

        case 'exit':
            break

print("Bye!!!")