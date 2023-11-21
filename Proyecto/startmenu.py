from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
import sqlite3
import level1
import level2
import level3
import scores

fullscreen = False

def on_resize(event):
    win.geometry(f"{event.width}x{event.height}")
    canvas.config(width=win.winfo_width(), height=win.winfo_height())

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        # Guardar las dimensiones originales antes de cambiar a pantalla completa
        win.original_dimensions = win.winfo_width(), win.winfo_height()
        win.attributes("-fullscreen", True)
    else:
        # Restaurar las dimensiones originales al cambiar de vuelta a la ventana
        width, height = win.original_dimensions
        win.geometry(f"{width}x{height}")
        win.attributes("-fullscreen", False)

def get_name():
    global name
    name = name_entry.get()
    name_entry.delete(0, END)

def show_scores():
    scores.scores()

def play():
    global name
    global lvl
    j = lvl.get()
    if j == "1":
        level1.start(type.get(), name)
    if j == "2":
        level2.start(type.get(), name)
    if j == "3":
        level3.start(type.get(), name)

def on_enter(event):
    event.widget.config(bg="#E8E8E8")  # Cambiar el color de fondo al entrar

def on_leave(event):
    event.widget.config(bg="#FFFFFF")  # Cambiar el color de fondo al salir

def salir():
    # Función para salir con confirmación
    respuesta = messagebox.askquestion("Salir", "¿Estás seguro de que quieres salir?")
    if respuesta == "yes":
        win.destroy()

win = Tk()
win.title("JUEGO DE PAREJAS")
win.geometry("900x525")
win.resizable(width=True, height=True)

# Configurar el color de fondo de la ventana en formato hexadecimal
win.configure(bg="#f0ebdf")  # Por ejemplo, #FFFFFF es blanco

# Connect to the database
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Load and display the background image on the canvas
background_image = Image.open("Images/fondos/fondo_menu.png")
background_image = ImageTk.PhotoImage(background_image)

# Canvas que se sobreponga sobre la ventana y ocupe todo el espacio
canvas = Canvas(win, bg="#f0ebdf", highlightthickness=0)  # Puedes especificar el color hexadecimal aquí también
canvas.grid(row=0, column=0, rowspan=7, columnspan=4, sticky="nsew")
canvas.create_image(0, 0, anchor=NW, image=background_image)

# Vincular el evento de cambio de tamaño de la ventana a la función on_resize
win.bind("<Configure>", on_resize)

# Vincular el evento de teclado Ctrl+f para alternar pantalla completa
win.bind("<Control-f>", toggle_fullscreen)

# Texto informativo sobre el atajo de teclado
font_info = tkFont.Font(size=12, family="Rockwell")
info_text = "Ctrl + F para alternar entre pantalla completa y ventana"
info_label = Label(win, text=info_text, font=font_info, bg="#f0ebdf", bd=0, highlightthickness=0)
info_label.place(relx=0.5, rely=0.26, anchor="center")

# Inicializar la variable que indica si está en pantalla completa o no
fullscreen = False

# Main Title
fontTitle = tkFont.Font(size=40, family="Rockwell")
Label(win, text="JUEGO DE PAREJAS", padx=0, pady=30, font=fontTitle, bg="#f0ebdf", bd=0, highlightthickness=0).grid(row=0, column=0, columnspan=4)

# Player name
fontName = tkFont.Font(size=15, family="Rockwell")
lbl_name = Label(win, text="Nombre:", font=fontName, bg="#f0ebdf", bd=0, highlightthickness=0)
lbl_name.grid(row=1, column=0, padx=15, pady=10)

name = ""
name_entry = Entry(win, width=80)
name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=25, pady=1)

btn_ingresar = Button(win, width=10, text="Ingresar", font=fontName, command=get_name, bg="#FFFFFF", bd=0, highlightthickness=0)
btn_ingresar.grid(row=1, column=3, columnspan=1, padx=6, sticky="ew")
btn_ingresar.bind("<Enter>", on_enter)
btn_ingresar.bind("<Leave>", on_leave)

# Levels
Label(win, text="Selecciona un nivel:", font=fontName, bg="#f0ebdf", bd=0, highlightthickness=0).grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

levels = [("Nivel 1", "1"), ("Nivel 2", "2"), ("Nivel 3", "3"), ]
lvl = StringVar()
lvl.set("None")

for n, (text, level) in enumerate(levels, start=3):
    Radiobutton(win, variable=lvl, text=text, value=level, font=fontName, bg="#f0ebdf", bd=0, highlightthickness=0).grid(row=n, column=0, columnspan=2, sticky="ew")

# Img Types
Label(win, text="Selecciona un tipo de imagen:", font=fontName, bg="#f0ebdf", bd=0, highlightthickness=0).grid(row=2, column=2, columnspan=2, sticky="ew", pady=10)

types = [("Paisajes", "1"), ("Superheroes", "2"), ("Animales", "3")]
type = StringVar()
type.set("None")

for m, (text, k) in enumerate(types, start=3):
    Radiobutton(win, variable=type, text=text, value=k, font=fontName, bg="#f0ebdf", bd=0, highlightthickness=0).grid(row=m, column=2, columnspan=2, sticky="ew")

# Scores
btn_puntuaciones = Button(win, text="Ver puntuaciones", font=fontName, width=25, height=3, command=show_scores, bg="#FFFFFF", bd=0, highlightthickness=0)
btn_puntuaciones.grid(row=6, column=2, columnspan=2, padx=15)
btn_puntuaciones.bind("<Enter>", on_enter)
btn_puntuaciones.bind("<Leave>", on_leave)

# Play Button
btn_jugar = Button(win, text="Jugar", font=fontName, width=25, height=3, command=play, bg="#FFFFFF", bd=0, highlightthickness=0)
btn_jugar.grid(row=6, column=0, columnspan=2, padx=15)
btn_jugar.bind("<Enter>", on_enter)
btn_jugar.bind("<Leave>", on_leave)

# Botón para salir
btn_salir = Button(win, text="Volver al menú", font=fontName, width=7, height=2, command=salir, bg="#FFFFFF", bd=0, highlightthickness=0)
btn_salir.grid(row=6, column=0, columnspan=4, padx=15)
btn_salir.bind("<Enter>", on_enter)
btn_salir.bind("<Leave>", on_leave)

win.mainloop()