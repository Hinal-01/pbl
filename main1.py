#code of gui.py

import PySimpleGUI as sg

sg.theme("Reddit")

layout = [[sg.Text("")], [sg.Text("Choose Source folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("Choose Destination folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("")], [sg.Button("Submit", size=(8, 1))]]

window = sg.Window("Python OS Project", layout, size=(600,200))
    
while True:
    event, values = window.read()

    if values[0] == '':
        print("Source Path can't be empty")
        continue

    if values[1] == '':
        print("Destination Path can't be empty")
        continue
    
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    
    elif event == "Submit":
        source=values[0]
        destination=values[1]
        break


# code of main.py

import os
import os.path
import shutil
import gui

def file_extension(filename):
    split_tup = os.path.splitext(filename)
    return split_tup[1]

def directory_exists(temp_dest):
    return os.path.isdir(temp_dest)

def create_directory(d, dir):
    path=os.path.join(d, dir)
    os.mkdir(path)

def file_exists(f):
    return os.path.exists(f)

def movefile(s, d):
    shutil.move(s, d)

source = gui.source
destination = gui.destination

source += '/'
destination += '/'

for filename in os.listdir(source):

    extension=(file_extension(filename))
    extension=extension[1:]

    if extension == '':
        continue

    temp = destination + extension

    if not(directory_exists(temp)):
        create_directory(destination, extension)

    s = source + filename
    d = destination + extension + '/' + filename

    if file_exists(d):
        print(filename, " already exists")
        continue

    movefile(s, d)

