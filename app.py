from cgitb import text
import tkinter
from tkinter import *
import random

questions = [
    "The Battle of Plassey was fought in ?",
    "ICICI is the name of a ?",
    "Which was the 1st non Test playing country to beat India in an international match ?",
    "Who is the first Indian woman to win an Asian Games gold in 400m run ?",
    "Ricky Ponting is also known as what ?",
    "How long are professional Golf Tour players allotted per shot ?",
    "In the match between India and Pakistan at Jaipur on 02-10-1983, Which new rule was introduced?",
    "The first hang gliders to be flown were flown in...?",
    "India won its first Olympic hockey gold in...?",
    "Who was the 1st ODI captain for India ?",
]

answer_choice = [
    ["1757","1782","1748","1764",],
    ["chemical industry","bureau","corporation","financial institution",],
    ["Canada","Sri Lanka","Zimbabwe","East Africa",],
    ["M.L.Valsamma","P.T.Usha","Kamaljit Sandhu","K.Malleshwari",],
    ["The Rickster","Ponts","Ponter","Punter",],
    ["45 seconds","25 seconds","1 minute","2 minute",],
    ["Limit of overs was reduced to 50 overs","The rule of field restriction was taken.","Over throw runs were batsman's score","No-balls & wides were debited to bowlers analysis",],
    ["1600s","1700s","1800s","1900s",],
    ["1928","1932","1936","1948",],
    ["Ajit Wadekar","Bishen Singh Bedi","Nawab Pataudi","Vinoo Mankad",],
]

answer = [0,3,1,2,3,0,3,2,0,0]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()

    if score >=20:
        img = PhotoImage(file = "great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are excellent !!")
    elif (score >=10 and score < 20):
        img = PhotoImage(file = "ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You can be better !!")
    else:
        img = PhotoImage(file = "bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should work hard !!")

def calc():
    global indexes,user_answer,answer
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answer[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)

    if ques < 5:
        lblQuestion.config(text = questions[indexes[ques]])
        r1['text'] = answer_choice[indexes[ques]][0]
        r2['text'] = answer_choice[indexes[ques]][1]
        r3['text'] = answer_choice[indexes[ques]][2]
        r4['text'] = answer_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()

def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas",16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][0],
        font = ("Times",12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][1],
        font = ("Times",12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][2],
        font = ("Times",12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answer_choice[indexes[0]][3],
        font = ("Times",12),
        value = 4,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnstart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Quiz application")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quiz",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnstart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnstart.pack()

lblInstruction = Label(
    root,
    text = "Read the rules and\nClick start ones you are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 10 questions\nYou will get 20 seconds to solve a questions\nOnce you select a radio button that will be a final choice\nHence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()