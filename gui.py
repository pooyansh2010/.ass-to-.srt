# created by pooyan
import PySimpleGUI as sg
import os.path
import convertor

file_list_column = [
    [
        sg.Text("Sub Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]
right_viewer_column = [
    [sg.Text("ass to srt:")],
    [sg.Text(size=(40, 5), key="-TOUT-")],
    [sg.Text(" ",size=(40, 3),key="-done-")],
    [sg.Text("po.sh1389@gmail.com",size=(40, 3),key="email")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(right_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            # and f.lower().endswith((".ass", ".srt"))
            and f.lower().endswith((".ass"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-done-"].update("loading ...")
            convertor.convert(filename) 
            window["-TOUT-"].update("save location : " + filename)
            window["-done-"].update(convertor.fileNameWithoutLocation(filename) + " \n "+ "------------ DONE ------------")

            print('------------ DONE ------------')

        except:
            pass

window.close()