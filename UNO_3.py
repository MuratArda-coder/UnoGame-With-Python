#!/usr/bin/python3
import random

class UnoCard():
	c = -1
	n = -1 
	def __init__(self,c,n):
		self.c=c
		self.n=n
	def __str__(self):
		if str(self.c) =='0':
			self.c='Green'
		if str(self.c) =='1':
			self.c='Yellow'
		if str(self.c) =='2':
			self.c='Blue'
		if str(self.c) =='3':
			self.c='Red'
		return str(self.c)+""+str(self.n)
	def canPlay(self, other):
		if(self.c==other.c or self.n==other.n):
			return True
		else:
			return False
class CollectionOfUnoCards():
	def __init__(self):
		self.list = []
	def addCard(self,card):
		self.list.append(card)	
	def makeDeck(self):
		c = ''
		d = ''
		for color in range(4):
			for number in range(1,10):
				c = UnoCard(color,number)
				self.addCard(c)
		for color in range(4):
			for number in range(1,10):
				d = UnoCard(color,number)
				self.addCard(d)	
	def shuffle(self): 
		k = 0
		while (k < 1000):
			x1 = random.randint(0,71)		
			x2 = random.randint(0,71)
			key = self.list[x1]
			self.list[x1] = self.list[x2]
			self.list[x2] = key
			k = k+1
	def __str__(self):
		x = ''
		for i in range(len(self.list)):
			x += str(self.list[i])+','
		return str(x)
	def getNumCards(self):
		return len(self.list)
	def getTopCard(self):
		TopCard = self.list[0]
		return TopCard
		if (len(TopCard)==1):
			return True
		else:
			return False
	def canPlay1(self,card1,card2):
		if card1.canPlay(card2):
			return True
	def getCard(self,index):
		for i in range(len(self.list)):
			if i == index :
				print(self.list[i])
				return self.list[i]
