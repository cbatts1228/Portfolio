from tkinter import *
from PIL import ImageTk, Image
import math
import random as rand
import time
import board
import adafruit_mpu6050
root=Tk()
root.configure(bg= 'black')
images = []
startImage = Image.open('startGame.png')
startImage = startImage.resize((600,300))
start = ImageTk.PhotoImage(startImage)
images.append(start)
randOpponentList = ["Spongebob","Mario","Goku","Batman","Spider-Man"]
randomImageList = ['sponge.png','mario.png','goku.png','bat.png','spider.png']
randomImages = []
bioList= ["Goofy little sponge guy", "It's-a-me Chris Pratt", "Kamehameha!!!", "I am vengence!", "It's just your friendly neighborhood Spider-Man"] 
defense=[3, 5, 5, 5, 5]
offense=[5, 10, 10, 10, 10]
speed = [3000, 1000, 500, 500, 500]
hintList = ["Spongebob has extremely low stats, just punch the bag and you'll win", "Mario has decent offense so try and outpace his speed", "You're not beating Goku", "Unless you are a master of martial arts you probably don't have a chance", "I hope you have super strength"]
i=0
op=0
opponent=rand.randint(0,4)
listy=[]
opx1=0
opy1=0
opx2=900
opy2=50
px1=0
py1=0
px2=900
py2=350
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def endGame(event):
    exit()

def sumSquares(x,y,z):
    return math.sqrt(pow(x,2)+pow(y,2)+pow(z,2))

def loseHealth(opponentCanvas, opponentHealthBar):
    global opx2, opx1, opy2, opy1, opponent
    x,y,z=mpu.acceleration
    movement = round(sumSquares(x,y,z),0)
    if movement>=15:
        print(movement)
        if op == 1:
            opx2-=movement
        elif op ==2:
            opx2-=(movement - 5)
        elif op == 3:
            opx2-=(movement - 5)
        elif op == 4:
            opx2-=(movement - 5)
        elif opponent == 0:
            opx2-=(movement - defense[opponent])
        elif opponent == 1:
            opx2-=(movement - defense[opponent])
        elif opponent == 2:
            opx2-=(movement - defense[opponent])
        elif opponent == 3:
            opx2-=(movement - defense[opponent])
        elif opponent == 4:
            opx2-=(movement - defense[opponent])
        
        opponentCanvas.coords(opponentHealthBar, opx1,opy1,opx2,opy2)
        print(opponentHealthBar)
        if opx2<=0:
            winScreen()
    root.after(100, lambda:loseHealth(opponentCanvas,opponentHealthBar))

