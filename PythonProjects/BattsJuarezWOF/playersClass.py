class Myplayers:    #:)
    player1=0
    player2=0
    player3=0
    
    player1Name=""
    player2Name=""
    player3Name=""
    
    def __init__ (self,name):
        self.name=name
        self.score=0
        self.bank=0

    #toString 
    def __str__(self):
        return f"{self.name}"
    
    # def getName(self):
    #     return f"{self.name}"


'''
p1 = Myplayers(0)
p1Name=Myplayers(player1Name="")
p1Name+="Bob"
print(p1Name.player1Name)

p2 = Myplayers(0)
p2Name=Myplayers(player2Name="")


p3 = Myplayers(0)
p3Name=Myplayers(player3Name="")
'''
'''
players = Myplayers()

print(players.player1Name)

players.player1Name="Joe"

print(players.player1Name)'''