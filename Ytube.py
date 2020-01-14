from tkinter import *
import pytube


win = Tk()
win.title( 'Youtube downloader')
win.geometry('320x200')
win.config(bg = 'red')

url = ' '

def click():
    url = entry.get()
    video = pytube.YouTube(url)
    youtube = video.streams.first()
    youtube.download(r'C:\Users\Ugoboss\Desktop\Youtube')


label1 = Label(win, text = 'Download YouTube Videos', fg = 'green', bg = 'red', font = ('Ariel', 16, 'bold'))
label1.grid(row = 0, column = 0, padx = 25, ipady = 10)

label2 = Label(win, text = 'Enter Video URL below :')
label2.grid(row = 1, column = 0, padx = 25)

entry = Entry(win, width = 48)
entry.grid(row = 2, column = 0, padx = 3, columnspan = 5)

label3 = Label(win, text = ' ', bg = 'red')
label3.grid(row = 3, column = 0)

btn = Button(win, text = 'Download', command = click)
btn.grid(row = 4, column = 0, ipadx = 5)


win.mainloop()
