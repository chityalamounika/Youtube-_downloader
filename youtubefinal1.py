import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
def Widgets():

    head_label = Label(root, text="YouTube Video Downloader ",padx=15,pady=15,font="SegoeUI 14",bg="palegreen1",fg="red")
    head_label.grid(row=1,column=1,pady=10,padx=5,columnspan=3)
    
    link_label = Label(root,text="YouTube link :",bg="salmon",pady=5,padx=9)
    link_label.grid(row=2,column=0,pady=5,padx=5)
    
    root.linkText = Entry(root,width=35,textvariable=video_Link,font="Arial 14")
    root.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)
    
    destination_label = Label(root,text="Destination :",bg="salmon",pady=5,padx=9)
    destination_label.grid(row=3,column=0,pady=5,padx=5)
    
    root.destinationText = Entry(root,width=27,textvariable=download_Path,font="Arial 14")
    root.destinationText.grid(row=3,column=1,pady=5,padx=5)
    
    browse_B = Button(root,text="Browse",command=Browse,width=10,bg="bisque",relief=GROOVE)
    browse_B.grid(row=3,column=2,pady=1,padx=1)

    quality = Label(root, text="Choose Type of Quality ",padx=15,pady=15,font="SegoeUI 14",bg="palegreen1",fg="red")
    quality.grid(row=4,column=1,pady=10,padx=5,columnspan=3)
    
    best=Button(root,text="Best",command=Best1,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
    best.grid(row=5,column=1,pady=2,padx=20)
    
    worst=Button(root,text="Worst",command=Worst1,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
    worst.grid(row=5,column=2,pady=20,padx=20)
    
    audio=Button(root,text="Quality",command=Audio1,width=20,bg="thistle1",pady=10,padx=15,relief=GROOVE,font="Georgia, 13")
    audio.grid(row=5,column=3,pady=20,padx=20)
    
    Download_B = Button(root,text="Download Video",command=Download,width=20,padx=15,pady=15,font="SegoeUI 14",bg="palegreen1",fg="red")
    Download_B.grid(row=6,column=1,pady=10,padx=5,columnspan=3)

    # destination folder to save the video

def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)

# Defining Download() to download the video
def Best1():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo1 = YouTube(Youtube_link)
    
    videoStream = getVideo1.get_highest_resolution()
    videoStream.download(download_Folder)
def Worst1():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo1 = YouTube(Youtube_link)
    videoStream = getVideo1.get_lowest_resolution()
    videoStream.download(download_Folder)
def Audio1():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo1 = YouTube(Youtube_link)
    videoStream = getVideo1.get_audio_only()
    videoStream.download(download_Folder)

def Download():
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)

	videoStream = getVideo.streams.first()
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)


root = tk.Tk()
root.geometry("1020x980")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")

video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()


