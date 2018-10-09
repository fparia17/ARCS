from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    
root = Tk()

#Create three frames for the GUI
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
lowFrame = Frame(root)
lowFrame.pack()

#Import test and button to top frame
step1 = Label(topFrame, text="STEP 1")
step1.pack()
theLabel = Label(topFrame, text ="Select the ARCS CD directory")
theLabel.pack()

#Set up the Browse button
folder_path = StringVar()
entry1 = Entry(topFrame, textvariable=folder_path)
entry1.pack(side=LEFT)
button1 = Button(topFrame, text='Browse', fg='black', bg='grey', command=browse_button)
button1.pack(side=LEFT)

#Import test and button to bottom frame
seperator1 = Label(bottomFrame, text="------------------------------------")
seperator1.pack()
step2 = Label(bottomFrame, text="STEP 2")
step2.pack()
theLabel2 = Label(bottomFrame, text ="Type ARCS ID")
theLabel2.pack()
entry2 = Entry(bottomFrame)
entry2.pack()

#Import test and button to lower frame
seperator1 = Label(lowFrame, text="------------------------------------")
seperator1.pack()
step3 = Label(lowFrame, text="STEP 3")
step3.pack()
theLabel3 = Label(lowFrame, text="Locate and Compress")
theLabel3.pack()
button2 = Button(lowFrame, text='Create', fg='black', bg='grey')
button2.pack()

root.mainloop()
