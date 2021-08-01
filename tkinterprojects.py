from tkinter import *
import random

root = Tk()
root.title('Rock Paper Scissors')
e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3)
window_icon = PhotoImage(file='C:\\rockpaperscissorstk.png')
root.iconphoto(True, window_icon)

def choserock():
    global player_move
    player_move = 'rock'
    e.delete(0, END)
    e.insert(0, player_move)

def chosepaper():
    global player_move
    player_move = 'paper'
    e.insert(0, player_move)

def chosescissor():
    global player_move
    player_move = 'scissor'
    e.insert(0, player_move)

def play():
    moves = ['rock', 'paper', 'scissor']
    cpu_move = random.choice(moves)
    e.delete(0, END)
    cpumoverandom = f'the cpu uses {cpu_move}'
    e.insert(0, cpumoverandom)
    if cpu_move == 'rock' and player_move == 'scissor':
        results = 'You lost, loser'
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == 'rock' and player_move == 'paper':
        results = "Congrats you're a winner!"
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == 'paper' and player_move == 'rock':
        results = 'You lost, loser'
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == 'paper' and player_move == 'scissor':
        results = "Congrats you're a winner!"
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == 'scissor' and player_move == 'rock':
        results = "Congrats you're a winner!"
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == 'scissor' and player_move == 'paper':
        results = 'You lost, loser'
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)
    if cpu_move == player_move:
        results = 'It was a tie game!'
        cpumovelabel = Label(root, text=results, width=20, font=('Arial', 30, 'bold'))
        cpumovelabel.grid(row=2, column=0, columnspan=3)

def restart():
    e.delete(0, END)

button_rock = Button(root, text='Rock', fg='black', bg='#d3d3d3', width=30, height=10, padx=5, pady=3, command=choserock)
button_rock.grid(row=3, column=0)
button_paper = Button(root, text='Paper', fg='black', bg='#d3d3d3', width=30, height=10, padx=5, pady=3, command=chosepaper)
button_paper.grid(row=3, column=1)
button_scissor = Button(root, text='Scissor', fg='black', bg='#d3d3d3', width=30, height=10, padx=5, pady=3, command=chosescissor)
button_scissor.grid(row=3, column=2)

button_play = Button(root, text='Click to use', fg='black', bg='#d3d3d3', width=35, height=1, padx=5, pady=3, command=play)
button_play.grid(row=1, column=0, columnspan=3)

button_restart = Button(root, text='Restart Game', fg='black', bg='#d3d3d3', width=15, height=1, padx=5, pady=3, command=restart)
button_restart.grid(row=4, column=0, columnspan=3)

root.mainloop()
