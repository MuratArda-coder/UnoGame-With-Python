import random

class UnoCard:
    def __init__(self, color, number):
        self.Color = color
        self.Number = number

    def __str__(self):
        if self.Color == 0:
            return ("Blue "+ str(self.Number))
        if self.Color == 1:
            return ("Green "+ str(self.Number))
        if self.Color == 2:
            return ("Red "+ str(self.Number))
        if self.Color == 3:
            return ("Yellow "+ str(self.Number))

    def can_play(self, other):
        if (self.Color == other.Color) or (self.Number == other.Number):
            return True
        else:
            return False
class CollectionOfUnoCards(UnoCard):
    def __init__(self):
        self.Cards = []

    def add_card(self, card):
        self.Cards.append(card)
        return self.Cards

    def make_deck(self):
        for color in range(4):
            for number in range(1, 10):
                self.add_card(UnoCard(color, number))
                self.add_card(UnoCard(color, number))

    def shuffle(self):
        for shuffle in range(10000):
            first = random.randint(0, 71)
            second = random.randint(0, 71)
            self.Cards[first],self.Cards[second]= self.Cards[second],self.Cards[first]
        return self.Cards
    def __str__(self):
        string = ""
        for i in range(len(self.Cards)):
            string = string + str(self.Cards[i]) + ", "
        return string[0: -2]
    def get_num_cards(self):
        NumberOfCards = len(self.Cards)
        return NumberOfCards
    def get_top_card(self):
        global topcard
        topcard = self.Cards[0]
        self.Cards.remove(topcard)
        return topcard
    def canPlay(self,hand):
        for i in range(len(hand.Cards)):
            if hand.Cards[i].can_play(lastPlayedCard) == True:
                return True
        return False
    def comp_canplay(self):
        for i in range(len(self.Cards)):
            if self.Cards[i].Color == lastPlayedCard.Color or self.Cards[i].Number == lastPlayedCard.Number:
                return self.Cards[i]
    def get_card(self, index):
        return self.Cards[self.index]

