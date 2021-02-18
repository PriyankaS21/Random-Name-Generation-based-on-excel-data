import tkinter as tk
import random
import pandas as pd
import time
from datetime import datetime


root = tk.Tk()
root.title('GAME IS ON') 

df_team_member = pd.read_excel(f'DATA\\Name_list.xlsx')
team_name_list = df_team_member['Team_Member'].tolist()

def guessThePerson():     
    list1=[]    
    for i in team_name_list:
        r=random.sample(team_name_list,1)        
        if r not in list1:
            list1.append(r[0])     
        
    print(r[0]) 
    text_ = " " * 100
    label1 = tk.Label(root, text= text_,font=('helvetica', 10, 'bold'))    
    canvas1.create_window(200, 230, window=label1) 
    
    label2 = tk.Label(root, text= r[0],font=('helvetica', 10, 'bold'))    
    canvas1.create_window(200, 230, window=label2)
    team_name_list.remove(r[0])

# Code to add widgets will go here...
canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.pack()


button1 = tk.Button(text='Guess The Person', command=guessThePerson, activebackground='yellow')
canvas1.create_window(200, 180, window=button1)


root.mainloop()