import customtkinter
from customtkinter import filedialog as fd

#Use custom tkinter for a more modern look
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Create small window with a title and button allowing user to uplaod their audiofile
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Music Genre Predicter")

def file_upload():
    file_path = fd.askopenfilename()
    if file_path:
        #check file path
        print(f"File selected: {file_path}")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="MUSIC GENRE PREDICTER", font=customtkinter.CTkFont(family='Roboto', size=37))
label.pack(pady=12, padx=10)

file_button = customtkinter.CTkButton(master=frame, text="Upload File", command=file_upload)
file_button.pack(pady=12, padx=10)

root.mainloop()