# from module.functions import get_todos,write_todos
from module import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action.strip()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]

        # todos = get_todos()
        #todos = get_todos("Files/todos.txt")
        todos = functions.get_todos()

        todos.append(todo + '\n')

        # with open("Files/todos.txt", 'w') as file:
        #     file.writelines(todos)

        # write_todos("Files/todos.txt",todos)
        functions.write_todos(todos)

    elif user_action.startswith('show'):

        # todos = get_todos()
        # todos = get_todos("Files/todos.txt")
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            # todos = get_todos()
            # todos = get_todos("Files/todos.txt")
            todos = functions.get_todos()

            new_todo = input("Type new todo item:")
            todos[number] = new_todo + "\n"

            # with open("Files/todos.txt", 'w') as file:
            #     file.writelines(todos)

            # write_todos("Files/todos.txt",todos)
            functions.write_todos(todos)
        except ValueError:
            print("You enter an invalid command!")
            continue

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])

            # todos = get_todos()
            # todos = get_todos("Files/todos.txt")
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # with open("Files/todos.txt", 'w') as file:
            #     file.writelines(todos)

            #write_todos(filepath="Files/todos.txt", file_arg=todos)
            # write_todos("Files/todos.txt",todos)
            functions.write_todos(todos)

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


