from bs4 import BeautifulSoup
import requests
import tkinter
from tkinter import *
from tkinter import messagebox

def sacar_info_pomodoro():
    url = "https://lecturaagil.com/como-ser-mas-productivo-con-la-tecnica-del-pomodoro/"
    pagina= requests.get(url)
    soup= BeautifulSoup(pagina.content,"html.parser")
    pomodoro= soup.find_all("p")
    textofin=[]
    texto=""
    for pom in range(0,len(pomodoro)):
        if pomodoro[pom].string == None:
            continue
        else:
            textofin+=[pomodoro[pom].string]
    for item in range(3,len(textofin)-11):
        if textofin[item] == '\xa0':
            continue
        else:
            texto+=textofin[item]

    messagebox.showinfo(message=texto,title="Info")



def menu():
    ventana=Tk()
    ventana.title("Info")
    ventana.geometry("180x80")
    ventana.configure(bg="gray")

    Label(ventana,text="¿Que es la tecnica pomodoro?",bg="cyan").pack(fill=X,pady=2)
    Button(ventana,text="Info",command=sacar_info_pomodoro).pack(pady=5)

    ventana.mainloop()
    
menu()



