from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
WORD = None


# ------------------------- READ DATA -----------------------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

to_learn = data.to_dict('records')

def next_card():
    global current_card # let this variable can be used in flip_card func
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text = "French", fill= "black")
    canvas.itemconfig(word_text, text=current_card['French'], fill = "black")
    canvas.itemconfig(card_background, image=cardfront_img)
    flip_timer= window.after(3000, func=flip_card)

def check_read():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index = False)
    next_card()


# -------------------------- FLIP THE CARD ------------------------------------
def flip_card():
    canvas.itemconfig(title_text, text = "English", fill="white")
    canvas.itemconfig(word_text, text = current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=cardback_img)



# ------------------------- UI SETUP -------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardfront_img = PhotoImage(file="./images/card_front.png")
cardback_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263,image=cardfront_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263,text="Word", fill="black",font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



# wrong_buttom = Button(image="./images/wrong.png")
# wrong_buttom.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
unkonwn_img = PhotoImage(file="./images/wrong.png")
unkonwn_buttom = Button(image=unkonwn_img, highlightthickness=0, command = next_card)
unkonwn_buttom.grid(column=0, row=1)
check_buttom = Button(image=check_img,highlightthickness=0, command=check_read)
check_buttom.grid(column=1, row=1)

next_card()



window.mainloop()