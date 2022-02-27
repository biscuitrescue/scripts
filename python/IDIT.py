#!/usr/bin/env python3
from tkinter import *
import os
from datetime import date
from time import sleep

col_deepblue="#282a36"
col_lighterblue="#44475a"
col_foreground="#f8f8f2"
col_lightestblue="#6272a4"
col_cyan="#8be9fd"
col_green="#50fa7b"
col_orange="#ffb86c"
col_pink="#ff79c6"
col_purple="#bd93f9"
col_red="#ff5555"
col_yellow="#f1fa8c"

root = Tk()
root.title("I'll do it tomorrow:)")
root.configure(background="#282a36")
root.geometry("700x400")


fontboi="arial"
tt_file = "/home/trogdor/.do.txt"

# file_entry = Entry(root,bg="#f1fa8c", font=(fontboi,12))
# file_entry.insert(0,"tt.txt")
# tt_file = file_entry.get()
# file_entry.place(x=70,y=25,height=30,width=215)


# file_name_label = Label(root,bg="#f1fa8c",font=(fontboi,12),text="File:")
# file_name_label.place(x=25,y=25,height=30,width=40)

date_panel_color=col_purple
colour_label_date = Label(root,text='',bg=date_panel_color)
colour_label_date.place(x=0,y=350,height=50,width=350)

time_label = Label(root,text="Datestamping:", font=(fontboi,12),bg=date_panel_color)
time_label.place(x=25,y=360,height=30,width=100)
r = IntVar()
r.set(0)

Radiobutton(root,text="Enable",variable=r,value=1,bg=date_panel_color,activebackground=date_panel_color,borderwidth=0,highlightthickness=0).place(x=135,y=360,height=30,width=70)
Radiobutton(root,text="Disable",variable=r,value=0,bg=date_panel_color,activebackground=date_panel_color,borderwidth=0,highlightthickness=0).place(x=210,y=360,height=30,width=70)


if os.path.exists(tt_file):
    None
else:
    file = open(tt_file,'w')
    file.close()

file = open(tt_file)
Lis1 = file.readlines()
file.close()

def printer():
    global L1
    global Lis1
    global s
    s = '\n  To do list:\n'
    for i in range(len(Lis1)):
        s+="    "+str(i+1)+") "+Lis1[i]
    L1 = Label(root,text=s,bg=col_yellow,justify="left",anchor="nw", font=(fontboi,13))
    L1.place(x=350,y=0,height=4000,width=4000) 

printer()

def click1(a):
    today=date.today()
    global s
    global r
    global E1
    global Lis1
    work = E1.get()
    date_resp=r.get()
    if a == 1:
        if work[0]==">":
            index=''
            for i in range(len(work)):
                if work[i].isdigit()==True:
                    index+=work[i]
                elif work[i]==">" or work[i]==")" or work[i]==" ":
                    continue
                else:
                    work = work[i:]
                    break
            if date_resp==1:
                Lis1[int(index)-1]=work.title()+" ["+today.strftime('%d-%b-%Y')+"]"+'\n'
            elif date_resp==0:
                Lis1[int(index)-1]=work.title()+'\n'
        else:
            if date_resp==1:
                Lis1.append(work.title()+" ["+today.strftime('%d-%b-%Y')+"]"+'\n')
            elif date_resp==0:
                Lis1.append(work.title()+'\n')
    elif a == 2:
        wdone = int(work)
        Lis1.pop(wdone-1)

    elif a == 3:
        wdone = int(work)
        str1=Lis1[wdone-1]
        str2='\u0336'
        for c in str1:
            str2+= c + '\u0336'
        Lis1.pop(wdone-1)
        Lis1.append(str2[:-1])

    printer()
    file = open(tt_file,'w')
    for i in Lis1:
        file.write(i)
    file.close()
    E1.delete(0,END)

E1 = Entry(root,bg=col_yellow, font=(fontboi,12))
B1 = Button(root,text="Add/Modify(>) ",command=lambda:click1(1),bg=col_cyan, font=(fontboi,11),bd=0)
B2 = Button(root,text="Remove",command=lambda:click1(2),bg=col_red, font=(fontboi,11),bd=0)
B3 = Button(root,text="Job Done",command=lambda:click1(3),bg=col_green,font=(fontboi,11),bd=0)
L1 = Label(root,text=s,bg=col_yellow,justify="left",anchor="nw", font=(fontboi,13))

E1.place(x=25,y=145,height=30,width=300)
B1.place(x=25,y=185,height=30,width=145)
B2.place(x=180,y=185,height=30,width=145)
B3.place(x=25,y=225,height=30,width=300)
L1.place(x=350,y=0,height=4000,width=4000)



root.mainloop()