def playerLoseHealth(playerCanvas,playerHealthBar):
    global px2, px1, py2, py1, opponent
    if op == 1:
        px2-= 10
        root.after(10000, lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif op ==2:
        px2-=10
        root.after(1000, lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif op == 3:
        px2-=15
        root.after(500, lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif op == 4:
        px2-=20
        root.after(500, lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif opponent == 0:
        px2-=offense[opponent]
        root.after(speed[opponent], lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif opponent == 1:
        px2-=offense[opponent]
        root.after(speed[opponent], lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif opponent == 2:
        px2-=offense[opponent]
        root.after(speed[opponent], lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif opponent == 3:
        px2-=offense[opponent]
        root.after(speed[opponent], lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    elif opponent == 4:
        px2-=offense[opponent]
        root.after(speed[opponent], lambda:playerLoseHealth(playerCanvas,playerHealthBar))
    
    playerCanvas.coords(playerHealthBar, px1,py1,px2,py2)
    print(playerHealthBar)
    if px2<=0:
        loseScreen()
        
    
#root.attributes('-fullscreen', True)
#canvas = Canvas(root, width=1920, height=1080)
#canvas.pack()

#canvas.create_text(300,100, text="Pi Fighter", fill="red",font="72")
#def gameScreen(event):
    #print("hi")

def wipeScreen():
    for widget in root.winfo_children():
        widget.destroy()


def opponentScreen(event):
    global images
    wipeScreen()
    Label(root,text="Choose Your Opponent", font = ("Broadway",20), bg = 'black', fg='red' ).grid(row=0,column=0,columnspan=5)

    paulImage = Image.open('logan.png')
    paulImage = paulImage.resize((300,500))
    paul = ImageTk.PhotoImage(paulImage)
    images.append(paul)
    paulBTN = Label(root,image=paul)
    paulBTN.bind("<Button-1>",paulScreen)
    paulBTN.grid(row=1,column=0)
    Label(root,text="Logan Paul", font = ("Broadway",20), bg='black', fg='red').grid(row=2,column=0)
    
    tateImage = Image.open('andrew.png')
    tateImage = tateImage.resize((300,500))
    tate = ImageTk.PhotoImage(tateImage)
    images.append(tate)
    tateBTN = Label(root,image=tate)
    tateBTN.bind("<Button-1>",tateScreen)
    tateBTN.grid(row=1,column=1)
    Label(root,text="Andrew Tate", font = ("Broadway",20), bg='black', fg='red').grid(row=2,column=1)
    
    tysonImage = Image.open('mike.png')
    tysonImage = tysonImage.resize((300,500))
    tyson = ImageTk.PhotoImage(tysonImage)
    images.append(tyson)
    tysonBTN = Label(root,image=tyson)
    tysonBTN.bind("<Button-1>",tysonScreen)
    tysonBTN.grid(row=1,column=2)
    Label(root,text="Mike Tyson", font = ("Broadway",20), bg='black', fg='red').grid(row=2,column=2)
    
    aliImage = Image.open('ali.png')
    aliImage = aliImage.resize((300,500))
    ali = ImageTk.PhotoImage(aliImage)
    images.append(ali)
    aliBTN = Label(root,image=ali)
    aliBTN.bind("<Button-1>",aliScreen)
    aliBTN.grid(row=1,column=3)
    Label(root,text="Muhammad Ali", font = ("Broadway",20), bg='black', fg='red').grid(row=2,column=3)
    
    randImage = Image.open('sillouette.png')
    randImage = randImage.resize((300,500))
    rand = ImageTk.PhotoImage(randImage)
    images.append(rand)
    randBTN = Label(root,image=rand)
    randBTN.bind("<Button-1>",randomFighterScreen)
    randBTN.grid(row=1,column=4)
    Label(root,text="Random Opponent", font = ("Broadway",20), bg='black', fg='red').grid(row=2,column=4)
    
    loseImage = Image.open('death.png')
    lose = ImageTk.PhotoImage(loseImage)
    images.append(lose)
    
    winImage = Image.open('win.png')
    win = ImageTk.PhotoImage(winImage)
    images.append(win)
    

def paulScreen(event):
    global images,x2,op
    op+=1
    wipeScreen()
    opponentCanvas = Canvas(root, height = 50, width = 900)
    opponentCanvas.create_rectangle(0,0,900,50, fill="red")
    opponentHealthBar = opponentCanvas.create_rectangle(0,0,900,50, fill="green")
    opponentCanvas.grid(row=0,column=0,columnspan=2)
    
    
    Label(root,image=images[1]).grid(row=1,column=0, rowspan=3)
    bio = Label(root,text= "Likes to look at dead bodies in the woods and film it", bg='black', fg='red')
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 0, Offense: 10, Speed: 1 punch/10 sec", bg='black', fg='red')
    stats.grid(row=2,column=1)
    hint = Label(root,text="Logan is very easy to beat, just hit the punching bag and you should beat him", bg='black', fg='red')
    hint.grid(row=3,column=1)
    
    playerCanvas = Canvas(root, height = 50, width = 900)
    playerCanvas.create_rectangle(0,0,900,50+300, fill="red")
    playerHealthBar = playerCanvas.create_rectangle(0,0,900,50+300, fill="green")
    playerCanvas.grid(row=4, column=0, columnspan=2)
    
    root.after(0, lambda:loseHealth(opponentCanvas, opponentHealthBar))
    root.after(0, lambda:playerLoseHealth(playerCanvas, playerHealthBar))
        
def tateScreen(event):
    global images,x2,op
    op+=2
    wipeScreen()
    opponentCanvas = Canvas(root, height = 50, width = 900)
    opponentCanvas.create_rectangle(0,0,900,50, fill="red")
    opponentHealthBar = opponentCanvas.create_rectangle(0,0,900,50, fill="green")
    opponentCanvas.grid(row=0,column=0,columnspan=2)

    Label(root,image=images[2]).grid(row=1,column=0, rowspan=3)
    bio = Label(root,text= "What color is your Bughatti? You would know if you went to Hustlers University V2.", bg='black', fg='red')
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 10, Offense: 20, Speed: 1 punch/5 sec", bg='black', fg='red')
    stats.grid(row=2,column=1)
    hint = Label(root,text="You've gotta have Top G energy to beat Tate", bg='black', fg='red')
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)
    
    playerCanvas = Canvas(root, height = 50, width = 900)
    playerCanvas.create_rectangle(0,0,900,50+300, fill="red")
    playerHealthBar = playerCanvas.create_rectangle(0,0,900,50+300, fill="green")
    playerCanvas.grid(row=4, column=0, columnspan=2)
    
    root.after(0, lambda:loseHealth(opponentCanvas, opponentHealthBar))
    root.after(0, lambda:playerLoseHealth(playerCanvas, playerHealthBar))

def tysonScreen(event):
    global images,x2,op
    op+=3
    wipeScreen()
    opponentCanvas = Canvas(root, height = 50, width = 900)
    opponentCanvas.create_rectangle(0,0,900,50, fill="red")
    opponentHealthBar = opponentCanvas.create_rectangle(0,0,900,50, fill="green")
    opponentCanvas.grid(row=0,column=0,columnspan=2)
    
    Label(root,image=images[3]).grid(row=1,column=0, rowspan=3)
    bio = Label(root,text= "My nameth isth Mike Tyson", bg='black', fg='red')
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 15, Offense: 40, Speed: 1 punch/7 sec", bg='black', fg='red')
    stats.grid(row=2,column=1)
    hint = Label(root,text="Have you tried biting his ear off?", bg='black', fg='red')
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)
    
    playerCanvas = Canvas(root, height = 50, width = 900)
    playerCanvas.create_rectangle(0,0,900,50+300, fill="red")
    playerHealthBar = playerCanvas.create_rectangle(0,0,900,50+300, fill="green")
    playerCanvas.grid(row=4, column=0, columnspan=2)
    
    root.after(0, lambda:loseHealth(opponentCanvas, opponentHealthBar))
    root.after(0, lambda:playerLoseHealth(playerCanvas, playerHealthBar))

def aliScreen(event):
    global images,x2,op
    op+=4
    wipeScreen()
    opponentCanvas = Canvas(root, height = 50, width = 900)
    opponentCanvas.create_rectangle(0,0,900,50, fill="red")
    opponentHealthBar = opponentCanvas.create_rectangle(0,0,900,50, fill="green")
    opponentCanvas.grid(row=0,column=0,columnspan=2)
    
    Label(root,image=images[4]).grid(row=1,column=0, rowspan=3)
    bio = Label(root,text= "Float like a butterfly, sting like a bee. His hands can't hit what his eyes can't see.", bg='black', fg='red')
    bio.grid(row=1,column=1)
    stats = Label(root,text="Defense: 20, Offense: 30, Speed: 1 punch/.5 sec", bg='black', fg='red')
    stats.grid(row=2,column=1)
    hint = Label(root,text="Try giving up", bg='black', fg='red')
    hint.grid(row=3,column=1)
    Button(root, text="Back", command = opponentScreen).grid(row=4,column=1)
    
    playerCanvas = Canvas(root, height = 50, width = 900)
    playerCanvas.create_rectangle(0,0,900,50+300, fill="red")
    playerHealthBar = playerCanvas.create_rectangle(0,0,900,50+300, fill="green")
    playerCanvas.grid(row=4, column=0, columnspan=2)
    
    root.after(0, lambda:loseHealth(opponentCanvas, opponentHealthBar))
    root.after(0, lambda:playerLoseHealth(playerCanvas, playerHealthBar))

def randomFighterScreen(event):
    global images,x2, opponent
    wipeScreen()
    opponentCanvas = Canvas(root, height = 50, width = 900)
    opponentCanvas.create_rectangle(0,0,900,50, fill="red")
    opponentHealthBar = opponentCanvas.create_rectangle(0,0,900,50, fill="green")
    opponentCanvas.grid(row=0,column=0,columnspan=2)
    
    randomImage = Image.open(randomImageList[opponent])
    randomImage = randomImage.resize((300,500))
    random = ImageTk.PhotoImage(randomImage)
    randomImages.append(random)
    Label(root,image=randomImages[0]).grid(row=1,column=0,rowspan=3)
    Label(root,text=randOpponentList[opponent]).grid(row=4,column=0,)
    
    bio=Label(root,text=bioList[opponent], bg='black', fg='red')
    bio.grid(row=1,column=1)
    
    stats = Label(root,text=f"Defense: {defense[opponent]}, Offense: {offense[opponent]}, Speed: {speed[opponent]/1000} sec", bg='black', fg='red')
    stats.grid(row=2,column=1)
    
    hint = Label(root,text=hintList[opponent], bg='black', fg='red')
    hint.grid(row=3,column=1)
    
    playerCanvas = Canvas(root, height = 50, width = 900)
    playerCanvas.create_rectangle(0,0,900,50+300, fill="red")
    playerHealthBar = playerCanvas.create_rectangle(0,0,900,50+300, fill="green")
    playerCanvas.grid(row=4, column=0, columnspan=2)
    
    root.after(0, lambda:loseHealth(opponentCanvas, opponentHealthBar))
    root.after(0, lambda:playerLoseHealth(playerCanvas, playerHealthBar))
        
def startScreen():
    wipeScreen()
    Label(root,text="Pi Fighter").grid(row=0,column=0)
    Label(root,text="Pi Fighter", font=("Brooklyn",100), bg='black', fg='red').grid(row=0,column=0)
    startBTN = Label(root,image=images[0],bg='black')
    startBTN.bind("<Button-1>",opponentScreen)
    startBTN.grid(row=1,column=0)

def loseScreen():
    wipeScreen()
    loseBTN = Label(root,image= images[6])
    loseBTN.bind("<Button-1>", endGame)
    loseBTN.pack()
    
def winScreen():
    wipeScreen()
    winBTN = Label(root, image = images[7])
    winBTN.bind("<Button-1>", endGame)
    winBTN.pack()
    
startScreen()

root.mainloop()
 