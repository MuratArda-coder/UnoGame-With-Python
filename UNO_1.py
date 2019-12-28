#!/usr/bin/python3
import random
class UnoCard:
	def __init__(self,c,n):
		self.c = c
		self.n = n
	def __str__(self):
		if(self.c==0):
			x = 'Green '
		elif(self.c==1):
			x = 'Red '
		elif(self.c==2):
			x = 'Blue '
		else:
			x = 'Yellow '
		return x+str(self.n)+(' ')
	def canplay(self,other):
		if((self.c==other.c) or (self.n==other.n)):
			return 1
		else:
			return 0
class CollectionOfUnoCards:
	def __init__(self):
		self.list = []
	def addCard(self,c):
		self.list.append(c)
	def makeDeck(self):
		list = []
		for iii in range(2):
			for ii in range(4):
				for i in range(1,10):
					self.list.append(UnoCard(ii,i))
	def shuffle(self):
		for i in range(2000):
			a = random.randint(0,71)
			b = random.randint(0,71)
			tmp = self.list[a]
			self.list[a] = self.list[b]
			self.list[b] = tmp
	def __str__(self):
		return self.list
	def getNumCards(self):
		return len(self.list)
	def getTopCard(self):
		return self.list[-1]
	def getCard(self,index):
		return self.list[index]
	def canPlay(self,card):
		for i in range(len(self.list)):
			if(self.list[i].canplay(card)==1):
				return 1
		return 0
				
deck = CollectionOfUnoCards()
hand1= CollectionOfUnoCards()
hand2= CollectionOfUnoCards()
lastPlayedCard = UnoCard(0,0)
class Uno:
	def start(self):
		deck.makeDeck()	
		deck.shuffle()
		for i in range(7):
			hand1.addCard(deck.getTopCard())
			del deck.list[-1]
			hand2.addCard(deck.getTopCard())
			del deck.list[-1]
		lastPlayedCard.c = deck.list[-1].c
		lastPlayedCard.n = deck.list[-1].n
		del deck.list[-1]
	def p(self):
		print('YOUR HAND :\n')
		for i in range(hand1.getNumCards()):
			print(i+1,')',hand1.getCard(i))
		print('last played card :',lastPlayedCard,'   Your opponent has',hand2.getNumCards(),'cards')
	def turn(self,p):
		if(p==1):
			f = 0
			while(f==0):
				print(len(deck.list),'cards left in the deck')
				x =input('Type the number of the card you want to play\nType d to draw a card\n')
				if(x=='d'):
					if(len(deck.list)==0):
						return
					else:
						hand1.addCard(deck.getTopCard())
						del deck.list[-1]
						my_game.p()
				elif(x.isdigit()== 0):
					print('Please try again')
				else:
					x = int(x)
					if((x<0) or (x>63)):
						print('Please try again')
					elif(lastPlayedCard.canplay(hand1.list[x-1])==1):
						lastPlayedCard.c = hand1.list[x-1].c
						lastPlayedCard.n = hand1.list[x-1].n
						del hand1.list[x-1]
						f = 1
					else:
						print("You can't play this card\n")
		else:
			while(hand2.canPlay(lastPlayedCard)==0):
				if(deck.getNumCards()==0):
					return
				hand2.addCard(deck.getTopCard())
				del deck.list[-1]
			j=0
			k = len(hand2.list)
			while(j<len(hand2.list)):
				if(lastPlayedCard.canplay(hand2.list[j])==1):
					lastPlayedCard.n = hand2.list[j].n
					lastPlayedCard.c = hand2.list[j].c
					del hand2.list[j]
				j+=1
				if(k>len(hand2.list)):
					break
			my_game.p()
	def playGame(self):
		my_game.start()
		my_game.p()
		while(1):
			my_game.turn(1)
			if(len(deck.list)==0):
				print('__Tie Game__')
				break
			if(len(hand1.list)==0):
				print('__You Won__')
				break
			my_game.turn(2)
			if(len(deck.list)==0):
				print('__Tie Game__')
				break
			if(len(hand2.list)==0):
				print('__You Lost__')
				break
def main():
	global my_game
	my_game = Uno()
	my_game.playGame()
main()
			
