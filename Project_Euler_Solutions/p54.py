'''
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest
cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	  Winner
1	 	5H 5C 6S 7S KD    2C 3S 8S 8D TD      Player 2
         Pair of Fives    Pair of Eights

2	 	5D 8C 9S JS AC    2C 5C 7D 8S QH      Player 1
      Highest card Ace   Highest card Queen

3	 	2D 9C AS AH AC    3D 6D 7D TD QD      Player 2
        Three Aces      Flush with diamonds

4	 	4D 6S 9H QH QC    3D 6D 7H QD QS      Player 1
        Pair of Queens    Pair of Queens
      Highest card Nine  Highest card Seven

5	 	2H 2D 4C 4D 4S     3C 3D 3S 9S 9D     Player 1
        Full House         Full House
       with three fours   with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

values = '23456789TJQKA'

#Gets value of card
def get_value(card):
    return values.index(card[0])

#Gets max value of hand
def get_max_value(hand):
    return max([values.index(card) for card in hand])

#Gets all values of a hand
def get_values(hand):
    return sorted([get_value(card) for card in hand], reverse=True)

#Check if the hand is a flush
def is_flush(hand):
    suits = set([card[1] for card in hand])
    return len(suits) == 1

#Check if the hand is straight
def is_straight(hand):
    values = get_values(hand)
    return (max(values) - min(values) == 4) and (len(set(values)) == 5)

#Gets ig there are repeated cards and how many
def get_multiples(hand):
    values = get_values(hand)
    multiples = {}
    for value in values:
        if value not in multiples:
            multiples[value] = 0
        multiples[value] += 1
    return multiples

#If there are 4 repeated cards, it's four of  kind
def is_four_of_a_kind(hand):
    multiples = get_multiples(hand)
    return 4 in multiples.values()

#If there are 3 repeated cards and the last 2 are repeated, it's full house
def is_full_house(hand):
    multiples = get_multiples(hand)
    return (3 in multiples.values()) and (2 in multiples.values())

#If there are three repeated crds, it's three of a kind
def is_three_of_a_kind(hand):
    multiples = get_multiples(hand)
    return 3 in multiples.values()

#If there are 2 repeated cards, it's a two pair
def is_two_pair(hand):
    multiples = get_multiples(hand)
    return list(multiples.values()).count(2) == 2

#If there is only one repeated card, it's one pair
def is_one_pair(hand):
    multiples = get_multiples(hand)
    return 2 in multiples.values()

#Get the kind of hand we have
def get_hand_type(hand):
    if is_flush(hand) and is_straight(hand) and get_value(hand[-1]) == 12:
        return 10 #Royal Flush
    elif is_flush(hand) and is_straight(hand):
        return 9 #Straight Flush
    elif is_four_of_a_kind(hand):
        return 8 #Four of a Kind
    elif is_full_house(hand):
        return 7 #Full House
    elif is_flush(hand):
        return 6 #Flush
    elif is_straight(hand):
        return 5 #Straight
    elif is_three_of_a_kind(hand):
        return 4 #Three of a Kind
    elif is_two_pair(hand):
        return 3 #Two Pairs
    elif is_one_pair(hand):
        return 2 #One Pair
    else:
        return 1 #High Card

def compare_hands(hand1, hand2):
    #Type of hand
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    #If hands have different rank and hand 1 has a greater rank
    if hand1_type!=hand2_type and hand1_type>hand2_type:
        return 1
    #Both hands have the same rank
    elif hand1_type==hand2_type:
        #If they are straight or a flush, hand with biggest card wins
        if hand1_type in [9, 6, 5]:
            if get_max_value(hand1)>get_max_value(hand2):
                return 1
            else:
                return 2
        #Else we only have hands with repeated cards. Highest repeated value wins
        else:
            # Sort the dictionary by value in descending order
            sorted_dict1 = {k: v for k, v in sorted(get_multiples(hand1).items(), key=lambda item: item[1], reverse=True)}
            sorted_dict2 = {k: v for k, v in sorted(get_multiples(hand2).items(), key=lambda item: item[1], reverse=True)}
            # Get the sorted keys as a list
            value1 = list(sorted_dict1.keys())
            value2 = list(sorted_dict2.keys())
            for i in range(len(value1)):
                if value1[i]>value2[i]:
                    return 1
                elif value1[i]<value2[i]:
                    return 2
    #Hand 2 has a greater rank
    else:
        return 2


#Count wins for each player
count1=0
count2=0

#Name of file that contains the hands
name='p054_poker.txt'

#Opens file
file= open(name, 'r')

#List of hands in the file
hand1=[]
hand2=[]

#Extract each hand
for line in file:
    hand1=[]
    hand2=[]
    row=line.split()
    #First 5 cards are hand1. Last 5 are hand2
    for i in range(5):
        hand1.append(row[i])
        hand2.append(row[i+5])
    if compare_hands(hand1, hand2)==1:
        count1+=1
    else:
        count2+=1

print('Player 1:', count1)
print('Player 2:', count2)
