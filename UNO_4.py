#!/usr/bin/python3
import random
import time

class UnoCard:
    def __init__(self,color,number):
        self.color = color
        self.number = number

    def canPlay(self, other):
        if self.color == other.color or self.number == other.number:
            return True
        else:
            return False

    def __str__(self):
        if self.color == 0:
            return "Yellow "+ str(self.number)
        elif self.color == 1:
            return "Red "+str(self.number)
        elif self.color == 2:
            return "Green "+str(self.number)
        elif self.color == 3:
            return "Blue "+str(self.number)



class CollectionOfUnoCards:

    def __init__(self):
        self.Cards = []

    def addCard(self,c):
        self.Cards.append(c)

    def makeDeck(self):
        for i in range(1,10):
            for j in range(4):
                for k in range(2):
                    self.Cards.append(UnoCard(j,i))

    def shuffle(self):
        for i in range(800):
            x = random.randint(0,len(self.Cards)-1)
            y = random.randint(0,len(self.Cards)-1)
            temp = self.Cards[x]
            self.Cards[x] = self.Cards[y]
            self.Cards[y] = temp

    def __str__(self):
        s = "1) "+ str(self.Cards[0])
        for i in range(1,len(self.Cards)):
            s = s + "\n"+str(i+1)+") "+str(self.Cards[i])
        return s

    def getNumCards(self):
        return len(self.Cards)

    def getTopCard(self):
        return self.Cards[-1]

    def canPlay(self,c):
        global index
        for i in range(len(self.Cards)):
            if self.Cards[i].canPlay(c) == True:
                index = i
                return True
        return False

    def getCard(self,index):
        return self.Cards[index]

class Uno:
    player = 1
    Deck = CollectionOfUnoCards()
    lastPlayedCard = 0
    hand1 = CollectionOfUnoCards()
    hand2 = CollectionOfUnoCards()
    Game = True

    def __init__(self):
        self.Deck.makeDeck()
        self.Deck.shuffle()
        for i in range(7):
            self.hand1.addCard(self.Deck.Cards.pop())
        for i in range(7):
            self.hand2.addCard(self.Deck.Cards.pop())

    def playGame(self):
        print("Welcome. Type 'exit' to end the game.")
        print("Player 1:")
        print(self.hand1)
        while 1:
            try:
                a = input("Please enter the index of the card you want to discard.")
                if a == "exit":
                    print("Bye bye!")
                    self.Game = False
                    break
                a = int(a)
                if a <= 0:
                    nope
                print("Discarding",self.hand1.Cards[a-1])
                self.lastPlayedCard = self.hand1.Cards[a-1]
                del self.hand1.Cards[a-1]
                break
            except:
                print("Out of index.")
        self.playTurn(2)

    def playTurn(self,player):
        self.player = player
        self.printResult()
        while self.Game == True:

            if self.player == 1:
                time.sleep(random.uniform(0.5,1.0))
                print("\nPlayer 1:")
                print(self.hand1)
                while 1:
                    self.printResult()
                    try:
                        print("Last played card is",self.lastPlayedCard)
                        if self.hand1.canPlay(self.lastPlayedCard) == True:
                            a = input("Which card would you like to play? ")
                            if a == "exit":
                                print("Bye bye!")
                                self.Game = False
                                self.playTurn(1)
                                break
                            a = int(a)
                            if a <= 0:
                                nopenopenope
                            if self.hand1.Cards[a-1].canPlay(self.lastPlayedCard) == True:
                                print("Playing",self.hand1.Cards[a-1])
                                self.lastPlayedCard = self.hand1.Cards[a-1]
                                del self.hand1.Cards[a-1]
                                if self.hand1.getNumCards() == 1:
                                    print("UNO!")
                                self.playTurn(2)
                                break
                            else:
                                print("Please select a playable card.")
                        else:
                            print("No card to play. Drawing.")
                            self.hand1.Cards.append(self.Deck.Cards.pop())
                            self.playTurn(2)
                            break
                    except:
                        print("Please enter the index of the card you want to play.")
            elif self.player == 2:
                time.sleep(0.5)
                self.printResult()
                print("\nPlayer 2:")
                if self.hand2.canPlay(self.lastPlayedCard) == True:
                    print("Playing",self.hand2.Cards[index])
                    self.lastPlayedCard = self.hand2.Cards[index]
                    del self.hand2.Cards[index]
                    if self.hand2.getNumCards() == 1:
                        print("UNO!")
                    self.playTurn(1)
                else:
                    print("No card to play. Drawing.")
                    self.hand2.Cards.append(self.Deck.Cards.pop())
                    self.playTurn(1)

    def printResult(self):
        if len(self.hand1.Cards) == 0:
            print("Player 1 has won.")
            print("Deck has",self.Deck.getNumCards(),"cards left.")
            self.Game = False
        elif len(self.hand2.Cards) == 0:
            print("Player 2 has won.")
            print("Deck has",self.Deck.getNumCards(),"cards left.")
            self.Game = False
        elif (self.player == 1 and self.Deck.getNumCards() == 0 and self.hand1.canPlay(self.lastPlayedCard) == False) or (self.player == 2 and self.Deck.getNumCards() == 0 and self.hand2.canPlay(self.lastPlayedCard) == False):
            print("Deck is out of cards.\nIt is a tie!")
            self.Game = False

    def main():
        my_game = Uno()
        my_game.playGame()

Uno.main()
