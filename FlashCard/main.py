from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}


try:
    data=pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    org_data=pd.read_csv("data/french_words.csv")
    to_learn=org_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    flip_timer=window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card['French'],fill="black")
    canvas.itemconfig(card_bg,image=card_img)
    flip_timer=window.after(3000,func=flip_card)
def flip_card():
    canvas.itemconfig(card_bg,image=card_back)
    canvas.itemconfig(card_title,text='English',fill="white")
    canvas.itemconfig(card_word,text=current_card['English'],fill="white")

def is_known():
    data=to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()



window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)
#canvas.itemconfig(card_img,image=card_back)

canvas=Canvas(width=800,height=526)
card_img=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
card_bg=canvas.create_image(400,263,image=card_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="word",font=('arial',30,'italic'))
card_word=canvas.create_text(400,263,text="meaning",font=('arial',20,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

cross_img=PhotoImage(file="images/wrong.png")
un_button=Button(image=cross_img,command=next_card,highlightthickness=0)
un_button.grid(row=1,column=0)
right_img=PhotoImage(file="images/right.png")
kn_button=Button(image=right_img,command=is_known,highlightthickness=0)
kn_button.grid(row=1,column=1)

next_card()
window.mainloop()

