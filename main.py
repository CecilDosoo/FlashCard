from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_f.itemconfig(title,text="French",fill="black")
    card_f.itemconfig(word, text=current_card["French"], fill="black")
    card_f.itemconfig(logo_image, image=front_logo)
    flip_timer = window.after(3000, back_card)

def back_card():
    card_f.itemconfig(title, text="English",fill="white")
    card_f.itemconfig(word, text=current_card["English"], fill="white")
    card_f.itemconfig(logo_image, image=back_logo)

def known_words():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    card()



window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

flip_timer = window.after(3000, back_card)

card_f = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_logo= PhotoImage(file="images/card_front.png")
back_logo = PhotoImage(file="images/card_back.png")

logo_image = card_f.create_image(400, 263, image=front_logo)

title = card_f.create_text(400,150,text="Title",font=("Arial",40,"italic"))
word = card_f.create_text(400,260,text="Word",font=("Arial",60,"bold"))
card_f.grid(column=0,row=0,columnspan=2)

x = PhotoImage(file="images/wrong.png")
x_button = Button(image=x,highlightthickness=0,command=card)
x_button.grid(column=0,row=1)

r = PhotoImage(file="images/right.png")
r_button = Button(image=r,highlightthickness=0,command=known_words)
r_button.grid(column=1,row=1)

card()

window.mainloop()