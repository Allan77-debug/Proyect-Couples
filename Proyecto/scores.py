from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import tkinter.font as tkFont

def scores():
    scores_win = Toplevel()
    scores_win.title("Puntuuaciones")
    scores_win.geometry("480x580")
    scores_win.resizable(width=True, height=True)
    scores_win.config(bg="#DC8787")
    scores_win.attributes("-fullscreen", False)

    color = "#DC8787"

    #Functions
    def close():
        scores_win.destroy()

    # Connect to database
    conn = sqlite3.connect("database.db")
    c = conn.cursor()   

    # Title
    fontTitle = tkFont.Font(size=40, family="Rockwell")
    title = Label(scores_win, text="Puntuaciones", font=fontTitle, bg=color, anchor="center", padx=0, pady=30)
    title.grid(column=0, row=0, columnspan=9, sticky="ew")

    # Close window
    btn_salir = Button(scores_win, text="Volver al menú", command=close, bg="#FFFFFF", highlightthickness=0, bd=0, width=15, height=2)
    btn_salir.grid(column=0, row=4, columnspan=9)

    # Font
    info_font = tkFont.Font(size=10, family="Rockwell")

    #Table for level 1
    Label(scores_win, text="Level 1", font=info_font, bg=color).grid(column=0, row=1, columnspan=3, pady=10)
    Label(scores_win, text="Nombre:", bg=color).grid(column=0, row=2)
    Label(scores_win, text="Tiempo:", bg=color).grid(column=1, row=2)
    Label(scores_win, text="Intentos:", bg=color).grid(column=2, row=2)
    frame1 = LabelFrame(scores_win, bg=color, bd=5)
    frame1.grid(row=3, column=0, columnspan=3, pady=5, padx=10)
    c.execute(f"SELECT * FROM PlayerData1")
    data1 = c.fetchall()
    data1.sort(key=lambda x: x[1])
    for i in range(len(data1)):
        for j in range(3):
            Label(frame1, font=info_font, anchor="center", text=data1[i][j], bg=color).grid(column=j, row=i, padx=10)
    
    #Table for level 2

    Label(scores_win, text="Nivel 2", bg=color, font=info_font).grid(column=3, row=1, columnspan=3, pady=10)
    Label(scores_win, text="Nombre:", bg=color).grid(column=3, row=2)
    Label(scores_win, text="Tiempo:", bg=color).grid(column=4, row=2)
    Label(scores_win, text="Intentos:", bg=color).grid(column=5, row=2)
    frame2 = LabelFrame(scores_win, bg=color, bd=5)
    frame2.grid(row=3, column=3, columnspan=3, pady=5, padx=10)
    c.execute(f"SELECT * FROM PlayerData2")
    data2 = c.fetchall()    
    data2.sort(key=lambda x: x[1])
    for i in range(len(data2)):
        for j in range(3):
            Label(frame2, font=info_font, anchor="center", text=data2[i][j], bg=color).grid(column=j, row=i, padx=10)
    
    #Table for level 3
    Label(scores_win, text="Nivel 3", font=info_font, bg=color).grid(column=6, row=1, columnspan=3, pady=10)
    Label(scores_win, text="Nombre:", bg=color).grid(column=6, row=2)
    Label(scores_win, text="Tiempo:", bg=color).grid(column=7 , row=2)
    Label(scores_win, text="Intentos:", bg=color).grid(column=8, row=2)
    frame3 = LabelFrame(scores_win, bg=color, bd=5)
    frame3.grid(row=3, column=6, columnspan=3, pady=5, padx=10)
    c.execute(f"SELECT * FROM PlayerData3")
    data3 = c.fetchall()
    data3.sort(key=lambda x: x[1])
    for i in range(len(data3)):
        for j in range(3):
            Label(frame3, font=info_font, anchor="center", text=data3[i][j], bg=color).grid(column=j, row=i, padx=10)

    conn.commit()
    conn.close()
    
    scores_win.mainloop()
