import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image

imgfiletype=[("jpg image","*.jpg"),("png image","*png")]

foldir=""
def getFoldir():
    foldir=filedialog.askdirectory()
    l1.config(text=foldir)
imgdir=""
def getImgdir():
    imgdir=filedialog.askopenfilename(filetypes=imgfiletype)
    l2.config(text=imgdir)
    print(imgdir)
    newImg=ImageTk.PhotoImage(Image.open(imgdir).resize((300,300)))
    limg1.configure(image=newImg)
    limg1.image=newImg
    # canvas1.itemconfig(canvas2,image=ImageTk.PhotoImage(Image.open(imgdir)))

window = tk.Tk()
window.geometry("720x480")
# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()

l1=tk.Label(window,text="no file selected",bg="lightblue",width=60,height=1)
l2=tk.Label(window,text="no file selected",bg="yellow",width=60,height=1)
l1.grid(row=0,column=1,sticky='w',columnspan=5)
l2.grid(row=1,column=1,sticky='w',columnspan=5)

# canvas1 = tk.Canvas(window,width=300,height=300)
# canvas1.grid(row=1,column=2)
# canvas2 = tk.Canvas(window,width=300,height=300)
# canvas2.grid(row=2,column=3)
img1=ImageTk.PhotoImage(Image.open("defaultImg.jpg").resize((300,300)))
# canvas1.create_image(20,20,image=img1)
img2=ImageTk.PhotoImage(Image.open("defaultImg.jpg").resize((300,300)))
# canvas2.create_image(20,20,image=img2)
limg1=tk.Label(window)
limg1.grid(row=2,column=0,sticky='w',columnspan=3,padx=10,pady=10)
limg1.config(width=300,height=300)
limg2=tk.Label(window)
limg2.grid(row=2,column=4,sticky='w',columnspan=3,padx=10,pady=10)
limg2.config(width=300,height=300)
limg1.config(image=img1)
limg2.config(image=img2)

button1=tk.Button(window,text="input folder",bg="red",justify="left")
button2=tk.Button(window,text="input image",bg="red",justify="left")
button1.config(command=lambda:getFoldir())
button2.config(command=lambda:getImgdir())
button1.grid(row=0,column=0,padx=5,pady=5)
button2.grid(row=1,column=0,padx=5,pady=5)

window.mainloop()