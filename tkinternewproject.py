from tkinter import *
from PIL import ImageTk

root = Tk()
root.title('Facts about Different types of Tigers')
tigericon = PhotoImage(file='C:\\tigericon.png')
root.iconphoto(True, tigericon)

siberian = ImageTk.PhotoImage(file='C:\\tiger1siberian.png')
bengal = ImageTk.PhotoImage(file='C:\\tiger2bengal.png')
indochinese = ImageTk.PhotoImage(file='C:\\tiger3indochinese.png')
malayan = ImageTk.PhotoImage(file='C:\\tiger4malayan.png')
sumatran = ImageTk.PhotoImage(file='C:\\tiger5sumatram.png')

tigers = [bengal, indochinese, malayan, siberian, sumatran]

currenttiger = Label(root, image=bengal, height=600, compound='bottom', width=1000)
currenttigerinfo = Label(root, text='Bengal Tiger', font=('Arial', 35, 'bold'))
currenttiger.grid(row=0, column=0, columnspan=3)
currenttigerinfo.grid(row=0, column=0, columnspan=3)
status = Label(root, text=f'tiger 1 of {len(tigers)}', anchor=E, relief=SUNKEN)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forwardbutton(imagenum):
    global currenttiger
    global tigers
    global currenttigerinfo
    global buttonforward
    global currentimage
    global buttonforward
    currentimage = imagenum
    currenttigerinfo.grid_forget()
    currenttiger.grid_forget()
    currenttiger = Label(root, image=tigers[imagenum], height=600, width=1000)
    currenttiger.grid(row=0, column=0, columnspan=3)
    if imagenum == 1:
        currenttigerinfo = Label(root, text='Indochinese Tiger', font=('Arial', 35, 'bold'))
        currenttigerinfo.grid(row=0, column=0, columnspan=3)
        buttonforward = Button(root, text='→', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                               command=lambda: forwardbutton(imagenum + 1))
        buttonforward.grid(row=1, column=2)
        status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    if imagenum == 2:
        currenttigerinfo = Label(root, text='Malayan Tiger', font=('Arial', 35, 'bold'))
        currenttigerinfo.grid(row=0, column=0, columnspan=3)
        buttonforward = Button(root, text='→', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                               command=lambda: forwardbutton(imagenum + 1))
        buttonforward.grid(row=1, column=2)
        status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    if imagenum == 3:
        currenttigerinfo = Label(root, text='Siberian Tiger', font=('Arial', 35, 'bold'))
        currenttigerinfo.grid(row=0, column=0, columnspan=3)
        buttonforward = Button(root, text='→', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                               command=lambda: forwardbutton(imagenum + 1))
        buttonforward.grid(row=1, column=2)
        status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    elif imagenum == 4:
        currenttigerinfo = Label(root, text='Sumatran Tiger', font=('Arial', 35, 'bold'))
        currenttigerinfo.grid(row=0, column=0, columnspan=3)
        buttonforward = Button(root, text='→', state=DISABLED)
        buttonforward.grid(row=1, column=2)
        status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3, command=lambda: backclick(imagenum-1))
    buttonbackward.grid(row=1, column=0)

def backclick(imagenum):
    global buttonbackward
    global tigers
    global currenttigerinfo
    global currenttiger
    global buttonforward
    currenttiger.grid_forget()
    currenttigerinfo.grid_forget()
    if imagenum == 0:
        buttonbackward = Button(root, text='←', state=DISABLED)
        buttonbackward.grid(row=1, column=0)
        currenttiger = Label(root, image=tigers[0], height=600, width=1000)
        currenttigerinfo = Label(root, text='Bengal Tiger', font=('Arial', 35, 'bold'))
        currenttigerinfo.grid(row=0, column=0, columnspan=3)
        currenttiger.grid(row=0, column=0, columnspan=3)
        status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    elif imagenum > 0:
        currenttiger = Label(root, image=tigers[imagenum], height=600, width=1000)
        currenttiger.grid(row=0, column=0, columnspan=3)
        if imagenum == 1:
            currenttigerinfo = Label(root, text='Indochinese Tiger', font=('Arial', 35, 'bold'))
            currenttigerinfo.grid(row=0, column=0, columnspan=3)
            buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                                    command=lambda: backclick(imagenum - 1))
            buttonbackward.grid(row=1, column=0)
            status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
            status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        if imagenum == 2:
            currenttigerinfo = Label(root, text='Malayan Tiger', font=('Arial', 35, 'bold'))
            currenttigerinfo.grid(row=0, column=0, columnspan=3)
            buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                                    command=lambda: backclick(imagenum - 1))
            buttonbackward.grid(row=1, column=0)
            status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
            status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        if imagenum == 3:
            currenttigerinfo = Label(root, text='Siberian Tiger', font=('Arial', 35, 'bold'))
            currenttigerinfo.grid(row=0, column=0, columnspan=3)
            buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                                    command=lambda: backclick(imagenum - 1))
            buttonbackward.grid(row=1, column=0)
            status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
            status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        elif imagenum == 4:
            currenttigerinfo = Label(root, text='Sumatran Tiger', font=('Arial', 35, 'bold'))
            currenttigerinfo.grid(row=0, column=0, columnspan=3)
            buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                                    command=lambda: backclick(imagenum - 1))
            status = Label(root, text=f'tiger {imagenum+1} of {len(tigers)}', anchor=E, relief=SUNKEN)
            status.grid(row=2, column=0, columnspan=3, sticky=W + E)
            buttonbackward.grid(row=1, column=0)
    buttonforward = Button(root, text='→', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3,
                           command=lambda: forwardbutton(imagenum + 1))
    buttonforward.grid(row=1, column=2)

buttonforward = Button(root, text='→', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3, command=lambda: forwardbutton(1))
buttonforward.grid(row=1, column=2)
buttonquit = Button(root, text='Quit', fg='black', bg='#d3d3d3', width=10, height=3, padx=5, pady=3, command=root.quit)
buttonquit.grid(row=1, column=1)
buttonbackward = Button(root, text='←', fg='black', bg='#d3d3d3', width=15, height=3, padx=5, pady=3, command=lambda: backclick(0), state=DISABLED)
buttonbackward.grid(row=1, column=0)

root.mainloop()
