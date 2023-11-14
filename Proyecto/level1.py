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
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 1.jpg").resize((250, 150)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 2.jpg").resize((250, 150)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 3.jpg").resize((250, 150)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 4.jpg").resize((250, 150)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 5.jpg").resize((250, 150)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 6.jpg").resize((250, 150)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 7.jpg").resize((250, 150)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisajes/Paisaje 8.jpg").resize((250, 150)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((250,150)))
    elif t == "2":
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisaje 1.jpg").resize((250, 150)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisaje 2.jpg").resize((250, 150)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisaje 3.jpg").resize((250, 150)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisaje 4.jpg").resize((250, 150)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisaje 5.jpg").resize((250, 150)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisaje 6.jpg").resize((250, 150)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisaje 7.jpg").resize((250, 150)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisaje 8.jpg").resize((250, 150)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((250,150)))
    elif t == "3":
        img1 = ImageTk.PhotoImage(Image.open("Images/Paisaje 1.jpg").resize((250, 150)))
        img2 = ImageTk.PhotoImage(Image.open("Images/Paisaje 2.jpg").resize((250, 150)))
        img3 = ImageTk.PhotoImage(Image.open("Images/Paisaje 3.jpg").resize((250, 150)))
        img4 = ImageTk.PhotoImage(Image.open("Images/Paisaje 4.jpg").resize((250, 150)))
        img5 = ImageTk.PhotoImage(Image.open("Images/Paisaje 5.jpg").resize((250, 150)))
        img6 = ImageTk.PhotoImage(Image.open("Images/Paisaje 6.jpg").resize((250, 150)))
        img7 = ImageTk.PhotoImage(Image.open("Images/Paisaje 7.jpg").resize((250, 150)))
        img8 = ImageTk.PhotoImage(Image.open("Images/Paisaje 8.jpg").resize((250, 150)))
        qmark = ImageTk.PhotoImage(Image.open("Images/questionmark.jpg").resize((250,150)))
    
    all_images = [qmark, img1, img2, img3, img4, img5, img6, img7, img8, img1, img2, img3, img4, img5, img6, img7, img8]
    images = [qmark]

    while len(images) < 17:
        j = random.randint(1, 16)
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

    btns = [Imgbtn1, Imgbtn2, Imgbtn3, Imgbtn4, Imgbtn5, Imgbtn6, Imgbtn7, Imgbtn8, Imgbtn9, Imgbtn10, Imgbtn11, Imgbtn12, Imgbtn13, Imgbtn14, Imgbtn15, Imgbtn16, ]

    # Set Random Uncovered Button
    k = random.randint(0, 15)
    btns[k].config(image=images[k + 1])

    # Grid system for Buttons
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
        nonlocal k

        if 0 < num < 17:
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

    def uncover(num):
        nonlocal startime
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
        nonlocal k

        if 0 < num < 17 and num != k + 1:
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
    below.grid(row=4, column=0)
    Label(img_frame, text="Enter the image number (1-16):", width=5).grid(row=4, column=0, columnspan=2, sticky="ew")
    bar = Entry(img_frame, width=5)
    bar.grid(row=4, column=2, columnspan=1, sticky="ew")

    def get_show():
        nonlocal submit
        nonlocal k
        num = int(bar.get())
        if 0 < num < 17:
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
        
        if 0 < num < 17 and num != k + 1:
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
    submit.grid(row=4, column=3, columnspan=1, sticky="ew")

    # Finish the game:
