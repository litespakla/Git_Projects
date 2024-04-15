'''
In the game, Monopoly, the standard board is set up in the following way:

A player starts on the GO square and adds the scores on two 6-sided dice 
to determine the number of squares they advance in a clockwise direction. 
Without any further rules we would expect to visit each square with equal 
probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), 
and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player 
to go directly to jail, if a player rolls three consecutive doubles,
 they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC 
or CH they take a card from the top of the respective pile and, after following the instructions, 
it is returned to the bottom of the pile. There are sixteen cards in each pile, 
but for the purpose of this problem we are only concerned with cards that order a movement; 
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. 
For this reason it should be clear that, with the exception of G2J for which the 
probability of finishing on it is zero, the CH squares will have the lowest probabilities, 
as 5/8 request a movement to another square, and it is the final square that the player 
finishes at on each roll that we are interested in. We shall make no distinction between 
"Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring 
a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate 
these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, 
E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be 
listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
'''
import random

#Monopoly player
class player(object):
    def __init__(self):
        self.__pos=0
    
    def getpos(self):
        return self.__pos
    
    def changepos(self, diceroll):
        self.__pos=(self.__pos+diceroll)%40
    
    def setpos(self, pos):
        self.__pos=pos

#Chance and community chest
class cc_ch(object):
    def __init__(self):
        self.chance=[i for i in range(16)]
        self.chest=[i for i in range(16)]
    
    def shuffle(self):
        random.shuffle(self.chance)
        random.shuffle(self.chest)
    
    def get_chance(self):
        card=self.chance.pop(0)
        self.chance.append(card)
        return card
    
    def get_chest(self):
        card=self.chest.pop(0)
        self.chest.append(card)
        return card
    
    def cc_turn(self, pos):
        card=self.get_chest()

        #Advance to go
        if card==0:
            return 0
        
        #Go to jail
        elif card==1:
            return 10
        
        else:
            return pos
        
    def ch_turn(self, pos):
        match self.get_chance():
            case 1:
                return 0
            case 2:
                return 10
            case 3:
                return 11
            case 4:
                return 24
            case 5:
                return 39
            case 6:
                return 5
            case 7:
                match pos:
                    case 7:
                        return 15
                    case 22:
                        return 25
                    case 36:
                        return 5
            case 8:
                match pos:
                    case 7:
                        return 15
                    case 22:
                        return 25
                    case 36:
                        return 5
            case 9:
                if pos==7 or pos==36:
                    return 12
                elif pos==22:
                    return 28
            case 10:
                return pos-3
            case _:
                return pos

class monopoly(object):
    def __init__(self, num_players, dice_size):
        self.board=[0]*40
        self.cards=cc_ch()
        self.cards.shuffle()
        self.Players=[player() for i in range(num_players)]
        self.size=dice_size
    
    def dice(self):
        a=random.randint(1, self.size)
        b=random.randint(1, self.size)
        return a+b, a==b
    
    def turn(self):
        for p in self.Players:
            while True:
                count=0
                roll, double= self.dice()
                #print(roll, double)
                if double:
                    count+=1

                #Three doubles in a row, go to jail
                if count==3:
                    p.setpos(10)
                    break

                p.changepos(roll)

                pos=p.getpos()
                #print(pos)

                #Chance
                if pos==7 or pos==22 or pos==36:
                    p.setpos(self.cards.ch_turn(pos))

                #Community chest
                elif pos==2 or pos==17 or pos==33:
                    p.setpos(self.cards.cc_turn(pos))
                elif pos==30:
                    p.setpos(10)
                else:
                    pass

                if not double:
                    break
                if p.getpos()==10 and p.getpos!=pos:
                    break

            #print(p.getpos(), type(p.getpos()))  
            self.board[p.getpos()]+=1

class sim(object):
    def __init__(self, num_players, dice_size, turns):
        self.game=monopoly(num_players, dice_size)
        self.turns=turns
    
    def simulation(self):
        for i in range(self.turns):
            self.game.turn()

        board=[i*100/(self.turns*len(self.game.Players)) for i in self.game.board]
        return board
    
players=100
dice=6
turns=100
games=1000
board=[0]*40

for i in range(games):
    game=sim(players, dice, turns)
    board=[a + b for a, b in zip(board, game.simulation())]

board=[i/games for i in board]
print(board)

sorted_pairs = sorted(enumerate(board), key=lambda x: x[1], reverse=True)

# Extract the indices of the top three elements
print((sorted_pairs[:3]))
  


