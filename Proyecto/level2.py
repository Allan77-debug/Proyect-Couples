from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
import sqlite3
import keyboard

fullscreen = False
def start(t, name):
    root = Toplevel()
    root.title("NIVEL 2")
    root.geometry("1250x720")
    root.attributes("-fullscreen", False)
    root.iconbitmap("Images/Logo.ico")
    root.resizable(width=True, height=True)

    def toggle_fullscreen():
        global fullscreen
        fullscreen = not fullscreen
        root.attributes("-fullscreen", fullscreen)

    toggle_fullscreen()


    # Database
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS PlayerData2 (
            name TEXT,
            time REAL, 
            tries REAL,
            level TEXT)""")

    # Timer
    start_time = time.time()

    def update_timer():
        nonlocal start_time
        elapsed_time = time.time() - start_time
        timer_label.config(text=f"Tiempo: {int(elapsed_time)} segundos")
        root.after(1000, update_timer)

    timer_label = Label(root, text="Tiempo: 0 segundos", font=("Helvetica", 16))
    timer_label.grid(row=0, column=0, columnspan=6, sticky="ew")
    update_timer()

    # Images
    if t == "1":
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 1.jpg").resize((225, 155)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 2.jpg").resize((225, 155)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 3.jpg").resize((225, 155)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 4.jpg").resize((225, 155)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 5.jpg").resize((225, 155)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 6.jpg").resize((225, 155)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 7.jpg").resize((225, 155)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 8.jpg").resize((225, 155)))
        img9 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 9.jpg").resize((225, 155)))
        img10 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 10.jpg").resize((225, 155)))
        img11 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 11.jpg").resize((225, 155)))
        img12 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 12.jpg").resize((225, 155)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((225, 155)))

    elif t == "2":
        img1 = ImageTk.PhotoImage(Image.open("Images/superheroes/Ant-man.jpg").resize((225, 155)))
        img2 = ImageTk.PhotoImage(Image.open("Images/superheroes/Black-Widow.jpg").resize((225, 155)))
        img3 = ImageTk.PhotoImage(Image.open("Images/superheroes/Capitan-America.jpg").resize((225, 155)))
        img4 = ImageTk.PhotoImage(Image.open("Images/superheroes/Capitana-Marvel.jpg").resize((225, 155)))
        img5 = ImageTk.PhotoImage(Image.open("Images/superheroes/Doctor-Strange.jpg").resize((225, 155)))
        img6 = ImageTk.PhotoImage(Image.open("Images/superheroes/Gamora.jpg").resize((225, 155)))
        img7 = ImageTk.PhotoImage(Image.open("Images/superheroes/Hulk.jpg").resize((225, 155)))
        img8 = ImageTk.PhotoImage(Image.open("Images/superheroes/Iron-Man.jpg").resize((225, 155)))
        img9 = ImageTk.PhotoImage(Image.open("Images/superheroes/Pantera-Negra.jpg").resize((225, 155)))
        img10 = ImageTk.PhotoImage(Image.open("Images/superheroes/Spiderman.jpg").resize((225, 155)))
        img11 = ImageTk.PhotoImage(Image.open("Images/superheroes/Starlord.jpg").resize((225, 155)))
        img12 = ImageTk.PhotoImage(Image.open("Images/superheroes/Thor.jpg").resize((225, 155)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((225, 155)))

    elif t == "3":
        img1 = ImageTk.PhotoImage(Image.open("Images/Animales/Capybara.jpg").resize((225,155)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Animales/Cocodrilo.jpg").resize((225, 155)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Animales/Coyote.jpg").resize((225, 155)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Animales/Iguana.jpg").resize((225, 155)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Animales/Leon.jpg").resize((225, 155)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Animales/Mono.jpg").resize((225, 155)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Animales/Pinguino.jpg").resize((225, 155)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Animales/Tigre.jpg").resize((225, 155)))
        img9 = ImageTk.PhotoImage(Image.open("Images/Animales/aguila.jpg").resize((225, 155)))
        img10 = ImageTk.PhotoImage(Image.open("Images/Animales/elefante.jpg").resize((225, 155)))
        img11 = ImageTk.PhotoImage(Image.open("Images/Animales/hipopotamo.jpg").resize((225, 155)))
        img12 = ImageTk.PhotoImage(Image.open("Images/Animales/sapo.jpg").resize((225, 155)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((225, 155)))

    all_images = [qmark, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12]
    images = [qmark]

    while len(images) < 25:
        j = random.randint(1, 24)
        if images.count(all_images[j]) < 2:
            images.append(all_images[j])


    img_frame = Frame(root, relief=SUNKEN)  # Elimina las dimensiones iniciales
    img_frame.grid(row=1, column=1, rowspan=5, sticky="nsew")
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Configuración de gestión de geometría para el frame de imágenes
    for i in range(4):
        img_frame.grid_rowconfigure(i, weight=1)
        img_frame.grid_columnconfigure(i, weight=1)

    Imgbtn1 = Button(img_frame, image=qmark, command=lambda: uncover(1),bg="#99DBE3")
    Imgbtn2 = Button(img_frame, image=qmark, command=lambda: uncover(2),bg="#99DBE3")
    Imgbtn3 = Button(img_frame, image=qmark, command=lambda: uncover(3),bg="#99DBE3")
    Imgbtn4 = Button(img_frame, image=qmark, command=lambda: uncover(4),bg="#99DBE3")
    Imgbtn5 = Button(img_frame, image=qmark, command=lambda: uncover(5),bg="#99DBE3")
    Imgbtn6 = Button(img_frame, image=qmark, command=lambda: uncover(6),bg="#99DBE3")
    Imgbtn7 = Button(img_frame, image=qmark, command=lambda: uncover(7),bg="#99DBE3")
    Imgbtn8 = Button(img_frame, image=qmark, command=lambda: uncover(8),bg="#99DBE3")
    Imgbtn9 = Button(img_frame, image=qmark, command=lambda: uncover(9),bg="#99DBE3")
    Imgbtn10 = Button(img_frame, image=qmark, command=lambda: uncover(10),bg="#99DBE3")
    Imgbtn11 = Button(img_frame, image=qmark, command=lambda: uncover(11),bg="#99DBE3")
    Imgbtn12 = Button(img_frame, image=qmark, command=lambda: uncover(12),bg="#99DBE3")
    Imgbtn13 = Button(img_frame, image=qmark, command=lambda: uncover(13),bg="#99DBE3")
    Imgbtn14 = Button(img_frame, image=qmark, command=lambda: uncover(14),bg="#99DBE3")
    Imgbtn15 = Button(img_frame, image=qmark, command=lambda: uncover(15),bg="#99DBE3")
    Imgbtn16 = Button(img_frame, image=qmark, command=lambda: uncover(16),bg="#99DBE3")
    Imgbtn17 = Button(img_frame, image=qmark, command=lambda: uncover(17),bg="#99DBE3")
    Imgbtn18 = Button(img_frame, image=qmark, command=lambda: uncover(18),bg="#99DBE3")
    Imgbtn19 = Button(img_frame, image=qmark, command=lambda: uncover(19),bg="#99DBE3")
    Imgbtn20 = Button(img_frame, image=qmark, command=lambda: uncover(20),bg="#99DBE3")
    Imgbtn21 = Button(img_frame, image=qmark, command=lambda: uncover(21),bg="#99DBE3")
    Imgbtn22 = Button(img_frame, image=qmark, command=lambda: uncover(22),bg="#99DBE3")
    Imgbtn23 = Button(img_frame, image=qmark, command=lambda: uncover(23),bg="#99DBE3")
    Imgbtn24 = Button(img_frame, image=qmark, command=lambda: uncover(24),bg="#99DBE3")

    btns = [Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11,
            Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16,Imgbtn17, Imgbtn18, Imgbtn19,
            Imgbtn20, Imgbtn21, Imgbtn22, Imgbtn23, Imgbtn24, ]

    # Set Random Uncovered Button
    k = random.randint(0, 23)
    btns[k].config(image=images[k + 1])

    # Grid system for Buttons
    for i in range(6):
        for j in range(4):
            index = i * 4 + j
            btns[index].grid(row=i, column=j, sticky="nsew")
        # Ajuste específico para las últimas dos columnas
    for j in range(4, 6):
        img_frame.grid_columnconfigure(j, weight=1)
    Imgbtn1.grid(row=0, column=0)
    Imgbtn2.grid(row=1, column=0)
    Imgbtn3.grid(row=2, column=0)
    Imgbtn4.grid(row=3, column=0)
    Imgbtn5.grid(row=0, column=1)
    Imgbtn6.grid(row=1, column=1)
    Imgbtn7.grid(row=2, column=1)
    Imgbtn8.grid(row=3, column=1)
    Imgbtn9.grid(row=0, column=2)
    Imgbtn10.grid(row=1, column=2)
    Imgbtn11.grid(row=2, column=2)
    Imgbtn12.grid(row=3, column=2)
    Imgbtn13.grid(row=0, column=3)
    Imgbtn14.grid(row=1, column=3)
    Imgbtn15.grid(row=2, column=3)
    Imgbtn16.grid(row=3, column=3)
    Imgbtn17.grid(row=0, column=4)
    Imgbtn18.grid(row=1, column=4)
    Imgbtn19.grid(row=2, column=4)
    Imgbtn20.grid(row=3, column=4)
    Imgbtn21.grid(row=0, column=5)
    Imgbtn22.grid(row=1, column=5)
    Imgbtn23.grid(row=2, column=5)
    Imgbtn24.grid(row=3, column=5)

    # Point system:
    points = 0
    loses = 0
    n = 1

    # Function cover and discover

    def show(num):
        nonlocal Imgbtn1
        nonlocal Imgbtn2
        nonlocal Imgbtn3
        nonlocal Imgbtn4
        nonlocal Imgbtn5
        nonlocal Imgbtn6
        nonlocal Imgbtn7
        nonlocal Imgbtn8
        nonlocal Imgbtn9
        nonlocal Imgbtn10
        nonlocal Imgbtn11
        nonlocal Imgbtn12
        nonlocal Imgbtn13
        nonlocal Imgbtn14
        nonlocal Imgbtn15
        nonlocal Imgbtn16
        nonlocal Imgbtn17
        nonlocal Imgbtn18
        nonlocal Imgbtn19
        nonlocal Imgbtn20
        nonlocal Imgbtn21
        nonlocal Imgbtn22
        nonlocal Imgbtn23
        nonlocal Imgbtn24
        nonlocal k

        if 0 < num < 25:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            Imgbtn1.config(command=lambda: uncover(1))
            Imgbtn2.config(command=lambda: uncover(2))
            Imgbtn3.config(command=lambda: uncover(3))
            Imgbtn4.config(command=lambda: uncover(4))
            Imgbtn5.config(command=lambda: uncover(5))
            Imgbtn6.config(command=lambda: uncover(6))
            Imgbtn7.config(command=lambda: uncover(7))
            Imgbtn8.config(command=lambda: uncover(8))
            Imgbtn9.config(command=lambda: uncover(9))
            Imgbtn10.config(command=lambda: uncover(10))
            Imgbtn11.config(command=lambda: uncover(11))
            Imgbtn12.config(command=lambda: uncover(12))
            Imgbtn13.config(command=lambda: uncover(13))
            Imgbtn14.config(command=lambda: uncover(14))
            Imgbtn15.config(command=lambda: uncover(15))
            Imgbtn16.config(command=lambda: uncover(16))
            Imgbtn17.config(command=lambda: uncover(17))
            Imgbtn18.config(command=lambda: uncover(18))
            Imgbtn19.config(command=lambda: uncover(19))
            Imgbtn20.config(command=lambda: uncover(20))
            Imgbtn21.config(command=lambda: uncover(21))
            Imgbtn22.config(command=lambda: uncover(22))
            Imgbtn23.config(command=lambda: uncover(23))
            Imgbtn24.config(command=lambda: uncover(24))

            k = num - 1

    def cover(k, num):
        nonlocal Imgbtn1
        nonlocal Imgbtn2
        nonlocal Imgbtn3
        nonlocal Imgbtn4
        nonlocal Imgbtn5
        nonlocal Imgbtn6
        nonlocal Imgbtn7
        nonlocal Imgbtn8
        nonlocal Imgbtn9
        nonlocal Imgbtn10
        nonlocal Imgbtn11
        nonlocal Imgbtn12
        nonlocal Imgbtn13
        nonlocal Imgbtn14
        nonlocal Imgbtn15
        nonlocal Imgbtn16
        nonlocal Imgbtn17
        nonlocal Imgbtn18
        nonlocal Imgbtn19
        nonlocal Imgbtn20
        nonlocal Imgbtn21
        nonlocal Imgbtn22
        nonlocal Imgbtn23
        nonlocal Imgbtn24

        btns[num - 1].config(image=qmark)
        btns[num - 1].image = qmark
        btns[k].config(image=qmark)
        btns[k].image = qmark

        Imgbtn1.config(command=lambda: show(1))
        Imgbtn2.config(command=lambda: show(2))
        Imgbtn3.config(command=lambda: show(3))
        Imgbtn4.config(command=lambda: show(4))
        Imgbtn5.config(command=lambda: show(5))
        Imgbtn6.config(command=lambda: show(6))
        Imgbtn7.config(command=lambda: show(7))
        Imgbtn8.config(command=lambda: show(8))
        Imgbtn9.config(command=lambda: show(9))
        Imgbtn10.config(command=lambda: show(10))
        Imgbtn11.config(command=lambda: show(11))
        Imgbtn12.config(command=lambda: show(12))
        Imgbtn13.config(command=lambda: show(13))
        Imgbtn14.config(command=lambda: show(14))
        Imgbtn15.config(command=lambda: show(15))
        Imgbtn16.config(command=lambda: show(16))
        Imgbtn17.config(command=lambda: show(17))
        Imgbtn18.config(command=lambda: show(18))
        Imgbtn19.config(command=lambda: show(19))
        Imgbtn20.config(command=lambda: show(20))
        Imgbtn21.config(command=lambda: show(21))
        Imgbtn22.config(command=lambda: show(22))
        Imgbtn23.config(command=lambda: show(23))
        Imgbtn24.config(command=lambda: show(24))

    def uncover(num):
        nonlocal start_time
        nonlocal btns
        nonlocal points
        nonlocal loses
        nonlocal Imgbtn1
        nonlocal Imgbtn2
        nonlocal Imgbtn3
        nonlocal Imgbtn4
        nonlocal Imgbtn5
        nonlocal Imgbtn6
        nonlocal Imgbtn7
        nonlocal Imgbtn8
        nonlocal Imgbtn9
        nonlocal Imgbtn10
        nonlocal Imgbtn11
        nonlocal Imgbtn12
        nonlocal Imgbtn13
        nonlocal Imgbtn14
        nonlocal Imgbtn15
        nonlocal Imgbtn16
        nonlocal Imgbtn17
        nonlocal Imgbtn18
        nonlocal Imgbtn19
        nonlocal Imgbtn20
        nonlocal Imgbtn21
        nonlocal Imgbtn22
        nonlocal Imgbtn23
        nonlocal Imgbtn24
        nonlocal k

        if 0 < num < 25 and num != k + 1:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            if images[num] == images[k + 1]:
                points += 1
                btns[num - 1].config(state=DISABLED)
                btns[k].config(state=DISABLED)

                Imgbtn1.config(command=lambda: show(1))
                Imgbtn2.config(command=lambda: show(2))
                Imgbtn3.config(command=lambda: show(3))
                Imgbtn4.config(command=lambda: show(4))
                Imgbtn5.config(command=lambda: show(5))
                Imgbtn6.config(command=lambda: show(6))
                Imgbtn7.config(command=lambda: show(7))
                Imgbtn8.config(command=lambda: show(8))
                Imgbtn9.config(command=lambda: show(9))
                Imgbtn10.config(command=lambda: show(10))
                Imgbtn11.config(command=lambda: show(11))
                Imgbtn12.config(command=lambda: show(12))
                Imgbtn13.config(command=lambda: show(13))
                Imgbtn14.config(command=lambda: show(14))
                Imgbtn15.config(command=lambda: show(15))
                Imgbtn16.config(command=lambda: show(16))
                Imgbtn17.config(command=lambda: show(17))
                Imgbtn18.config(command=lambda: show(18))
                Imgbtn19.config(command=lambda: show(19))
                Imgbtn20.config(command=lambda: show(20))
                Imgbtn21.config(command=lambda: show(21))
                Imgbtn22.config(command=lambda: show(22))
                Imgbtn23.config(command=lambda: show(23))
                Imgbtn24.config(command=lambda: show(24))

                if points == 12:
                    totaltime = round(time.time() - start_time, 2)
                    conn = sqlite3.connect("database.db")
                    c = conn.cursor()
                    c.execute("INSERT INTO PlayerData2 VALUES (:name, :time, :tries, :level)",
                              {
                                  "name": name,
                                  "time": totaltime,
                                  "tries": points + loses,
                                  "level": "Nivel 2"
                              }
                              )
                    conn.commit()
                    conn.close()
                    completed = messagebox.showinfo("FELICITACIONES",
                                                    f"HA GANADO EL JUEGO!\nNúmero de intentos: {points + loses}\nTiempo empleado: {totaltime} segundos")
                    
                    if completed == "ok":
                        root.destroy()
            else:
                loses += 1
                root.after(1000, lambda: cover(k, num))
        else:
            pass

        # Entry y Label abajo

    below = Frame(root)
    below.grid(row=5, column=0, columnspan=6, sticky="ew")
    Label(img_frame, text="Ingrese el numero de la imagen (1-24):", width=5).grid(row=4, column=0, columnspan=2, sticky="ew")
    bar = Entry(img_frame, width=5)
    bar.grid(row=4, column=2, columnspan=1, sticky="ew")

    def get_show():
        nonlocal submit
        nonlocal k
        num = int(bar.get())
        if 0 < num < 25:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]
            submit.config(command=get_uncover)
            k = num - 1

    def get_cover(k, num):
        nonlocal submit
        btns[num - 1].config(image=qmark)
        btns[num - 1].image = qmark
        btns[k].config(image=qmark)
        btns[k].image = qmark
        submit.config(command=get_show)

    def get_uncover():
        nonlocal submit
        nonlocal k
        nonlocal points
        nonlocal loses
        num = int(bar.get())

        if 0 < num < 25 and num != k + 1:
            btns[num - 1].config(image=images[num])
            btns[num - 1].image = images[num]

            if images[num] == images[k + 1]:
                points += 1
                btns[num - 1].config(state=DISABLED)
                btns[k].config(state=DISABLED)
                submit.config(command=get_show)

                if points == 12:
                    totaltime = round(time.time() - start_time, 2)
                    conn = sqlite3.connect("database.db")
                    c = conn.cursor()
                    c.execute("INSERT INTO PlayerData2 VALUES (:name, :time, :tries, :level)",
                              {
                                  "name": name,
                                  "time": totaltime,
                                  "tries": points + loses,
                                  "level": "Nivel 2"
                              }
                              )
                    conn.commit()
                    conn.close()
                    completed = messagebox.showinfo("FELICITACIONES",
                                                    f"HA GANADO EL JUEGO!\nNúmero de intentos: {points + loses}\nTiempo empleado: {totaltime} segundos")
                    if completed == "ok":
                        root.destroy()

            else:
                loses += 1
                root.after(1000, lambda: get_cover(k, num))
        else:
            pass

    submit = Button(img_frame, width=5, text="Show Image", command=get_uncover)
    submit.grid(row=4, column=3, columnspan=1, sticky="ew")

    # Ajustar configuración de geometría para reducir el espacio de la fila 5 y dar más espacio a los frames de imágenes
    root.grid_rowconfigure(1,weight=5)

    conn.commit()
    conn.close()
    def on_key_event(event):
        if keyboard.is_pressed('ctrl+f'):
            toggle_fullscreen()

    root.bind('<Key>', on_key_event)
    root.mainloop()
