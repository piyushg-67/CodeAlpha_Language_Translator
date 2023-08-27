from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1= trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
    s= sor_comb.get()
    d= dest_comb.get()
    msg= src_text.get(1.0,END)
    textget=change(text= msg, src=s,dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="White")

lab_txt= Label(root,text="Translator", font=("Times New Roman", 40,"bold"),bg="grey")
lab_txt.place(x=100,y=20,height=50,width=300)

frame= Frame(root).pack(side=BOTTOM)

lab_txt= Label(root,text="Source Text", font=("Times New Roman", 20,"bold"),bg="grey")
lab_txt.place(x=100,y=100,height=25,width=300)

src_text=Text(frame,font=("Times New Roman", 20,"bold"),wrap=WORD,bg="red")
src_text.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

sor_comb= ttk.Combobox(frame,value=list_text)
sor_comb.place(x=9,y=300,height=40,width=120)
sor_comb.set("English")

button_change=Button(frame, text="Translate", relief=RAISED,command=data)
button_change.place(x=190,y=300,height=40,width=120)

dest_comb= ttk.Combobox(frame,value=list_text)
dest_comb.place(x=370,y=300,height=40,width=120)
dest_comb.set("English")

lab_txt= Label(root,text="Destination Text", font=("Times New Roman", 20,"bold"),bg="grey")
lab_txt.place(x=100,y=360,height=25,width=300)

dest_text=Text(frame,font=("Times New Roman", 20,"bold"),wrap=WORD,bg="red")
dest_text.place(x=10,y=400,height=150,width=480)


root.mainloop()