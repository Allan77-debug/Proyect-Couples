from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random 
import time
import sqlite3

def start(t):
    root = Toplevel()
    root.title("NIVEL 1")
    root.geometry("1250x720")
    root.attributes("-fullscreen", False)
    root.iconbitmap("Images/Logo.ico")
    root.resizable(width=False, height=False)

    # Database
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS PlayerData (
            name TEXT,
            time REAL, 
            tries REAL)""")

    # Timer
    startime = time.time()

    # Images
    if t == "1":
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 1.jpg").resize((125, 75)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 2.jpg").resize((125, 75)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 3.jpg").resize((125, 75)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 4.jpg").resize((125, 75)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 5.jpg").resize((125, 75)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 6.jpg").resize((125, 75)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 7.jpg").resize((125, 75)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 8.jpg").resize((125, 75)))
        img9 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 9.jpg").resize((125, 75)))
        img10 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 10.jpg").resize((125, 75)))
        img11 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 11.jpg").resize((125, 75)))
        img12 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 12.jpg").resize((125, 75)))
        img13 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 13.jpg").resize((125, 75)))
        img14 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 14.jpg").resize((125, 75)))
        img15 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 15.jpg").resize((125, 75)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((125, 75)))
    elif t == "2":
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 1.jpg").resize((125, 75)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 2.jpg").resize((125, 75)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 3.jpg").resize((125, 75)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 4.jpg").resize((125, 75)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 5.jpg").resize((125, 75)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 6.jpg").resize((125, 75)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 7.jpg").resize((125, 75)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 8.jpg").resize((125, 75)))
        img9 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 9.jpg").resize((125, 75)))
        img10 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 10.jpg").resize((125, 75)))
        img11 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 11.jpg").resize((125, 75)))
        img12 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 12.jpg").resize((125, 75)))
        img13 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 13.jpg").resize((125, 75)))
        img14 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 14.jpg").resize((125, 75)))
        img15 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 15.jpg").resize((125, 75)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((125, 75)))
    elif t == "3":  
        img1 = ImageTk.PhotoImage(Image.open("Images/Animales/Capybara.jpg").resize((175, 125)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Animales/Cocodrilo.jpg").resize((175, 125)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Animales/Coyote.jpg").resize((175, 125)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Animales/Iguana.jpg").resize((175, 125)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Animales/Leon.jpg").resize((175, 125)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Animales/Mono.jpg").resize((175, 125)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Animales/Pinguino.jpg").resize((175, 125)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Animales/Tigre.jpg").resize((175, 125)))
        img9 = ImageTk.PhotoImage(Image.open("Images/Animales/aguila.jpg").resize((175, 125)))
        img10 = ImageTk.PhotoImage(Image.open("Images/Animales/elefante.jpg").resize((175, 125)))
        img11 = ImageTk.PhotoImage(Image.open("Images/Animales/hipopotamo.jpg").resize((175, 125)))
        img12 = ImageTk.PhotoImage(Image.open("Images/Animales/sapo.jpg").resize((175, 125)))
        img13 = ImageTk.PhotoImage(Image.open("Images/Animales/oso.jpg").resize((175, 125)))
        img14 = ImageTk.PhotoImage(Image.open("Images/Animales/zorro.jpg").resize((175, 125)))
        img15 = ImageTk.PhotoImage(Image.open("Images/Animales/jirafa.jpg").resize((175, 125)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((175, 125)))

    all_images = [qmark, img1, img2, img3, img4, img5, img6, img7, img8, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img1, img2, img3, img4, img5, img6, img7, img8, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15]
    images = [qmark]

    while len(images) < 31:
        j = random.randint(1, 30)
        if images.count(all_images[j]) < 2:
            images.append(all_images[j])

    # Images Frame and Buttons

    img_frame = Frame(root, width=100, height=100, relief=SUNKEN)
    img_frame.grid(row=0, column=0)

    Imgbtn1 = Button(img_frame, image=qmark, command=lambda:uncover(1))
    Imgbtn2 = Button(img_frame, image=qmark, command=lambda: uncover(2))
    Imgbtn3 = Button(img_frame, image=qmark, command=lambda: uncover(3))
    Imgbtn4 = Button(img_frame, image=qmark, command=lambda: uncover(4))
    Imgbtn5 = Button(img_frame, image=qmark, command=lambda: uncover(5))
    Imgbtn6 = Button(img_frame, image=qmark, command=lambda: uncover(6))
    Imgbtn7 = Button(img_frame, image=qmark, command=lambda: uncover(7))
    Imgbtn8 = Button(img_frame, image=qmark, command=lambda: uncover(8))
    Imgbtn9 = Button(img_frame, image=qmark, command=lambda: uncover(9))
    Imgbtn10 = Button(img_frame, image=qmark, command=lambda: uncover(10))
    Imgbtn11 = Button(img_frame, image=qmark, command=lambda: uncover(11))
    Imgbtn12 = Button(img_frame, image=qmark, command=lambda: uncover(12))
    Imgbtn13 = Button(img_frame, image=qmark, command=lambda: uncover(13))
    Imgbtn14 = Button(img_frame, image=qmark, command=lambda: uncover(14))
    Imgbtn15 = Button(img_frame, image=qmark, command=lambda: uncover(15))
    Imgbtn16 = Button(img_frame, image=qmark, command=lambda: uncover(16))
    Imgbtn17 = Button(img_frame, image=qmark, command=lambda: uncover(17))
    Imgbtn18 = Button(img_frame, image=qmark, command=lambda: uncover(18))
    Imgbtn19 = Button(img_frame, image=qmark, command=lambda: uncover(19))
    Imgbtn20 = Button(img_frame, image=qmark, command=lambda: uncover(20))
    Imgbtn21 = Button(img_frame, image=qmark, command=lambda: uncover(21))
    Imgbtn22 = Button(img_frame, image=qmark, command=lambda: uncover(22))
    Imgbtn23 = Button(img_frame, image=qmark, command=lambda: uncover(23))
    Imgbtn24 = Button(img_frame, image=qmark, command=lambda: uncover(24))
    Imgbtn25 = Button(img_frame, image=qmark, command=lambda: uncover(25))
    Imgbtn26 = Button(img_frame, image=qmark, command=lambda: uncover(26))
    Imgbtn27 = Button(img_frame, image=qmark, command=lambda: uncover(27))
    Imgbtn28 = Button(img_frame, image=qmark, command=lambda: uncover(28))
    Imgbtn29 = Button(img_frame, image=qmark, command=lambda: uncover(29))
    Imgbtn30 = Button(img_frame, image=qmark, command=lambda: uncover(30))

    btns = [Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16, Imgbtn17, Imgbtn18, Imgbtn19, Imgbtn20, Imgbtn21, Imgbtn22, Imgbtn23, Imgbtn24, Imgbtn25, Imgbtn26, Imgbtn27, Imgbtn28, Imgbtn29, Imgbtn30,]

    # Set Random Uncovered Button
    k = random.randint(0, 29)
    btns[k].config(image=images[k + 1])

    # Grid system for Buttons
    Imgbtn1.grid(row=0, column=0)
    Imgbtn2.grid(row=0, column=1)
    Imgbtn3.grid(row=0, column=2)
    Imgbtn4.grid(row=0, column=3)
    Imgbtn5.grid(row=0, column=4)
    Imgbtn6.grid(row=0, column=5)
    Imgbtn7.grid(row=1, column=0)
    Imgbtn8.grid(row=1, column=1)
    Imgbtn9.grid(row=1, column=2)
    Imgbtn10.grid(row=1, column=3)
    Imgbtn11.grid(row=1, column=4)
    Imgbtn12.grid(row=1, column=5)
    Imgbtn13.grid(row=2, column=0)
    Imgbtn14.grid(row=2, column=1)
    Imgbtn15.grid(row=2, column=2)
    Imgbtn16.grid(row=2, column=3)
    Imgbtn17.grid(row=2, column=4)
    Imgbtn18.grid(row=2, column=5)
    Imgbtn19.grid(row=3, column=0)
    Imgbtn20.grid(row=3, column=1)
    Imgbtn21.grid(row=3, column=2)
    Imgbtn22.grid(row=3, column=3)
    Imgbtn23.grid(row=3, column=4)
    Imgbtn24.grid(row=3, column=5)
    Imgbtn25.grid(row=4, column=0)
    Imgbtn26.grid(row=4, column=1)
    Imgbtn27.grid(row=4, column=2)
    Imgbtn28.grid(row=4, column=3)
    Imgbtn29.grid(row=4, column=4)
    Imgbtn30.grid(row=4, column=5)

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
        nonlocal Imgbtn25
        nonlocal Imgbtn26
        nonlocal Imgbtn27
        nonlocal Imgbtn28
        nonlocal Imgbtn29
        nonlocal Imgbtn30
        nonlocal k

        if 0 < num < 31:
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
            Imgbtn25.config(command=lambda: uncover(25))
            Imgbtn26.config(command=lambda: uncover(26))
            Imgbtn27.config(command=lambda: uncover(27))
            Imgbtn28.config(command=lambda: uncover(28))
            Imgbtn29.config(command=lambda: uncover(29))
            Imgbtn30.config(command=lambda: uncover(30))

            k = num - 1
        else:
            pass

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
        nonlocal Imgbtn25
        nonlocal Imgbtn26
        nonlocal Imgbtn27
        nonlocal Imgbtn28
        nonlocal Imgbtn29
        nonlocal Imgbtn30

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
        Imgbtn25.config(command=lambda: show(25))
        Imgbtn26.config(command=lambda: show(26))
        Imgbtn27.config(command=lambda: show(27))
        Imgbtn28.config(command=lambda: show(28))
        Imgbtn29.config(command=lambda: show(29))
        Imgbtn30.config(command=lambda: show(30))

    def uncover(num):
        nonlocal points
        nonlocal loses
        nonlocal k
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
        nonlocal Imgbtn25
        nonlocal Imgbtn26
        nonlocal Imgbtn27
        nonlocal Imgbtn28
        nonlocal Imgbtn29
        nonlocal Imgbtn30

        if 0 < num < 31 and num != k + 1:
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
                Imgbtn25.config(command=lambda: show(25))
                Imgbtn26.config(command=lambda: show(26))
                Imgbtn27.config(command=lambda: show(27))
                Imgbtn28.config(command=lambda: show(28))
                Imgbtn29.config(command=lambda: show(29))
                Imgbtn30.config(command=lambda: show(30))

                if points == 8:
                    totaltime = round(time.time() - startime, 2)
                    completed = messagebox.showinfo("FELICITACIONES", f"HA GANADO EL JUEGO!\nNúmero de intentos: {points + loses}\nTiempo empleado: {totaltime} segundos")
                    if completed == "ok":
                        root.destroy()
            else: 
                loses += 1
                root.after(1000, lambda: cover(k, num))
        else:
            pass
            

    # Entry and Label below
    below = Frame(root)
    below.grid(row=5, column=0)
    Label(img_frame, text="Enter the image number (1-16):", width=5).grid(row=5, column=0, columnspan=2, sticky="ew")
    bar = Entry(img_frame, width=5)
    bar.grid(row=5, column=2, columnspan=1, sticky="ew")

    def get_show():
        nonlocal submit
        nonlocal k
        num = int(bar.get())
        if 0 < num < 31:
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
        
        if 0 < num < 31 and num != k + 1:
            btns[num - 1].config(image=images[num]) 
            btns[num - 1].image = images[num]

            if images[num] == images[k + 1]: 
                points += 1
                btns[num - 1].config(state=DISABLED)
                btns[k].config(state=DISABLED)
                submit.config(command=get_show)

                if points == 8:
                    completed = messagebox.showinfo("FELICITACIONES", "HA GANADO EL JUEGO!\nNúmero de intentos: {}")
                    if completed == "ok":
                        root.quit()
                
            else:    
                loses += 1
                root.after(1000, lambda: get_cover(k, num))
        else: 
            pass

    submit = Button(img_frame, width=5, text="Show Image", command=get_uncover)
    submit.grid(row=5, column=3, columnspan=1, sticky="ew")
