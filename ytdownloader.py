from __future__ import unicode_literals
import subprocess
import youtube_dl
import tkinter as tk
from tkinter import Label , Button 
import tkinter.font as tkFont
import os


tkWindow = tk.Tk()  
tkWindow.geometry('400x150')
font_20 = tkFont.Font(family="Lucida Grande", size=20)
font_10 = tkFont.Font(family="Lucida Grande", size=10)
tkWindow.title('🎵 ดาวโหลดเพลง 🎵')
program_label = Label(text = "โปรเกรมโหลดเพลงจาก Youtube", font=font_20)
program_label.pack(side=tk.TOP)


def close_program():
    tkWindow.destroy()

def start_download():
    with open("music.txt", "r") as f:
        music_list = f.readlines()

    music_list = [x.strip() for x in music_list]
    for i in music_list:
        ydl_opts = {
            'outtmpl': "output/%(title)s.%(ext)s",
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])

start = Button(tkWindow,
    font=font_10,
    height = 5,
    width = 10,
	text = 'เริ่ม Download',
	command = start_download)  
start.place(relx = 0.4, rely = 0.6, anchor = tk.CENTER)

close = Button(tkWindow,
    font=font_10,
    height = 5,
    width = 10,
	text = 'ปิดโปรเกรม',
	command = close_program)  
close.place(relx = 0.65, rely = 0.6, anchor = tk.CENTER)

tkWindow.mainloop()
