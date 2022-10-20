from tkinter import *
from PIL import ImageTk, Image

root=Tk()
images = []
#root.attributes('-fullscreen', True)
#canvas = Canvas(root, width=1920, height=1080)
#canvas.pack()

#canvas.create_text(300,100, text="Pi Fighter", fill="red",font="72")
#def gameScreen(event):
    #print("hi")

def wipeScreen():
    for widget in root.winfo_children():
        widget.destroy()

def opponentScreen():
    global images
    wipeScreen()
    Label(root,text="Choose Your Opponent").grid(row=0,column=0,columnspan=4)

    paulImage = Image.open('paul.png')
    paulImage = paulImage.resize((300,500))
    paul = ImageTk.PhotoImage(paulImage)
    images.append(paul)
    paulBTN = Label(root,image=paul)
    paulBTN.bind("<Button-1>",paulScreen)
    paulBTN.grid(row=1,column=0)
    Label(root,text="Jake Paul").grid(row=2,column=0)
    
    tateImage = Image.open('tate.png')
    tateImage = tateImage.resize((300,500))
    tate = ImageTk.PhotoImage(tateImage)
    images.append(tate)
    tateBTN = Label(root,image=tate)
    tateBTN.bind("<Button-1>",tateScreen)
    tateBTN.grid(row=1,column=1)
    Label(root,text="Andrew Tate").grid(row=2,column=1)
    
    tysonImage = Image.open('tyson.png')
    tysonImage = tysonImage.resize((300,500))
    tyson = ImageTk.PhotoImage(tysonImage)
    images.append(tyson)
    tysonBTN = Label(root,image=tyson)
    tysonBTN.bind("<Button-1>",tysonScreen)
    tysonBTN.grid(row=1,column=2)
    Label(root,text="Mike Tyson").grid(row=2,column=2)
    
    aliImage = Image.open('ali.png')
    aliImage = aliImage.resize((300,500))
    ali = ImageTk.PhotoImage(aliImage)
    images.append(ali)
    aliBTN = Label(root,image=ali)
    aliBTN.bind("<Button-1>",aliScreen)
    aliBTN.grid(row=1,column=3)
    Label(root,text="Muhammad Ali").grid(row=2,column=3)

def paulScreen(event):
    global images
    wipeScreen()
    canvas = Canvas(root, height = 50, width = 900)
    canvas.create_rectangle(0,0,900,50, fill="red")
    healthBar = canvas.create_rectangle(0,0,900,50, fill="green")
    canvas.grid(row=0,column=0,columnspan=2)
    
    Label(root,image=images[0]).grid(row=1,column=0, rowspan=4)
    bio = Label(root,text= "Likes to look at dead bodies in the woods and film it")
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 0, Offense: 10, Speed: 1 punch/10 sec")
    stats.grid(row=2,column=1)
    hint = Label(root,text="Logan is very easy to beat, just hit the punching bag and you should beat him")
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)
    

def tateScreen(event):
    wipeScreen()
    canvas = Canvas(root, height = 50, width = 900)
    canvas.create_rectangle(0,0,900,50, fill="red")
    healthBar = canvas.create_rectangle(0,0,900,50, fill="green")
    canvas.grid(row=0,column=0,columnspan=2)

    Label(root,image=images[1]).grid(row=1,column=0, rowspan=4)
    bio = Label(root,text= "What color is your Bughatti? You would know if you went to Hustlers University V2.")
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 5, Offense: 20, Speed: 1 punch/5 sec")
    stats.grid(row=2,column=1)
    hint = Label(root,text="You've gotta have Top G energy to beat Tate")
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)

def tysonScreen(event):
    wipeScreen()
    canvas = Canvas(root, height = 50, width = 900)
    canvas.create_rectangle(0,0,900,50, fill="red")
    healthBar = canvas.create_rectangle(0,0,900,50, fill="green")
    canvas.grid(row=0,column=0,columnspan=2)
    
    Label(root,image=images[2]).grid(row=1,column=0, rowspan=4)
    bio = Label(root,text= "My nameth isth Mike Tyson")
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 15, Offense: 40, Speed: 1 punch/7 sec")
    stats.grid(row=2,column=1)
    hint = Label(root,text="Have you tried biting his ear off?")
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)

def aliScreen(event):
    wipeScreen()
    canvas = Canvas(root, height = 50, width = 900)
    canvas.create_rectangle(0,0,900,50, fill="red")
    healthBar = canvas.create_rectangle(0,0,900,50, fill="green")
    canvas.grid(row=0,column=0,columnspan=2)
    
    Label(root,image=images[3]).grid(row=1,column=0, rowspan=4)
    bio = Label(root,text= "Float like a butterfly, sting like a bee. His hands can't hit what his eyes can't see.")
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 50, Offense: 30, Speed: 1 punch/.5 sec")
    stats.grid(row=2,column=1)
    hint = Label(root,text="Try giving up")
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)
    
    
Label(root,text="Pi Fighter").grid(row=0,column=0)
Button(root, text="Start Game", command = opponentScreen).grid(row=1,column=0)


root.mainloop()
