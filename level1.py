from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
k = 0

def run_memory_game():
    game_window = Tk()
    game_window.title("NIVEL 1")
    game_window.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    game_window.iconbitmap(r"C:\Users\juanr\Downloads\Proyecto\images\Logo.ico")

    # Agregar evento para salir de pantalla completa con la tecla Esc
    game_window.bind("<Escape>", lambda e: game_window.attributes("-fullscreen", False))


    #Imágenes xd

    img1 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 1.jpg").resize((250, 150)))
    img2 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\images\Paisaje 2.jpg").resize((250, 150)))
    img3 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 3.jpg").resize((250, 150)))
    img4 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 4.jpg").resize((250, 150)))
    img5 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 5.jpg").resize((250, 150)))
    img6 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 6.jpg").resize((250, 150)))
    img7 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 7.jpg").resize((250, 150)))
    img8 = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\Paisaje 8.jpg").resize((250, 150)))
    qmark = ImageTk.PhotoImage(Image.open(r"E:\UNI\Proyecto\Images\questionmark.jpg").resize((250, 150)))

    all_images = [qmark, img1, img2, img3, img4, img5, img6, img7, img8, img1, img2, img3, img4, img5, img6, img7, img8]
    images = [qmark]

    while len(images) < 17:
        j = random.randint(1, 16)
        if images.count(all_images[j]) < 2:
            images.append(all_images[j])

    # Frame de Imágenes y Botones
    img_frame = Frame(game_window, width=100, height=100, relief=SUNKEN)
    img_frame.grid(row=0, column=0)

    Imgbtn1 = Button(img_frame, image=qmark, command=lambda: descubrir(1))
    Imgbtn2 = Button(img_frame, image=qmark, command=lambda: descubrir(2))
    Imgbtn3 = Button(img_frame, image=qmark, command=lambda: descubrir(3))
    Imgbtn4 = Button(img_frame, image=qmark, command=lambda: descubrir(4))
    Imgbtn5 = Button(img_frame, image=qmark, command=lambda: descubrir(5))
    Imgbtn6 = Button(img_frame, image=qmark, command=lambda: descubrir(6))
    Imgbtn7 = Button(img_frame, image=qmark, command=lambda: descubrir(7))
    Imgbtn8 = Button(img_frame, image=qmark, command=lambda: descubrir(8))
    Imgbtn9 = Button(img_frame, image=qmark, command=lambda: descubrir(9))
    Imgbtn10 = Button(img_frame, image=qmark, command=lambda: descubrir(10))
    Imgbtn11 = Button(img_frame, image=qmark, command=lambda: descubrir(11))
    Imgbtn12 = Button(img_frame, image=qmark, command=lambda: descubrir(12))
    Imgbtn13 = Button(img_frame, image=qmark, command=lambda: descubrir(13))
    Imgbtn14 = Button(img_frame, image=qmark, command=lambda: descubrir(14))
    Imgbtn15 = Button(img_frame, image=qmark, command=lambda: descubrir(15))
    Imgbtn16 = Button(img_frame, image=qmark, command=lambda: descubrir(16))

    btns = [Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12,
            Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16, ]

    # Configurar botón aleatorio descubierto
    k = random.randint(0, 15)
    btns[k].config(image=images[k + 1])

    # Sistema de cuadrícula para los botones
    Imgbtn1.grid(row=0, column=0)
    Imgbtn2.grid(row=0, column=1)
    Imgbtn3.grid(row=0, column=2)
    Imgbtn4.grid(row=0, column=3)
    Imgbtn5.grid(row=1, column=0)
    Imgbtn6.grid(row=1, column=1)
    Imgbtn7.grid(row=1, column=2)
    Imgbtn8.grid(row=1, column=3)
    Imgbtn9.grid(row=2, column=0)
    Imgbtn10.grid(row=2, column=1)
    Imgbtn11.grid(row=2, column=2)
    Imgbtn12.grid(row=2, column=3)
    Imgbtn13.grid(row=3, column=0)
    Imgbtn14.grid(row=3, column=1)
    Imgbtn15.grid(row=3, column=2)
    Imgbtn16.grid(row=3, column=3)

    # Sistema de puntos
    puntos = 0
    perdidas = 0
    n = 1


    # Funciones de descubrir y cubrir
    def mostrar(num):
        nonlocal Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16, k
        if 0 < num < 17:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            Imgbtn1.config(command=lambda: descubrir(1))
            Imgbtn2.config(command=lambda: descubrir(2))
            Imgbtn3.config(command=lambda: descubrir(3))
            Imgbtn4.config(command=lambda: descubrir(4))
            Imgbtn5.config(command=lambda: descubrir(5))
            Imgbtn6.config(command=lambda: descubrir(6))
            Imgbtn7.config(command=lambda: descubrir(7))
            Imgbtn8.config(command=lambda: descubrir(8))
            Imgbtn9.config(command=lambda: descubrir(9))
            Imgbtn10.config(command=lambda: descubrir(10))
            Imgbtn11.config(command=lambda: descubrir(11))
            Imgbtn12.config(command=lambda: descubrir(12))
            Imgbtn13.config(command=lambda: descubrir(13))
            Imgbtn14.config(command=lambda: descubrir(14))
            Imgbtn15.config(command=lambda: descubrir(15))
            Imgbtn16.config(command=lambda: descubrir(16))

            k = num - 1
        else:
            pass


    def cubrir(k, num):
        nonlocal Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16
        btns[num - 1].config(image=qmark)
        btns[num - 1].image = qmark
        btns[k].config(image=qmark)
        btns[k].image = qmark

        Imgbtn1.config(command=lambda: mostrar(1))
        Imgbtn2.config(command=lambda: mostrar(2))
        Imgbtn3.config(command=lambda: mostrar(3))
        Imgbtn4.config(command=lambda: mostrar(4))
        Imgbtn5.config(command=lambda: mostrar(5))
        Imgbtn6.config(command=lambda: mostrar(6))
        Imgbtn7.config(command=lambda: mostrar(7))
        Imgbtn8.config(command=lambda: mostrar(8))
        Imgbtn9.config(command=lambda: mostrar(9))
        Imgbtn10.config(command=lambda: mostrar(10))
        Imgbtn11.config(command=lambda: mostrar(11))
        Imgbtn12.config(command=lambda: mostrar(12))
        Imgbtn13.config(command=lambda: mostrar(13))
        Imgbtn14.config(command=lambda: mostrar(14))
        Imgbtn15.config(command=lambda: mostrar(15))
        Imgbtn16.config(command=lambda: mostrar(16))


    def descubrir(num):
        nonlocal btns, puntos, perdidas, Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16, k
        if 0 < num < 17 and num != k + 1:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            if images[num] == images[k + 1]:
                puntos += 1
                btns[num - 1].config(state=DISABLED)
                btns[k].config(state=DISABLED)

                Imgbtn1.config(command=lambda: mostrar(1))
                Imgbtn2.config(command=lambda: mostrar(2))
                Imgbtn3.config(command=lambda: mostrar(3))
                Imgbtn4.config(command=lambda: mostrar(4))
                Imgbtn5.config(command=lambda: mostrar(5))
                Imgbtn6.config(command=lambda: mostrar(6))
                Imgbtn7.config(command=lambda: mostrar(7))
                Imgbtn8.config(command=lambda: mostrar(8))
                Imgbtn9.config(command=lambda: mostrar(9))
                Imgbtn10.config(command=lambda: mostrar(10))
                Imgbtn11.config(command=lambda: mostrar(11))
                Imgbtn12.config(command=lambda: mostrar(12))
                Imgbtn13.config(command=lambda: mostrar(13))
                Imgbtn14.config(command=lambda: mostrar(14))
                Imgbtn15.config(command=lambda: mostrar(15))
                Imgbtn16.config(command=lambda: mostrar(16))

                if puntos == 8:
                    completado = messagebox.showinfo("FELICITACIONES",
                                                     "HA GANADO EL JUEGO!\nNúmero de intentos: {}".format(perdidas))
                    if completado == "ok":
                        game_window.quit()
            else:
                perdidas += 1
                game_window.after(1000, lambda: cubrir(k, num))
        else:
            pass


    # Entrada y Etiqueta abajo
    abajo = Frame(game_window)
    abajo.grid(row=4, column=0)
    Label(img_frame, text="Ingrese el número de la imagen (1-16):", width=5).grid(row=4, column=0, columnspan=2,
                                                                                  sticky="ew")
    bar = Entry(img_frame, width=5)
    bar.grid(row=4, column=2, columnspan=1, sticky="ew")


    def obtener_mostrar():
        global submit
        global k
        num = int(bar.get())
        if 0 < num < 17:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]
            submit.config(command=obtener_descubrir)
            k = num - 1


    def obtener_cubrir(k, num):
        global submit
        btns[num - 1].config(image=qmark)
        btns[num - 1].image = qmark
        btns[k].config(image=qmark)
        btns[k].image = qmark
        submit.config(command=obtener_mostrar)


    def obtener_descubrir():
        global submit
        global k
        global puntos
        global perdidas
        num = int(bar.get())

        if 0 < num < 17 and num != k + 1:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            if images[num] == images[k + 1]:
                puntos += 1
                btns[num - 1].config(state=DISABLED)
                btns[k].config(state=DISABLED)
                submit.config(command=obtener_mostrar)

                if puntos == 8:
                    completado = messagebox.showinfo("FELICITACIONES",
                                                     "HA GANADO EL JUEGO!\nNúmero de intentos: {}".format(perdidas))
                    if completado == "ok":
                        game_window.quit()

            else:
                perdidas += 1
                game_window.after(1000, lambda: obtener_cubrir(k, num))
        else:
            pass


    submit = Button(img_frame, width=5, text="Mostrar Imagen", command=obtener_descubrir)
    submit.grid(row=4, column=3, columnspan=1, sticky="ew")


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