class uno():
	def __init__(self):
		self.hand = CollectionOfUnoCards()
		self.hand1 = CollectionOfUnoCards()
		self.hand2 = CollectionOfUnoCards()
		self.deck=CollectionOfUnoCards()
		self.deck.makeDeck()
		self.deck.shuffle()
		self.deck.getNumCards()
		self.deck.getTopCard()
		self.TopCard = self.deck.getTopCard()
		self.Table=[]
		for i in range(0,7):
			self.hand1.list.append(self.TopCard)
			self.deck.list.remove(self.TopCard)
			self.TopCard = self.deck.getTopCard()
		for i in range(0,7):
			self.hand2.list.append(self.TopCard)
			self.deck.list.remove(self.TopCard)
			self.TopCard = self.deck.getTopCard()
		self.Table.append(self.TopCard)
		self.deck.list.remove(self.TopCard)
		print("Table:", self.Table[0])
		print()
		
	def playGame(self,hand):
		self.hand=hand
		k = 0
		for i in range (len(self.hand.list)):
			if self.hand.canPlay1(self.Table[0],self.hand.list[i]):
				key = self.hand.list[k] 
				self.hand.list[k]=self.hand.list[i]
				self.hand.list[i]=key
				k=k+1
		if k>0 :
			index=random.randint(0,k-1)
			card = self.hand.getCard(index)
			self.Table.append(self.hand.list[index])
			self.hand.list.remove(self.hand.list[index])
			self.Table=[self.Table[-1]]
		else :
			self.TopCard = self.deck.getTopCard()
			self.hand.list.append(self.TopCard)
			self.TopCard = self.deck.getTopCard()
			self.deck.list.remove(self.TopCard)
			if self.hand.canPlay1(self.Table[0],self.hand.list[-1]):
				self.Table.append(self.hand.list[-1])
				self.hand.list.remove(self.hand.list[-1])
				self.Table=[self.Table[-1]]
		k = 0

		print()
		print("Table:", self.Table[0])

	def yourturn(self,hand):
		self.hand=hand
		k = 0
		for i in range (len(self.hand.list)):
			if self.hand.canPlay1(self.Table[0],self.hand.list[i]):
				k =k+1
		if k > 0 :
			turn = 1
			while turn == 1 :
				key = 1
				index = input("Your turn:")
				try:
					index = int(index)
				except ValueError:
					print("just a number:" )
					index = input("Your turn:")
				while index > len(self.hand.list) and index > 0 :
					print("out of range, please try again: ")
					index = int(input("Your turn:"))
				card = self.hand.getCard(index-1)
				while 1 :
					if self.hand.canPlay1(self.Table[0],card):
						self.Table.append(card)
						self.hand.list.remove(card)
						self.Table=[self.Table[-1]]
						print("you play:",card)
						turn = 0
						break
					print("you draw wrong card, try again:")
					break
		else :
			self.TopCard = self.deck.getTopCard()
			print("you gain:",self.TopCard)
			print()
			cardmiss=input("You dont have any card to draw. You will automaticly take card from deck and draw automatickly if you can. Press enter to continue:")
			self.hand.list.append(self.TopCard)
			self.TopCard = self.deck.getTopCard()
			self.deck.list.remove(self.TopCard)
			if self.hand.canPlay1(self.Table[0],self.hand.list[-1]):
				self.Table.append(self.hand.list[-1])
				self.hand.list.remove(self.hand.list[-1])
				self.Table=[self.Table[-1]]
		print("your number of desk:",len(self.hand.list))
		print()
		print("your hand:",self.hand)
		print()
		print("Table:", self.Table[0])
		print()
		print("number of deck:",len(self.deck.list))
		
	def playTurn(self): 
		t = 1
		print("how do you want to play: \n user to computer(1) \n computer to computer(2) ")
		self.game = int(input("play style: "))
		if self.game == 1 or self.game == 2 :
			while self.game == 1 :
				print("#######################################################")
				print("Turn",t)
				for i in range(len(self.hand2.list)):
					print("("+str(i+1)+")",self.hand2.list[i])
				self.playGame(self.hand1)
				self.yourturn(self.hand2)
				print("player1 number of desk:",len(self.hand.list))
				t = t+1
				print("#######################################################")
				if len(self.hand1.list)==0:
					break
				if len(self.deck.list)==0:
					break
				if len(self.hand2.list)==0:
					break
			
			while self.game == 2 :
				print("#######################################################")
				print("Turn",t)
				self.playGame(self.hand1)
				self.playGame(self.hand2)
				z = 0
				y = 0
				key = 1
				print("player1:",self.hand1)
				print("player2:",self.hand2)
				print("number of card in deck:",len(self.deck.list))
				print("player1:","		","player2:")
				while(key == 1):
					if(y != len(self.hand1.list) and z != len(self.hand2.list)):
						for i in range(y,len(self.hand1.list)):
							print("p1","("+str(i+1)+")",self.hand1.list[i], end='		')
							y = y+1
							break
					elif(y != len(self.hand1.list)):
						for i in range(y,len(self.hand1.list)):
							print("p1","("+str(i+1)+")",self.hand1.list[i])
							y = y+1
					else:
						print(end='			')
					if (z != len(self.hand2.list)):
						for j in range(z,len(self.hand2.list)):
							print("p2","("+str(j+1)+")",self.hand2.list[j])
							z = z+1
							break
					if(y == len(self.hand1.list) and z == len(self.hand2.list)):
						key = 0
				print("\n")
				t = t+1
				print("#######################################################")
				if len(self.hand1.list)==0:
					break
				if len(self.deck.list)==0:
					break
				if len(self.hand2.list)==0:
					break
		else:
			print("sory wrong number")
	def printResult(self):
		if self.game == 1 :
			if len(self.hand1.list) == 0 :	
				print("Player1 is winner")
				print("player1 hand:",self.hand1)
				print("your hand :",self.hand2)
			if len(self.hand2.list) == 0 :
				print("You are winner")
				print("player1 hand:",self.hand1)
				print("your hand :",self.hand2)
			if len(self.deck.list) == 0 :
				print("No one wins")
				print("player1 hand:",self.hand1)
				print("your hand:",self.hand2)
		if self.game == 2 :
			if len(self.hand1.list) == 0 :	
				print("Player1 is winner")
				print("player1 hand:",self.hand1)
				print("player2 hand :",self.hand2)
			if len(self.hand2.list) == 0 :
				print("player2 is winner")
				print("player1 hand:",self.hand1)
				print("player2 hand :",self.hand2)
			if len(self.deck.list) == 0 :
				print("No one wins")
				print("player1 hand:",self.hand1)
				print("player2 hand:",self.hand2)
def main():
	game = uno()
	game.playTurn()
	game.printResult()
main()
