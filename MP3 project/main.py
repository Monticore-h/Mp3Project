# importing libraries
import os
from tkinter import *
from tkinter import filedialog
from pygame.mixer import music

from pygame import mixer

root = Tk()

root.title('Music Player')  # Title of the Player :
root.geometry("360x640")
root.configure(bg="White")
root.resizable(False, False)

mixer.init()


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith('.mp3'):
                playlist.insert(END, song)


def play_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    music.load(music_name)
    music.play()


# button
play_button = PhotoImage(file='play.png')
Button(image=play_button, fg='White', bg='white', bd=0, relief=SUNKEN, command=play_song).place(x=145, y=400)

pause_button = PhotoImage(file='pause.png')
Button(image=pause_button, fg='white', bg='white', bd=0, relief=SUNKEN, command=mixer.music.pause).place(x=220, y=400)

stop_button = PhotoImage(file='stop.png')
Button(image=stop_button, fg='white', bg='white', bd=0, relief=SUNKEN, command=mixer.music.stop).place(x=145, y=470)

resume_button = PhotoImage(file='resume.png')
Button(image=resume_button, fg='white', bg='white', bd=0, relief=SUNKEN, command=mixer.music.unpause).place(x=60, y=400)

# music frame
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=0, y=100, height=250, width=500)

Button(root, text="Select Songs", width=15, height=2, font=("arial", 10, "bold"), fg="black", bg="light blue",
       command=open_folder).place(x=10, y=50)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=500, height=100, font=("arial", 10), bg="light grey", fg="grey",
                   selectbackground="light blue", cursor="hand2",
                   yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(fill=Y)
playlist.pack(fill=BOTH)

root.mainloop()
