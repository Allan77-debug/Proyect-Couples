from tkinter import *
from PIL import Image, ImageTk
import pygame

def reproducir(win, n):
    volume = 0.5
    muted = False

    rutas = ["Música/inicial_music.wav", "Música/nivel1_music.wav", "Música/nivel2_music.wav", "Música/nivel3_music.wav"]

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(rutas[n])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

    def volume_up():
        global volume
        if volume < 1.0:
            volume += 0.1
            pygame.mixer.music.set_volume(volume)

    def volume_down():
            global volume
            if volume > 0.0:
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)

    def toggle_mute():
        global muted
        global volume
        if not muted:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(volume)
        muted = not muted

    def show_settings():
        settings_window = Toplevel(win)
        settings_window.title("Configuración de Sonido")
        settings_window.geometry("242x100")

        img_volume_up = Image.open("Música/volume_up.png").resize((30, 30), Image.BILINEAR)
        img_volume_up = ImageTk.PhotoImage(img_volume_up)

        img_volume_down = Image.open("Música/volume_down.png").resize((30, 30), Image.BILINEAR)
        img_volume_down = ImageTk.PhotoImage(img_volume_down)

        img_mute = Image.open("Música/mute.png").resize((30, 30), Image.BILINEAR)
        img_mute = ImageTk.PhotoImage(img_mute)

        Label(settings_window, text="Subir Volumen").grid(row=1, column=0)
        Label(settings_window, text="Bajar Volumen").grid(row=1, column=1)
        Label(settings_window, text="Silenciar").grid(row=1, column=2)

        volume_up_button = Button(settings_window, image=img_volume_up, command= volume_up)
        volume_down_button = Button(settings_window, image=img_volume_down, command= volume_down)
        mute_button = Button(settings_window, image=img_mute, command= toggle_mute)

        volume_up_button.grid(row=0, column=0)
        volume_down_button.grid(row=0, column=1)
        mute_button.grid(row=0, column=2)

        volume_up_button.image = img_volume_up
        volume_down_button.image = img_volume_down
        mute_button.image = img_mute


    settings_button = Button(win, text="⋮", command=show_settings)
    settings_button.place(relx=0.95, rely=0.05)

def finalizar():
    pygame.mixer.music.stop()