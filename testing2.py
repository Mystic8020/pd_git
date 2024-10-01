from customtkinter import *
from tkinter import *
from PIL import ImageTk,Image
from CTkMessagebox import CTkMessagebox
from pygame import mixer
set_appearance_mode("Light")
set_default_color_theme("green")
app = CTk()
app.geometry("1000x600")
app.title("Planet Dynamics")
from pygame import mixer

mixer.init()

def play_music():
    mixer.music.play()
def stop_music():
    mixer.music.stop()
def pause_music():
    mixer.music.pause()
    b2.pack_forget()
    b3.pack()
mixer.music.load("Recording.mp3")

def unpause_music():
    mixer.music.unpause()
    b3.pack_forget()
    b2.pack()


mytab = CTkTabview(app, width = 800, height = 550)
mytab.pack(side = RIGHT, expand = True, fill = Y)
tab1 = mytab.add("Tab_1")
tab2 = mytab.add("Tab_2")
l1 = CTkLabel(tab1, text = "Hello", font=("Arial", 30))
l1.pack()
frame = CTkFrame(app, width = 200, height = 550)
frame.pack(side= LEFT, expand = True, fill = Y)
b1 = CTkButton(tab2, text="Play",command = play_music)
b1.pack()
b4 = CTkButton(tab2, text="Stop", command= stop_music)
b4.pack()
b2 = CTkButton(frame, text="Pause", command = pause_music)
b2.pack()
b3 = CTkButton(frame, text="Unpause", command = unpause_music)

b1 = CTkButton(frame, text="Hello")
b1.pack()
app.mainloop()