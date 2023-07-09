from tkinter import *
from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer

import pyttsx3


data_list=["Hello",
           "hiii",
           "how are you?",
           "i am good",
           "I am feeling low today",
           "Sorry for that, would you like to play?",
           "No, Not in mood ",
           "How are you?"


      ]




bot=ChatBot("BOT")
trainer=ListTrainer(bot)

data=open("emotion.yml","r",encoding="utf-8").readlines()

trainer.train(data_list)


def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,"You:" +question+"\n\n")
    textarea.insert(END,"Bot:" +str(answer)+"\n\n")
    pyttsx3.speak(answer)

    questionField.delete(0,END)

root=Tk()

root.geometry("500x570+100+30")
root.title("chatter bot created by gunjan")
root.config(bg="light blue")

logoPic=PhotoImage(file="chatter bot1.png")

logoPicLabel=Label(root,image=logoPic)
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=("times new roman",20,"bold"),height=10,yscrollcommand=scrollbar.set,wrap="word")
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=("verdana",20,"bold"))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file="ask1.png")

askButton=Button(root,image=askPic,height=30,width=70,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()

root.bind("<Return>",click)

root.mainloop()