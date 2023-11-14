from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import tkinter.font as Tkfont
import level1
import level2
import level3

win = Tk()
win.title("JUEGO DE PAREJAS")
win.geometry("530x480")
win.resizable(width=False, height=False)

# Connect to database
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Main Title
fontTitle = Tkfont.Font(size=24)
Label(win, text="JUEGO DE PAREJAS", padx=0, pady=30, font=fontTitle).grid(row=0, column=0, columnspan=4)

# Player name
def get_name():
    global name
    name = name_entry.get()

fontName = Tkfont.Font(size=10)
lbl_name = Label(win, text="Nombre:", font=fontName)
lbl_name.grid(row=1, column=0, padx=15, pady=10)   

name_entry = Entry(win, width=50)
name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=25, pady=1)

Button(win, width=10, text="Ingresar", command=get_name).grid(row=1, column=3, columnspan=1, padx=6, sticky="ew")

# Levels
LvlFrame = LabelFrame(win)
LvlFrame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=20)
Label(LvlFrame, text="Selecciona un nivel:").grid(row=0, column=0, sticky="ew")

levels = [("Nivel 1", "1"), ("Nivel 2", "2"), ("Nivel 3", "3"),]
lvl = StringVar()
lvl.set("None")
n = 2

for text, level in levels:
    Radiobutton(LvlFrame, variable=lvl, text=text, value=level).grid(row=n, column=0, sticky="ew")
    n += 1

#Img Types

ImgTypeFrame = LabelFrame(win)
ImgTypeFrame.grid(row=2, column=2, columnspan=2, sticky="ew", padx=5, pady=20)
Label(ImgTypeFrame, text="Selecciona un tipo de imagen:").grid(row=0, column=1, sticky="ew")

types = [("Paisajes", "1"), ("Superheroes", "2"), ("Animales", "3")]
type = StringVar()
type.set("None")
m = 2

for text, k in types:
    Radiobutton(ImgTypeFrame, variable=type, text=text, value=k).grid(row=m, sticky="ew", column=1)
    m += 1

#Hall of Fame
def fame():
    return

fame_btn = Button(win, text="Salón de la Fama", width=15, height=4, command=fame)
fame_btn.grid(row=3, column=2, columnspan=2, padx=15)

#Play Button
def play():
    global lvl
    j = lvl.get() 
    if j == "1":
        level1.start(type.get()) # Para los tipos de imágenes poner en la función start un argumento, que en el archivo de lvl 1 haga que cambie la lista de las imagenes que se estan usando
    if j == "2":
        level2.start(type.get())
    if j == "3":
        level3.start(type.get())
    
fame_btn = Button(win, text="Jugar", width=15, height=4, command=play)
fame_btn.grid(row=3, column=0, columnspan=2, padx=15)

#Add Records to database

win.mainloop()

    
