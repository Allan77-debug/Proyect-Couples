from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from level1 import run_memory_game  # Asegúrate de tener esta importación correcta

def toggle_fullscreen(event=None):
    # Cambia entre pantalla completa y modo ventana
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def open_memory_game():
    # Cierra la ventana principal del menú
    root.destroy()

    # Abre la ventana del nivel 1
    run_memory_game()

def open_options():
    # Lógica para abrir la ventana de opciones
    pass

def exit_game():
    root.destroy()

# Configuración de la ventana principal del menú
root = Tk()
root.title("Menú de Juego")
root.attributes("-fullscreen", True)  # Inicia en modo pantalla completa

# Atajo de teclado: Ctrl + H para cambiar entre pantalla completa y modo ventana
root.bind("<Control-h>", toggle_fullscreen)

# Etiqueta de bienvenida
label_bienvenida = Label(root, text="¡Bienvenido al Menú de Juego!", font=("Helvetica", 30))
label_bienvenida.pack(pady=50)

# Botones del menú
btn_jugar = Button(root, text="Iniciar Juego", command=open_memory_game, height=3, width=15, font=("Helvetica", 24))
btn_jugar.pack(pady=20)

btn_opciones = Button(root, text="Opciones", command=open_options, height=3, width=15, font=("Helvetica", 24))
btn_opciones.pack(pady=20)

btn_salir = Button(root, text="Salir", command=exit_game, height=3, width=15, font=("Helvetica", 24))
btn_salir.pack(pady=20)

# Atajo de teclado: Escape para cambiar entre pantalla completa y modo ventana
root.bind("<Escape>", toggle_fullscreen)

# Finalizar el bucle de la interfaz gráfica
root.mainloop()
