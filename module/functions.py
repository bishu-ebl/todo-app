# def get_todos():
#     with open('Files/todos.txt', 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
FILEPATH = "Files/todos.txt"

# def get_todos(filepath"):
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# def write_todos(filepath, file_arg):
def write_todos(file_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(file_arg)

# print(__name__)
#
# if __name__ == "__main__":
#     print("__name__ return __main__ when execute this function standalone!!")
#     print(get_todos())