class Uno(CollectionOfUnoCards):
    Deck = CollectionOfUnoCards()
    Hand_1 = CollectionOfUnoCards()
    Hand_2 = CollectionOfUnoCards()
    lastPlayedCard = 0
    def convert_input(self,list):
        if list[0] == "Blue":
            list[0] = 0
            list[1] = int(list[1])
            return list
        if list[0] == "Green":
            list[0] = 1
            list[1] = int(list[1])
            return list
        if list[0] == "Red":
            list[0] = 2
            list[1] = int(list[1])
            return list
        if list[0] == "Yellow":
            list[1] = int(list[1])
            list[0] = 3
            return list

    def __init__(self):
        self.Deck.make_deck()
        self.Deck.shuffle()
        self.Deck.get_top_card()
        for i in range(7):
            self.Hand_1.add_card(self.Deck.Cards[i])
            self.Deck.Cards.remove(self.Deck.Cards[i])
        for j in range(7):
            self.Hand_2.add_card(self.Deck.Cards[j])
            self.Deck.Cards.remove(self.Deck.Cards[j])

    def play_game(self,Hand_1,Hand_2):
        self.flag = 0
        global name1, name2
        print(" SIMPLE UNO GAME")
        choosemode = input(" To play vs computer press 1 \n To play 1vs1 press 2\n:")
        if choosemode == "1":
            name1 = input("Player 1's name ")
            name2 = "Computer"
            print(name1, "'s HAND: ", self.Hand_1)
            print("Computer's HAND: ", self.Hand_2)
            self.flag = 0
        else:
            name1 = input("Player 1's name ")
            name2 = input("Player 2's name ")
            print(name1, "'s HAND: ", self.Hand_1)
            print(name2, "'s HAND: ", self.Hand_2)
            self.flag = 1

        global turn1,turn2
        turn1 = name1+"'s Turn:"
        turn2 = name2 + "'s Turn:"
        global lastPlayedCard
        lastPlayedCard = topcard
        print("Deck = ",self.Deck)
        print("TOPCARD = ",topcard)
        if self.play_turn() == 1:
            self.chooseside = 1
            print(name1, "is lucky and starting")
        else:
            self.chooseside = 0
            print(name2, "is lucky and starting")
        while self.flag:
            if self.chooseside == 1:
                while 1:
                    try:
                        if self.Deck.canPlay(Hand_1) == False:
                            self.Hand_1.add_card(self.Deck.Cards[0])
                            print(name1," has drawn ",self.Deck.Cards[0],"\n"," Last Played Card is ",lastPlayedCard)
                            self.Deck.Cards.remove(self.Deck.Cards[0])
                            print(name2, "'s HAND: ", self.Hand_2)
                            self.chooseside = 0
                            break
                        x = input(turn1)
                        a = x.split(" ")
                        self.convert_input(a)
                        x = UnoCard(a[0], a[1])
                        for i in range(len(self.Hand_1.Cards)):
                            if x.Color == self.Hand_1.Cards[i].Color and x.Number == self.Hand_1.Cards[i].Number:
                                z = self.Hand_1.Cards[i]
                        if lastPlayedCard.can_play(z) == True:
                            lastPlayedCard = z
                            self.Hand_1.Cards.remove(z)
                            print("Last Played Card is ",lastPlayedCard)
                            print(name2,"'s HAND: ",self.Hand_2)
                            self.chooseside = 0
                            break
                        else:
                            print("Enter a right card.")
                            print("Last Played Card is ", lastPlayedCard)
                            print(name1, "'s HAND: ", self.Hand_1)
                    except:
                        print("Enter a right card.")
                        print("Last Played Card is ", lastPlayedCard)
                        print(name1, "'s HAND: ", self.Hand_1)
                if self.print_result() == True:
                    break
            else:
                while 1:
                    try:
                        if self.Deck.canPlay(Hand_2) == False:
                            self.Hand_2.add_card(self.Deck.Cards[0])
                            print(name2,"has drawn ",self.Deck.Cards[0], "\n","Last Played Card is ",lastPlayedCard)
                            self.Deck.Cards.remove(self.Deck.Cards[0])
                            print(name1, "'s HAND: ", self.Hand_1)
                            self.chooseside = 1
                            break
                        x = input(turn2)
                        a = x.split(" ")
                        self.convert_input(a)
                        x = UnoCard(a[0], a[1])
                        for i in range(len(self.Hand_2.Cards)):
                            if x.Color == self.Hand_2.Cards[i].Color and x.Number == self.Hand_2.Cards[i].Number:
                                z = self.Hand_2.Cards[i]
                        if lastPlayedCard.can_play(z) == True:
                            lastPlayedCard = z
                            self.Hand_2.Cards.remove(z)
                            print("Last Played Card is ",lastPlayedCard)
                            print(name1,"'s HAND: ", self.Hand_1)
                            self.chooseside = 1
                            break
                        else:
                            print("Enter a right card.")
                            print("Last Played Card is ", lastPlayedCard)
                            print(name2, "'s HAND: ", self.Hand_2)
                    except:
                        print("Enter a right card.")
                        print("Last Played Card is ", lastPlayedCard)
                        print(name2, "'s HAND: ", self.Hand_2)
                if self.print_result() == True:
                    break
        while not self.flag:
            if self.chooseside == 1:
                while 1:
                    try:
                        if self.Deck.canPlay(Hand_1) == False:
                            self.Hand_1.add_card(self.Deck.Cards[0])
                            print(name1," has drawn ",self.Deck.Cards[0],"\n","Computers HAND :",self.Hand_2,"\nLast Played Card is ",lastPlayedCard)
                            self.Deck.Cards.remove(self.Deck.Cards[0])
                            print(name2, "'s HAND: ", self.Hand_2)
                            self.chooseside = 0
                            break
                        x = input(turn1)
                        a = x.split(" ")
                        self.convert_input(a)
                        x = UnoCard(a[0], a[1])
                        for i in range(len(self.Hand_1.Cards)):
                            if x.Color == self.Hand_1.Cards[i].Color and x.Number == self.Hand_1.Cards[i].Number:
                                z = self.Hand_1.Cards[i]
                        if lastPlayedCard.can_play(z) == True:
                            lastPlayedCard = z
                            self.Hand_1.Cards.remove(z)
                            print("Last Played Card is ",lastPlayedCard)
                            print("Computers HAND: ",self.Hand_2)
                            self.chooseside = 0
                            break
                        else:
                            print("Enter a right card.")
                            print("Last Played Card is ", lastPlayedCard)
                            print(name1, "'s HAND: ", self.Hand_1)
                    except:
                        print("Enter a right card.")
                        print("Last Played Card is ", lastPlayedCard)
                        print(name1, "'s HAND: ", self.Hand_1)
                if self.print_result() == True:
                    break

            else:
                while 1:
                        if self.Deck.canPlay(Hand_2) == False:
                            self.Hand_2.add_card(self.Deck.Cards[0])
                            print("Computer has drawn ",self.Deck.Cards[0],"\n",name1,"'s HAND: ",self.Hand_1,"\nLast Played Card is ",lastPlayedCard)
                            self.Deck.Cards.remove(self.Deck.Cards[0])
                            self.chooseside = 1
                            break
                        else:
                            strvar = Hand_2.comp_canplay()
                            print("Computer played:",strvar)
                            lastPlayedCard = strvar
                            self.Hand_2.Cards.remove(strvar)
                            print("Last Played Card is ",lastPlayedCard)
                            print(name1,"'s HAND: ", self.Hand_1)
                            self.chooseside = 1
                            break
                if self.print_result() == True:
                    break
    def play_turn(self):
        self.flag2 = 0
        if random.choice([1,2]) == 1:
            self.flag2 = 1
        else:
            self.flag2 = 0
        return self.flag2
    def print_result(self):
        if self.Hand_1.get_num_cards() == 0:
            print (name1+" won!")
            return True
        if self.Hand_2.get_num_cards() == 0:
            print (name2+" won!")
            return True
        if self.Deck.get_num_cards() == 0:
            print ("Draw!")
            return True
def main():
    my_game = Uno()
    my_game.play_game(my_game.Hand_1,my_game.Hand_2)
main()

