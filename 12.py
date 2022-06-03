import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import time
import requests
import json


root=tk.Tk()

tk.Label(text="ONLINE CRICKET SCOREBOARD",fg='red',bg='black',font="Times 40 bold").pack()

canvas=Canvas(root,width=224,height=280)
canvas.place(x=1250,y=250)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\SALMAN S_7\\Music\\cricket.png"))
canvas.create_image(0,0,anchor=NW,image=image)


b1=Button(root,height=2,width=20,text="EXIT",command=root.destroy)
b1.place(x=600,y=500)


root.geometry("1980x600")
root.geometry("1980x600")
root.title('Scorespro')
root.title('Scorespro')
root.configure(bg='black')
root.configure(bg='black')


root.iconbitmap(r'C:\Users\SALMAN S_7\Desktop\PYTHON\cricket.ico')



match_data=requests.get('https://cricapi.com/api/cricketScore?unique_id=1237181&apikey=0r0CmIr91qeY5aANIGpZ1ogdQKB3')
json_data=match_data.json()


def times():
    current_score=json_data['score']
    score.configure(text="CURRENT SCORE :  "+current_score)
    score.after(100,time)
    current_stat=json_data['stat']
    stat.configure(text="CURRENT STAT  :  "+current_stat)
    stat.after(100,time)


score=Label(root,fg='blue',bg='black',font=("times",30,"bold"))
score.place(x=25,y=150)
stat=Label(root,fg='blue',bg='black',font=("times",30,"bold"))
stat.place(x=25,y=250)


times()

root.mainloop()
