from cgitb import text
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import re
from turtle import color

IF = 'if'
PRINT = 'print'

window = Tk()
window.title('Felinus IDE')

gpath = ''

def runMyCode():
    global gpath
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Please save the file first")
        msg.pack()
        return
    command = f'python {gpath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.delete('1.0',END)
    output.insert('1.0',outputResult)
    output.insert('1.0',error)
     

def openMyFile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        
        textEditor.insert('1.0', code)
    
        update()
        global gpath
        gpath = path

def saveMyFileAs():
    global gpath
    if gpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = gpath    
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        
        file.write(code)
        update()



textEditor = Text(height=20,width=500)
textEditor.config(bg='#1e1e26', fg='#d2ded1', insertbackground='white', foreground='white', font=('Fira Code','15'))
textEditor.pack()


output = Text(height=8,width=500, font=('Fira Code','16'))
output.config(bg='#1e1e26', fg='#1dd604')
output.pack()
 
menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command = openMyFile)
fileBar.add_command(label='Save', command = saveMyFileAs)
fileBar.add_command(label='SaveAs', command = saveMyFileAs)
fileBar.add_command(label='Exit', command = exit)
menuBar.add_cascade(label='File', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command = runMyCode)
menuBar.add_cascade(label='Run', menu = runBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Update', command =update)
menuBar.add_cascade(label='Update', menu = runBar)

window.config(menu=menuBar)


window.mainloop()
