from tkinter import *
import tkinter as tk
from tkinter import filedialog,font
from pygame import mixer


class MP:
    def __init__(self, win):
        win.geometry('300x300')
        win.title('MP3 PLAYER')
        win.resizable(0, 0)   


        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')
        #1st button
        load_button = Button(win, text='Add', width=10, font=('Times', 20),bg="Dodgerblue2", relief='sunken',fg="white", command=self.load)
        load_button.place(x=150, y=40, anchor='center')
        #2nd button
        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Times', 20), bg='Dodgerblue2', relief='sunken',fg="white", command=self.play)
        play_button.place(x=150, y=80, anchor='center')
        #3rd button
        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Times', 20),bg='Dodgerblue2', relief='sunken',fg="white", command=self.pause)
        pause_button.place(x=150, y=120, anchor='center')
        #4th button
        stop_button = Button(win, text='Stop', width=10, font=('Times', 20),bg='Dodgerblue2', relief='sunken',fg="white", command=self.stop)
        stop_button.place(x=150, y=160, anchor='center')
        #condition which help to actual working
        self.music_file = False
        self.playing_state = False
    
    # 1st function which help to taking the song file
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')
    #2nd fuuction which help to paly the given song
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')
    #3rd function which help pasue the palying song
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')
    #4th function which stop the song
    def stop(self):
        mixer.music.stop()
MP(Tk())
Tk().mainloop()
