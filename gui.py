from module import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do Desktop Apps',layout=[[label], [input_box,add_button]])
# window = sg.Window('My To-Do Desktop Apps',layout=[[label, input_box]])
window.read()
window.close()