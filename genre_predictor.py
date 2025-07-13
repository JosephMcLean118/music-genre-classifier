import customtkinter
from customtkinter import filedialog as fd
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
from glob import glob
import pygame



#Use custom tkinter for a more modern look
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Create small window with a title and button allowing user to uplaod their audiofile
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Music Genre Predicter")


#Functions for all buttons in the GUI - UPLOAD, PLAY, PAUSE/RESUME

def file_upload():
    global file_path 
    file_path = fd.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        #check file path
        print(f"File selected: {file_path}")

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

pause = False
def pause_song():
    global pause
    if pause:
        pygame.mixer.music.unpause()
        pause = False
    else:
        pygame.mixer.music.pause()
        pause = True

top_frame = customtkinter.CTkFrame(master=root)
top_frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=top_frame, text="MUSIC GENRE PREDICTER", font=customtkinter.CTkFont(family='Roboto', size=37))
label.pack(pady=12, padx=10)

file_button = customtkinter.CTkButton(master=top_frame, text="Upload File", command=file_upload)
file_button.pack(pady=12, padx=10)



play_button = customtkinter.CTkButton(master = top_frame, text="Play", command = play_song)
play_button.pack(pady=12, padx=10)

pause_button = customtkinter.CTkButton(master = top_frame, text="Pause/Resume", command = pause_song)
pause_button.pack(pady=12, padx=10)

root.mainloop()