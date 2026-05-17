from module import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text(key="Clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

# Alternate way
# layout=[[label], [input_box,add_button],[list_box, edit_button]]

# Dynamic Layout
# button_level = ["Close", "Apply"]
# layout = []
#
# for bl in button_level:
#     layout.append([sg.Button(bl)])
#[[sg.Button("Close")], [sg.Button("Apply")]]

window = sg.Window('My To-Do Desktop Apps',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]],
                   # layout=layout,
                   font=('Helvetica',15))
# window = sg.Window('My To-Do Desktop Apps',layout=[[label, input_box]])
while True:
    event, values = window.read(timeout=200)
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    window["Clock"].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                # print("Please select an item First!")
                sg.popup("Please select an item first!", font=("Helvetica",12))
        case "Delete":
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first to delete!", font=("Helvetica", 12))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
            # exit() --Nothing beneath will be executed.

# print("Bye")
window.close()