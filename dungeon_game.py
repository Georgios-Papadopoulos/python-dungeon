import random
import os

level1= """
##############################################################
#..........................S>S...............................#
#........B..................S......######.####.....S.......###
###...........!....B............B..##$$..S.$##...........#####
########.................bbb.......##$$$$.$$####.......#######
##############################################################
"""

level2="""
##############################################################
#########.............E<E................SB$$#################
##############S........E....######...........SB$$$############
#####bbbb$$BbbB...........#########............BBS############
#########BSBSS..............####...#######E###......#####>####
######.!...........B...............##$$$$.E$##...#S######.####
######.............................##$$$$$$$##.###S.$$$$$$####
##############################################################
"""

level3="""
##############################################################
###########...................................################
########..........................................############
######...............##########........................#######
###..............######################....................###
####..............####################....####################
##########......######################.........###############
#######..........#######################.............#########
#####...............###########.............................##
##########..........................................F.....####
##############################################################
"""
dungeons = [level1.split(), level2.split(), level3.split()]
legend = """
------- Controls: ---------
W = up
S = down
A = left
D = right

------- Legend: ---------
@ = Player
B = Bat
S = Skorpion
E = Elephant
F = Final boss
# = Wall
b = Bread
$ = Money
! = Trader
"""
            
z= 0
player = "@"
x=1
y=1
dx = 0
dy = 0
bread = 0
money = 0
hitpoints = 100
foes =   {"B":["Bat", 3],
          "S":["Scorpion", 6],
          "E":["Elephant", 8],
          "F":["Final Boss",14]}

dungeon = dungeons[z]
testtile="."
while True:
    tile = dungeons[z][y][x]
    if tile == "b":
        bread += 1
        dungeons[z][y]= dungeons[z][y][:x]+"."+dungeons[z][y][x+1:]
    if tile == "$":
        money += 1
        dungeons[z][y]= dungeons[z][y][:x]+"."+dungeons[z][y][x+1:]
    line = dungeons[z][y][:x]+player+dungeons[z][y][x+1:]
    #os.system("clear")
    os.system('cls' if os.name=='nt' else 'clear')
    #print(line)
    ly = 0
    for line in dungeons[z]:
        if ly == y:
            print(line[:x]+player+line[x+1:])
        else:
            print(line)
        ly += 1
    command = input(" Breads: {}\n Money: {}\n Hitpoints: {}\n Dungeon level: {}\n>>>".format(bread,money,hitpoints,z+1))
    dx = 0
    dy = 0
    if command == "e" or command == "eat":
        if bread <1:
            print("You dont have bread!")
            input("Press Enter to continue\n")
        else:
            bread -= 1
            hitpoints +=2
    if command == "a":
        dx = -1
    if command == "d":
        dx = 1
    if command == "w":
        dy = -1
    if command == "s":
        dy=1
    if command == ">":
        if testtile == ">":
            z += 1
        else:
            print("Find first a stair!")
            input("Press Enter to continue\n")
            continue
    if command == "<":
        if testtile == "<":
            z -= 1
        else:
            print("Find first a stair!")
            input("Press Enter to continue")
            continue
    if command == "quit" or command == "exit":
        break
    if command =="?" or command == "help":
        os.system('cls' if os.name=='nt' else 'clear')
        print(legend)
        input("Press Enter to continue\n")
    testtile = dungeons[z][y+dy][x+dx]
    if testtile == "#":
        dx = 0
        dy = 0
    if testtile == "!":
        dx = 0
        dy = 0
        print("Welcome at the jolly bakery")
        print("how many money do you want to trade into bread?")
        amount = input("how much?\n")
        try:
            amount = int(amount)
        except:
            print("Idiot!")
            amount = -1 
        if amount > 0 and amount > money:
            print("you are far to poor! earn money first, idiot!")
        elif amount > 0:
            money -= amount
            bread += amount
            print("it's a pleasure to make business with you, Sir!")
        input("Press Enter to continue\n")
            
    if testtile in "BSEF":
        print("A batlle!")
        foeroll = random.randint(1, foes[testtile][1])
        print("The foe is a {} and rolls {}".format(
              foes[testtile][0], foeroll))
        roll = random.randint(1,10)
        print("You roll {}".format(roll))
        if roll > foeroll:
            print("You win!")
            dungeons[z][y+dy] = dungeons[z][y+dy][:x+dx]+"."+dungeons[z][y+dy][x+dx+1:]
            x += dx
            y += dy
        else:
            print("You loose!")
            hitpoints -= random.randint(1,3)
        input("Press Enter")
        
    else:
        x +=dx 
        y += dy
print("Game Over!")
