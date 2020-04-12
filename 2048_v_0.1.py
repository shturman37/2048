# !env/home/ar4i/PycharmProjects/foxford/venv/bin/python3

from tkinter import *
from random import randint
from time import sleep, time
root = Tk()
root.title('Game - 2048')
root.geometry("480x540+100+100")
root.resizable(0, 0)
frame_top = Frame(root, height=30, relief=SOLID, bd=1)
frame_mid = Frame(root, bg='#bbada0', height=480, padx=9, pady=8)
frame_bot = Frame(root, height=30, relief=SOLID, bd=1)
frame_top.pack(fill=BOTH, side=TOP)
frame_mid.pack(fill=BOTH)
frame_bot.pack(fill=BOTH, side=BOTTOM)


field = [[None] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        Label(frame_mid,
              height=2,
              width=4,
              font="Arial 32",
              bg='#cdc1b4',
              bd=0).place(y=i*120, x=j*120)


def check_empty_fields():
    count = 0
    for row in field:
        for elem in row:
            if elem is None:
                count += 1
    return count


def check_quantity_press_arrow():
    a = time()
    print(a)
    pass
#  TODO continue this function

def start():
    if check_empty_fields() == 16:
        add_tile()
        add_tile()


def game_over():
    print("Stop")
    Message(frame_mid, text="Game Over", font="Arial 48", bg='royalblue', fg='ivory',
            relief=GROOVE).place(relheight=1, relwidth=1)

def exit():
    root.destroy()


def change_color(tile):
    if tile == 2:
        return "#eee4da"
    elif tile == 4:
        return '#ede0c8'
    elif tile == 8:
        return '#f2b179'
    elif tile == 16:
        return '#f59563'
    elif tile == 32:
        return '#f67c5f'
    elif tile == 64:
        return '#f65e3b'
    elif tile == 128:
        return '#edcf72'
    elif tile == 256:
        return '#edcc61'
    elif tile == 512:
        return '#edc850'
    elif tile == 1024:   # нужен цвет
        return '#c8d831'
    else:
        return '#fa0d15'

var = StringVar()
a = 0
def count_score(count):
    global a
    a += count
    var.set(a)


def add_tile():
    rnd_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    rnd_show = randint(0, 9)
    i, j = randint(0, 3), randint(0, 3)
    if not field[i][j]:
        field[i][j] = Label(frame_mid, text=rnd_list[rnd_show],
                            width=4, height=2,
                            relief=GROOVE,
                            font='Arial 32')
        field[i][j]["bg"] = change_color(field[i][j]["text"])
        field[i][j].place(y=i*120, x=j*120)
    else:
        if check_empty_fields() != 0:
            add_tile()
        else:
            game_over()
# TODO
#  3. Need function to control quantity push keyboard arrow, Need find in intrnet;
#  4. Function best
#  5. Function timer
#  6. Add button 'Play Again'


def left(event):
    if check_empty_fields() != 16:
        count = False
        # сдвиг
        for i in range(4):
            free = 0
            for j in range(4):
                if not field[i][j]:
                    free += 1
                else:
                    if free > 0:
                        field[i][j - free] = field[i][j]
                        for d in range(1, 11):
                            field[i][j - free].place(y=i*120, x=j*120-free*d*12)
                            root.update()
                            sleep(0.008)
                        field[i][j] = None
                        count = True

                    if j - free > 0 and field[i][j - free]["text"] == field[i][j - free - 1]["text"]:
                        for d in range(1, 11):
                            field[i][j - free].place(y=i*120, x=(j-free)*120-d*12)
                            root.update()
                            sleep(0.008)
                        field[i][j - free].destroy()
                        field[i][j - free - 1]["text"] = field[i][j - free - 1]["text"] * 2
                        field[i][j - free - 1]["bg"] = change_color(field[i][j - free - 1]["text"])
                        count_score(field[i][j - free - 1]["text"])
                        field[i][j - free] = None
                        free += 1
                        count = True
        if count:
            add_tile()
        else:
            if check_empty_fields() == 0:
                game_over()
            print("Хода влево нет")


def right(event):
    if check_empty_fields() != 16:
        count = False
        # сдвиг
        for i in range(4):
            free = 0
            for j in range(3, -1, -1):
                if not field[i][j]:
                    free += 1
                else:
                    if free > 0:
                        field[i][j + free] = field[i][j]
                        for d in range(1, 11):
                            field[i][j + free].place(y=i*120, x=j*120+free*d*12)
                            root.update()
                            sleep(0.008)
                        field[i][j] = None
                        count = True

                    if j + free < 3 and field[i][j + free]["text"] == field[i][j + free + 1]["text"]:
                        for d in range(1, 11):
                            field[i][j + free].place(y=i*120, x=(j+free)*120+d*12)
                            root.update()
                            sleep(0.008)
                        field[i][j + free].destroy()
                        field[i][j + free + 1]["text"] = field[i][j + free + 1]["text"] * 2
                        field[i][j + free + 1]["bg"] = change_color(field[i][j + free + 1]["text"])
                        count_score(field[i][j + free + 1]["text"])
                        field[i][j + free] = None
                        free += 1
                        count = True
        if count:
            add_tile()
        else:
            if check_empty_fields() == 0:
                game_over()
            print("Хода вправо нет")


def up(event):
    if check_empty_fields() != 16:
        count = False
        # сдвиг
        for j in range(4):
            free = 0
            for i in range(4):
                if not field[i][j]:
                    free += 1
                else:
                    if free > 0:
                        field[i - free][j] = field[i][j]
                        for d in range(1, 11):
                            field[i - free][j].place(y=i*120-free*d*12, x=j*120)
                            root.update()
                            sleep(0.008)
                        field[i][j] = None
                        count = True

                    if i - free > 0 and field[i - free][j]["text"] == field[i - free - 1][j]["text"]:
                        for d in range(1, 11):
                            field[i - free][j].place(y=(i-free)*120-d*12, x=j*120)
                            root.update()
                            sleep(0.008)
                        field[i - free][j].destroy()
                        field[i - free - 1][j]["text"] = field[i - free - 1][j]["text"] * 2
                        field[i - free - 1][j]["bg"] = change_color(field[i - free - 1][j]["text"])
                        count_score(field[i - free - 1][j]["text"])
                        field[i - free][j] = None
                        free += 1
                        count = True
        if count:
            add_tile()
        else:
            if check_empty_fields() == 0:
                game_over()
            print("Хода вверх нет")


def down(event):
    if check_empty_fields() != 16:
        count = False
        # сдвиг
        for j in range(4):
            free = 0
            for i in range(3, -1, -1):
                if not field[i][j]:
                    free += 1
                else:
                    if free > 0:
                        field[i + free][j] = field[i][j]
                        for d in range(1, 11):
                            field[i + free][j].place(y=i*120+free*d*12, x=j*120)
                            root.update()
                            sleep(0.008)
                        field[i][j] = None
                        count = True

                    if i + free < 3 and field[i + free][j]["text"] == field[i + free + 1][j]["text"]:
                        for d in range(1, 11):
                            field[i + free][j].place(y=(i+free)*120+d*12, x=j*120)
                            root.update()
                            sleep(0.008)
                        field[i + free][j].destroy()
                        field[i + free + 1][j]["text"] = field[i + free + 1][j]["text"] * 2
                        field[i + free + 1][j]["bg"] = change_color(field[i + free + 1][j]["text"])
                        count_score(field[i + free + 1][j]["text"])
                        field[i + free][j] = None
                        free += 1
                        count = True
        if count:
            add_tile()
        else:
            if check_empty_fields() == 0:
                game_over()
            print("Хода вверх нет")


score_lable = Label(frame_top, text=0, textvariable=var, width=20)
score_lable.pack(side=RIGHT)
best_lable = Label(frame_top, text='Best:', width=10)
best_lable.pack(side=RIGHT)
but_exit = Button(frame_bot, text='Exit', command=exit)
but_exit.pack(side=RIGHT)
but_start = Button(frame_bot, text='Start', command=start)
but_start.pack(side=RIGHT)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()
