from tkinter import Tk, messagebox, Button, Label
import random

# global values
click_p = ''
click_s = ''
click_r = ''
status_winner = ''
winner = ''
loser = ''
counter_player = 0
counter_bot = 0

# random choose(bot)
bot1 = ['rock', 'scissors', 'paper', 'scissors', 'paper', 'rock', 'paper, scissors', 'rock']
bot = random.choice(bot1)


# functions click and choose value player and choose value bot
def click_btn_s():
    global winner
    global loser
    global status_winner
    global click_s
    global counter_bot
    global counter_player
    click_s = "scissors"
    status_winner = choose_winner(choose_player(), bot)
    winner = status_winner.get('winner')
    choose_player1 = status_winner.get('player')
    choose_bot = status_winner.get('bot')
    if winner == 'bot':
        winner = "bot is"
        loser = "you're"
        counter_bot += 1
    elif winner == "player":
        winner = "you're"
        loser = 'bot is'
        counter_player += 1
    if winner != 'equal':
        lbl_loser.config(text=f"{loser} loser", fg='red')
        lbl_loser.place(x=80, y=70)
        lbl_winner.config(text=f"{winner} winner", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    else:
        counter_bot += 1
        counter_player += 1
        lbl_winner.config(text="equal", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    btn_p.config(state="disable")
    btn_r.config(state="disable")
    btn_s.config(state="disable")
    lbl_bot.config(text=f"bot score:{counter_bot}")
    lbl_player.config(text=f"your score:{counter_player}")
    lbl_player.place(x=80, y=160)
    lbl_bot.place(x=80, y=190)
    if counter_player != 5 and counter_bot != 5:
        messagebox.showinfo(message="new round", title="new")
        btn_p.config(state="normal")
        btn_r.config(state="normal")
        btn_s.config(state="normal")
        if winner != "equal":
            lbl_loser.config(text="")
        lbl_winner.config(text="")
        lbl_status_player.config(text="")
        lbl_status_bot.config(text="")
        lbl_bot.config(text="")
        lbl_player.config(text="")
    elif counter_player != 5 and counter_bot == 5:
        messagebox.showerror(message="you lose", title="lose")
        root.destroy()
    elif counter_player == 5 and counter_bot != 5:
        messagebox.showinfo(message="you wine", title="wins")
        root.destroy()
    elif counter_player == 5 and counter_bot == 5:
        messagebox.showinfo(message="you wine", title="wins")
        root.destroy()


def click_btn_r():
    global counter_player
    global counter_bot
    global winner
    global loser
    global status_winner
    global click_r
    click_r = 'rock'
    status_winner = choose_winner(choose_player(), bot)
    winner = status_winner.get('winner')
    choose_player1 = status_winner.get('player')
    choose_bot = status_winner.get('bot')
    if winner == 'bot':
        winner = "bot is"
        loser = "you're"
        counter_bot += 1
    elif winner == "player":
        winner = "you're"
        loser = 'bot is'
        counter_player += 1
    if winner != 'equal':
        lbl_loser.config(text=f"{loser} loser", fg='red')
        lbl_loser.place(x=80, y=70)
        lbl_winner.config(text=f"{winner} winner", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    else:
        counter_bot += 1
        counter_player += 1
        lbl_winner.config(text="equal", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    btn_p.config(state="disable")
    btn_r.config(state="disable")
    btn_s.config(state="disable")
    lbl_bot.config(text=f"bot score:{counter_bot}")
    lbl_player.config(text=f"your score:{counter_player}")
    lbl_player.place(x=80, y=160)
    lbl_bot.place(x=80, y=190)
    if counter_player != 5 and counter_bot != 5:
        messagebox.showinfo(message="new round", title="new")
        btn_p.config(state="normal")
        btn_r.config(state="normal")
        btn_s.config(state="normal")
        if winner != "equal":
            lbl_loser.config(text="")
        lbl_winner.config(text="")
        lbl_status_player.config(text="")
        lbl_status_bot.config(text="")
        lbl_bot.config(text="")
        lbl_player.config(text="")
    elif counter_player != 5 and counter_bot == 5:
        messagebox.showerror(message="you lost", title="lost")
        root.destroy()
    elif counter_player == 5 and counter_bot != 5:
        messagebox.showinfo(message="you wine", title="wine")
        root.destroy()
    elif counter_player == 5 and counter_bot == 5:
        messagebox.showinfo(message="you wine", title="wine").center()
        root.destroy()


def click_btn_p():
    global loser
    global winner
    global status_winner
    global click_p
    global counter_bot
    global counter_player
    click_p = 'paper'
    status_winner = choose_winner(choose_player(), bot)
    winner = status_winner.get('winner')
    choose_player1 = status_winner.get('player')
    choose_bot = status_winner.get('bot')
    if winner == 'bot':
        winner = "bot is"
        loser = "you're"
        counter_bot += 1
    elif winner == "player":
        winner = "you're"
        loser = 'bot is'
        counter_player += 1
    if winner != 'equal':
        lbl_loser.config(text=f"{loser} loser", fg='red')
        lbl_loser.place(x=80, y=70)
        lbl_winner.config(text=f"{winner} winner", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    else:
        counter_bot += 1
        counter_player += 1
        lbl_winner.config(text="equal", fg='green')
        lbl_winner.place(x=80, y=40)
        lbl_status_bot.config(text=f"bot choose is {choose_bot}")
        lbl_status_player.config(text=f"you're choose is {choose_player1}")
        lbl_status_player.place(x=80, y=100)
        lbl_status_bot.place(x=80, y=130)
    btn_p.config(state="disable")
    btn_r.config(state="disable")
    btn_s.config(state="disable")
    lbl_bot.config(text=f"bot score:{counter_bot}")
    lbl_player.config(text=f"your score:{counter_player}")
    lbl_player.place(x=80, y=160)
    lbl_bot.place(x=80, y=190)
    if counter_player != 5 and counter_bot != 5:
        messagebox.showinfo(message="new round", title="new")
        btn_p.config(state="normal")
        btn_r.config(state="normal")
        btn_s.config(state="normal")
        if winner != "equal":
            lbl_loser.config(text="")
        lbl_winner.config(text="")
        lbl_status_player.config(text="")
        lbl_status_bot.config(text="")
        lbl_bot.config(text="")
        lbl_player.config(text="")
    elif counter_player != 5 and counter_bot == 5:
        messagebox.showerror(message="you lost", title="lost")
        root.destroy()
    elif counter_player == 5 and counter_bot != 5:
        messagebox.showinfo(message="you wine", title="wine")
        root.destroy()
    elif counter_player == 5 and counter_bot == 5:
        messagebox.showinfo(message="you wine", title="wine").center()
        root.destroy()


def choose_player():
    if click_p != '':
        return 'paper'
    elif click_s != '':
        return 'scissors'
    else:
        return 'rock'


# choose winner
def choose_winner(player, robot):
    # equal
    if player == robot:
        return {"winner": 'equal', "player": player, "bot": robot}
    # winner and loser
    elif player == 'scissors' and robot == 'rock':
        return {"winner": "bot", "player": player, "bot": robot}
    elif player == 'scissors' and robot == 'paper':
        return {"winner": "player", "player": player, "bot": robot}
    elif player == 'rock' and robot == 'paper':
        return {"winner": "bot", "player": player, "bot": robot}
    elif player == 'rock' and robot == 'scissors':
        return {"winner": "player", "player": player, "bot": robot}
    elif player == 'paper' and robot == 'rock':
        return {"winner": "player", "player": player, "bot": robot}
    elif player == 'paper' and robot == 'scissors':
        return {"winner": "bot", "player": player, "bot": robot}


# main settings
root = Tk()
root.title('game')
root.resizable(False, False)
root.geometry('300x250')
root.config(bg="green")
btn_s = (Button(root, fg="green", text="scissors", bd=8, command=click_btn_s, state='normal'))
btn_s.place(x=230, y=30)
btn_r = (Button(root, fg="green", text="rock", bd=8, command=click_btn_r, state="normal"))
btn_r.place(x=230, y=130)
btn_p = Button(root, fg="green", text="paper", bd=8, command=click_btn_p,  state="normal")
btn_p.place(x=230, y=80)
lbl_loser = Label(root, text='a')
lbl_winner = Label(root, text='a')
lbl_status_player = Label(root, text='a')
lbl_status_bot = Label(root, text='a')
Label(text="play status:", fg="black").place(x=80, y=0)
lbl_bot = Label(root, text='a')
lbl_player = Label(root, text='a')
root.mainloop()
