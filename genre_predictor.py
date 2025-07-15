import customtkinter
from customtkinter import filedialog as fd
import pygame
from pydub import AudioSegment
import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt



#Use custom tkinter for a more modern look
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Create small window with a title and button allowing user to uplaod their audio file
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Music Genre Predicter")





#Prepare audio


def prepare_audio(file_path):
    #make all audio at most 30 seconds, mono and 22050Hz sample rate and export as wav

    set_length = 30000
    sample_rate = 22050
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1).set_frame_rate(sample_rate)
    if len(audio) > set_length:
        audio = audio[:set_length]
    output_path = "processed_audio.wav"
    audio.export(output_path, format ="wav")
    
    #get new WAV file
    y, sample_rate = librosa.load(output_path)

    #create Mel spectogram
    S = librosa.feature.melspectrogram(y=y, sr=sample_rate)
    S_dB = librosa.power_to_db(S, ref = np.max)

    #plot and save spectogram
    plt.figure(figsize=(10,4))
    librosa.display.specshow(S_dB, sr=sample_rate, x_axis="time", y_axis="mel")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("spectogram.png", bbox_inches="tight", pad_inches=0)

    


#Functions for all buttons in the GUI - UPLOAD, PLAY, PAUSE/RESUME

def file_upload():
    global file_path 
    file_path = fd.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        #check file path
        print(f"File selected: {file_path}")
        processed_audio = prepare_audio(file_path)

pause = True
started = False

def play_song():
    global started
    if not started:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    
    started = True

    global pause
    if pause:
        pygame.mixer.music.unpause()
        pause = False
    else:
        pygame.mixer.music.pause()
        pause = True





#GUI

top_frame = customtkinter.CTkFrame(master=root)
top_frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=top_frame, text="MUSIC GENRE PREDICTER", font=customtkinter.CTkFont(family='Roboto', size=37))
label.pack(pady=12, padx=10)

file_button = customtkinter.CTkButton(master=top_frame, text="Upload File", command=file_upload)
file_button.pack(pady=12, padx=10)



play_button = customtkinter.CTkButton(master = top_frame, text="Play/Pause", command = play_song)
play_button.pack(pady=12, padx=10)



root.mainloop()