from tkinter import*
import random
from tkinter import messagebox

# a random number between 1 and 9 is assigned
# the number(x) is in str type to easily add new number to it
x = str(random.randint(1, 9))
# 'a' specifies index
a = 1

# initial size of the pattern is 5
i = 1
while i < 5:
    x = x + str(random.randint(0, 9))
    i += 1


def increment():
    def error():
        bye.destroy()

    global a
    k = 0
    global x

    guess = enter_guess.get()
    try:
        if int(guess) == int(x):
            enter_guess.delete(0, 'end')
            s = str(random.randint(1, 9))
            while k < a:
                s = s + str(random.randint(0, 9))
                k += 1

            x = s
            a = 1
            Game(outLine)

        elif int(guess) == -1:
            exit()
        else:
            bye = Label(outLine, text="SORRY!WRONG ANSWER\nTRY AGAIN",
                        font="Arial 30",
                        bg="RosyBrown1",
                        fg="red")
            bye.place(relx=0.1, rely=0.35)
            bye.after(1500, error)
    except ValueError:
        messagebox.showerror("BE CAREFUL", "PLEASE\nENTER AN INTEGER VALUE")


class Game:
    def __init__(self, value):
        self.number = int(x[0])
        self.label = Label(value, text="%i" % self.number,
                           font="Arial 30",
                           width=10,
                           bg="RosyBrown1",
                           fg="blue4")
        self.label.place(relx=random.uniform(0.2, 0.7), rely=random.uniform(0.3, 0.7))
        self.label.after(1000, self.disappear_label)

    def disappear_label(self):
        global a
        if a > len(x) or a == len(x):
            buton = Button(outLine,
                           text='GUESS',
                           activebackground="red",
                           activeforeground="red",
                           bg="PaleVioletRed4",
                           fg="pink",
                           font="Arial 12 bold",
                           width=30,
                           relief="raised",
                           command=increment)
            buton.place(relx=0.1, rely=0.2, height=45, width=85)
            self.label.destroy()
        try:
            self.number = int(x[a])
            # displaying the new number
            self.label.configure(text="%i" % self.number)
            self.label.place(relx=random.uniform(0.2, 0.7), rely=random.uniform(0.3, 0.7))
            # calling self.disappear_label after 1s
            self.label.after(1000, self.disappear_label)
            a += 1
        except:
            pass


if __name__ == "__main__":
    outLine = Tk()
    outLine.title("Welcome to The Memory Game - Have Fun !!")
    outLine.geometry("750x400")
    f = Frame(outLine, bg="RosyBrown1")
    f.pack(fill=BOTH, expand=1)
    enter_guess = Entry(outLine,
                        width=65,
                        relief="groove",
                        bg="light blue",
                        fg="dark blue",
                        font="Arial 12 bold")
    enter_guess.place(relx=0.1, rely=0.1, height=30)

    def start_game():
        Game(outLine)
        infoButon.destroy()
        startButon.after(0, startButon.destroy())

    def info():
        messagebox.showinfo("--INFO--",
                            "* Follow the random numbers that appear on the screen carefully\n" +
                            "* Each digit will disappear in 1 second\n" +
                            "* Remember them all and then enter the number in the box\n" +
                            "* The initial size of the first pattern is 5 !!\n" +
                            "  But the pattern size increases by 1 for each successful guess\n" +
                            "* Enter -1 to exit")


    infoButon = Button(outLine,
                       text="INFORMATION",
                       activebackground="red",
                       activeforeground="red",
                       bg="cornflower blue",
                       fg="yellow",
                       font="Arial 15 bold",
                       width=30,
                       relief="raised",
                       command=info
                       )
    infoButon.place(relx=0.27, rely=0.35, width=185, height=85)
    startButon = Button(outLine,
                        text='START',
                        activebackground="red",
                        activeforeground="red",
                        bg="cornflower blue",
                        fg="yellow",
                        font="Arial 15 bold",
                        width=30,
                        relief="raised",
                        command=start_game
                        )
    startButon.place(relx=0.52, rely=0.35, height=85, width=145)

    outLine.mainloop()