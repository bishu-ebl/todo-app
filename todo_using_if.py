while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action.strip()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('Files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("Files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open("Files/todos.txt", 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Type new todo item:")
            todos[number] = new_todo + "\n"

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("You enter an invalid command!")
            continue

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])

            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"The item {todo_to_remove} is remove from the list"
            print(message)
        except IndexError:
            print("There is no item in this list with this number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("You type an invalid command!")

print('Bye!!!')


