# battleship! in python, osrta, 1player only atm

from types import SimpleNamespace

# define board
class Board:
    def __init__(self,size):
        self.boardsize = size
        self.board = [[''] * self.boardsize for i in range(self.boardsize)]
        ship = ship
            # Help, moet aantal hits per schip opslaan, da kan neit in een tuple :(


    def printBoard(self):
        for row in self.board:
            print(row)

    def setboardelement(self,x,y,thing):
        self.board[x][y] = thing

    def getboardelement(self,x,y):
        return self.board[x][y]

    #x -1 =links
    #x +1 =rechts
    #y +1 = onder
    #y -1 = omhoog
    # Dit hierboven in 1 functie samenvatten

    def check_heading(self, h, sx, sy):
        if h == "u":
            sy += 1
        if h == "d":
            sy -= 1
        if h == "l":
            sx -= 1
        if h == "r":
            sx += 1
        return sx, sy

    #TODO: add orientation, heading
    def setShip(self,x,y,s,h):
        lenship = 5
        shipchar = s
        sx = x
        sy = y
        if sy + lenship > self.boardsize or sy + lenship > self.boardsize or sx + lenship > self.boardsize or sx - lenship > self.boardsize:
            print("Cant fit ship on board!")
        # check if other boat is placed already
        if self.getboardelement(sx,sy) != '':
            print(f"Already occupied by ship: {self.getboardelement(sx,sy)}!")
        else:
            # place n chars up, starting at location x,y
            for i in range(0,lenship):
                self.setboardelement(sx,sy,shipchar)
                sx, sy = self.check_heading(h, sx, sy)

    def strike(self,x,y):
        self.checkmove(x, y)

    def win(self):
        if sum([item[2] for item in self.ships]):
            print("You won!")


    def checkmove(self, x, y):
        strikechar = 'x'
        misschar = 'm'
        # check if hit:
        if self.getboardelement(x, y) in [item[1] for item in self.ships]:
            self.setboardelement(x, y, strikechar)
            print("Hit!")
        if self.getboardelement(x, y) == strikechar:
            print(f"already struck {x},{y}!!")
        else:
            self.setboardelement(x, y, misschar)
            print("Miss!")


zeeslagje = Board(10)
zeeslagje.setShip(4, 5, 'B', 'u')
print(zeeslagje.printBoard())
