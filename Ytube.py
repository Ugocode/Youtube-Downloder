from tkinter import *
import pytube
from tkinter import ttk

win = Tk()
win.title( 'Youtube downloader')
win.geometry('522x600')
win.iconbitmap('yt.ico') # This changes the icon of the tkinter window
win.config(bg = 'red')

#add an image
photo1 = PhotoImage(file = 'youtube-logo.png')
Label(win, image = photo1, bg = 'red').grid(row=0, column=0)

url = ' '

def click():
    url = entry.get()
    video = pytube.YouTube(url)
    youtube = video.streams.first()
    youtube.download(r'C:\Users\Ugoboss\Desktop\Youtube')


label1 = Label(win, text = 'Download YouTube Videos', fg = 'green', bg = 'red', font = ('Ariel', 16, 'bold'))
label1.grid(row = 1, column = 0, padx = 25, ipady = 10)

label2 = Label(win, text = 'Enter Video URL below :')
label2.grid(row = 2, column = 0, padx = 25)

entry = Entry(win, width = 48)
entry.grid(row = 3, column = 0, padx = 3, columnspan = 5)

label3 = Label(win, text = ' ', bg = 'red')
label3.grid(row = 4, column = 0)

#Download button
btn = ttk.Button(win, text = 'Download', command = click)
btn.grid(row = 5, column = 0, ipadx = 5)



# Copywrite:
label2 = Label(win, text = '\n\n\n Made by @Ugocode', bg = 'red')
label2.grid(row = 7, column = 0)


win.mainloop()
