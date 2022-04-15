## Library for the gui development 
from tkinter import *
## Library for the Youtube Download 
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader", )
root.iconbitmap("C:\Portofolio\Python.Py\YoutubeDownloader.py\Photos")
root.minsize(400,200)


Description = Entry(root, width = 50, bg = "white", fg = "black")   # type Box 
describe = Label(text = "Give Us The Url :") # Message for the user to give us the url 
describe.pack(side = TOP)
Description.pack(side = TOP)


def Video_Details():
    myLabel = Label(root, text = "Look i clicked a button !")
    myLabel.pack()

# function that downloads the video 
def Video_Downlaoder(): 
    link = Description.get()                    # Gets the Link from the type Box 
    yt = YouTube(link) 
    ys = yt.streams.get_highest_resolution()    # It downloads on tthe highest possible resolution
    ys.download('/Users/azlatan/Downloads')     # Location where the File is downloading and Download Command
    downloading_label = Label(root, text = "Download Completed ...")
    downloading_label.pack()
    
# Prints Whatever is in the type Box
def Printer():
    txt = Description.get()
    print(txt)


myButton = Button(root, text = "Click to download", command = Video_Downlaoder) # Button for Downloader Function
printer_button = Button(text = 'Print', command = Printer)  # Button for printer function 
Button_quit = Button(root, text="Quit", command = root.destroy) # Button for terminating the programm
myButton.pack()
Button_quit.pack()
printer_button.pack()


# For not terminating the window after Complete
root.mainloop()