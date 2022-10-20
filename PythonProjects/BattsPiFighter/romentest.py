from tkinter import *
from PIL import ImageTk, Image

root=Tk()
#root.attributes('-fullscreen', True)
#canvas = Canvas(root, width=1920, height=1080)
#canvas.pack()

#canvas.create_text(300,100, text="Pi Fighter", fill="red",font="72")

Label(root,text="PiFighter").grid(row=0,column=0,columnspan=2)

def gameScreen(event):
    print("hi")
    
#def opponentScreen():

paulImage = Image.open('paul.png')
paulImage = paulImage.resize((300,500))
paul = ImageTk.PhotoImage(paulImage)
Label(root,image=paul).grid(row=1,column=0)
Label(root,text="Jake Paul").grid(row=2,column=0)

tateImage = Image.open('tate.png')
tateImage = tateImage.resize((300,500))
tate = ImageTk.PhotoImage(tateImage)
test = Label(root,image=tate)
test.bind("<Button-1>",gameScreen)
test.grid(row=1,column=1)
Label(root,text="Andrew Tate").grid(row=2,column=1)


#opponentScreen()
root.mainloop()