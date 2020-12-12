
# IMPORTING RANDOM MODULE TO SHUFFLE THE CARDS
import random

# CREATING GLOBAL VARIABLES
# SUITS TUPLE
suits = ("Spades","Hearts","Clubs","Diamonds")

# RANKS TUPLE 
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")

# VALUES DICTIONARY
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8,
        "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

# CARD CLASS
class Card:
    '''
    Here we will set up our card class that will give us the suit of a card, the rank of a card
    and the value of a card that will help us letter to compare their values
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    #  IT WILL PRINT THIS VALUE WHENEVER WE PRINT AN OBJECT OF THIS CLASS
    def __str__(self):
        return self.rank + " of " + self.suit

# DECK CLASS
class Deck:
    '''
    Here we will set up our deck class that will create a new deck as we make an object of it.
    All cards will be added in a list and later we will shuffle that list to give us random cards
    '''

    def __init__(self):
        # SETTING UP EMPTY LIST
        self.all_cards = []

        # APPENDING CARDS IN THE LIST 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        '''
        SINCE IT WILL NOT RETURN ANYTHING WE NEED TO CALL THIS METHOD AT THE INSTANT 
        OF THE MAIN PROGRAM.
        '''

        # USING THE RANDOM MODULE TO SHUFFLE THE LIST
        random.shuffle(self.all_cards)

    # CREATING THIS METHOD TO DEAL A CARD
    def deal_one(self):
        return self.all_cards.pop()

# PLAYER CLASS
class Player:
    '''
    Here we will set up our player and player deck.
    Here player will be able to remove a card from the top and add cards at the bottom.
    '''

    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.player_cards = []

    def remove_one(self):
        # REMEMBER TO SET POP AT 0 BECAUSE 0 IS TOP AND -1 IS BOTTOM AND WE NEED TO REMOVE CARDS FROM THE TOP
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):
        # IF THERE ARE MULTIPLE CARDS USE EXTEND
        # EXTEND MERGES TWO LIST 
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)

        # IF THERE IS A SINGLE CARD    
        else:
            self.player_cards.append(new_cards)    

    def __str__(self):
        #  IT WILL PRINT THIS VALUE WHENEVER WE PRINT AN OBJECT OF THIS CLASS
        return f"Player {self.name} has {len(self.player_cards)} cards" 

# MAIN PROGRAM STARTS FROM HERE
if __name__ == "__main__":
    
    # STARTING OUR GAME
    print("\n+-------------------------------------------------+")
    print("| ***** WELCOME TO THE 'WAR! THE CARD GAME' ***** |")
    print("+-------------------------------------------------+")

    start = ""

    while True:
        # USER PERMISSION
        print("\n ---> DO YOU WANT TO PLAY THIS GAME")
        start = input("TO START PRESS 'S' AND TO QUIT PRESS 'Q' :-\n").upper()

        if start == "S":
            players = 0

            # PLAYERS SELECTION
            while players != 1 and players != 2:
                try:
                    print("SELECT A PLAYER MODE")
                    players = int(input("FOR SINGLE PLAYER PRESS '1' AND FOR TWO PLAYERS PRESS '2' :-\n"))

                except ValueError:
                    print("\nSORRY WRONG INPUT\n")    

            # PLAYER 1 VS COMPUTER MODE
            if players == 1:
                player_1_name = input("Player enter your name :-\n")

                # SETTING UP PLAYER NAME AND COMPUTER
                player_one_deck = Player(player_1_name)
                computer_deck = Player("Computer")

                # DECK OBJECT
                new_deck = Deck()

                # SHUFFLING DECK
                new_deck.shuffle()

                # DISTRIBUTION OF CARDS
                for items in range(26):
                    player_one_deck.add_cards(new_deck.deal_one())
                    computer_deck.add_cards(new_deck.deal_one())

                print("\nCARDS HAS BEEN DISTRIBUTED\n")    

                GAME_ON = True

                # TO KEEP UPDATE WITH WHICH ROUND IS GOING ON
                round_counter = 0

                while GAME_ON:
                    round_counter = round_counter + 1
                    print("--->")
                    print(f"\n*** ROUND {round_counter} ***\n")
                    print("--->")

                    # TO SHOW PLAYERS HOW MUCH CARDS ARE LEFT
                    print(f"YOU HAVE {len(player_one_deck.player_cards)} CARDS LEFT")
                    print(f"COMPUTER HAVE {len(computer_deck.player_cards)} CARDS LEFT")

                    # IF PLAYER ONE LOSE
                    if len(player_one_deck.player_cards) == 0:
                        print(f"Player {player_one_deck.name}, you are out of cards!")
                        print("You LOSE! Computer has WON the game")
                        GAME_ON = False
                        break
                    
                    # IF COMPUTER LOSE
                    if len(computer_deck.player_cards) == 0:
                        print("Computer is out of cards!")
                        print(f"CONGRATULATIONS! Player {player_one_deck.name} YOU WON")
                        GAME_ON = False
                        break

                    # STARTING NEW ROUND
                    player_one_cards = []
                    dial_key = input("\nPress Enter to deal a card :-\n")
                    player_one_cards.append(player_one_deck.remove_one())
                    print(player_one_cards[-1])

                    computer_cards = []
                    computer_cards.append(computer_deck.remove_one())
                    print(computer_cards[-1])

                    # WHILE AT WAR
                    AT_WAR = True

                    while AT_WAR:
                        
                        print(f"\nPlayer {player_one_deck.name} WAR card is {player_one_cards[-1]}")
                        print(f"\nComputer WAR card is {computer_cards[-1]}\n")

                        # IF COMPUTER LOSE
                        if player_one_cards[-1].value > computer_cards[-1].value:
                            print(f"\nPlayer {player_one_deck.name} have won this round\n")
                            player_one_deck.add_cards(player_one_cards)
                            player_one_deck.add_cards(computer_cards)
                            AT_WAR = False

                        # IF PLAYER ONE LOSE
                        elif player_one_cards[-1].value < computer_cards[-1].value:
                            print("\nComputer have won this round\n")
                            computer_deck.add_cards(player_one_cards)
                            computer_deck.add_cards(computer_cards)
                            AT_WAR = False

                        else:
                            print("XXXXXXXX")
                            print("\n| WAR! |\n")
                            print("XXXXXXXX")

                            # WE CAN SET IT TO ANY LIMITS 3, 5, 10 DEPENDS ON YOU
                            dial_key = input("\nPress Enter to deal 10 cards :-\n")
                            if len(player_one_deck.player_cards) < 10:
                                print("You are unable to declare war")
                                print("You LOSE! Computer has WON the game")
                                GAME_ON = False
                                break

                            elif len(computer_deck.player_cards) < 10:
                                print("Computer is unable to declare war")
                                print(f"CONGRATULATIONS! Player {player_one_deck.name} YOU WON")
                                GAME_ON = False
                                break

                            else:
                                # THIS WILL APPEND TO THE PLAYER AND COMPUTER CARDS
                                for num in range(10):
                                    player_one_cards.append(player_one_deck.remove_one())
                                    computer_cards.append(computer_deck.remove_one())    

            # PLAYER 1 VS PLAYER 2 MODE
            else:
                player_1_name = input("Player 1 enter your name :-\n")
                player_2_name = input("Player 2 enter your name :-\n")

                # SETTING UP PLAYER 1 AND PLAYER 2 NAME
                player_one_deck = Player(player_1_name)
                player_two_deck = Player(player_2_name)

                new_deck = Deck()

                new_deck.shuffle()

                for items in range(26):
                    player_one_deck.add_cards(new_deck.deal_one())
                    player_two_deck.add_cards(new_deck.deal_one())

                print("\nCARDS HAS BEEN DISTRIBUTED\n")

                # FROM HERE ONWARDS EVERYTHIS IS SAME JUST CHANGED COMPUTER TO PLAYER TWO
                # AND IT WILL TAKE RESPONSE FROM BOTH THE PLAYERS       

                GAME_ON = True

                round_counter = 0

                while GAME_ON:
                    round_counter = round_counter + 1
                    print("--->")
                    print(f"*** ROUND {round_counter} ***")
                    print("--->")

                    print(f"Player {player_one_deck.name} HAVE {len(player_one_deck.player_cards)} CARDS LEFT")
                    print(f"Player {player_two_deck.name} HAVE {len(player_two_deck.player_cards)} CARDS LEFT")

                    if len(player_one_deck.player_cards) == 0:
                        print(f"Player {player_one_deck.name} is out of cards!")
                        print(f"CONGRATULATIONS! Player {player_two_deck.name} YOU WON")
                        GAME_ON = False
                        break

                    if len(player_two_deck.player_cards) == 0:
                        print(f"Player {player_two_deck.name} is out of cards!")
                        print(f"CONGRATULATIONS! Player {player_one_deck.name} YOU WON")
                        GAME_ON = False
                        break

                    # STARTING NEW ROUND
                    player_one_cards = []
                    dial_key_1 = input(f"\nPlayer {player_one_deck.name} Press Enter to deal a card :-\n")
                    player_one_cards.append(player_one_deck.remove_one())
                    print(f"\nPlayer {player_one_deck.name} got {player_one_cards[-1]} card")

                    player_two_cards = []
                    dial_key_2 = input(f"\nPlayer {player_two_deck.name} Press Enter to deal a card :-\n")
                    player_two_cards.append(player_two_deck.remove_one())
                    print(f"Player {player_two_deck.name} got {player_two_cards[-1]} card\n")

                    # WHILE AT WAR
                    AT_WAR = True

                    while AT_WAR:

                        print(f"\nPlayer {player_one_deck.name} WAR card is {player_one_cards[-1]}")
                        print(f"Player {player_two_deck.name} WAR card is {player_two_cards[-1]}\n")

                        if player_one_cards[-1].value > player_two_cards[-1].value:
                            print(f"\nPlayer {player_one_deck.name} have won this round\n")
                            player_one_deck.add_cards(player_one_cards)
                            player_one_deck.add_cards(player_two_cards)
                            AT_WAR = False

                        elif player_one_cards[-1].value < player_two_cards[-1].value:
                            print(f"\nPlayer {player_two_deck.name} have won this round\n")
                            player_two_deck.add_cards(player_one_cards)
                            player_two_deck.add_cards(player_two_cards)
                            AT_WAR = False   

                        else:
                            print("XXXXXXXX")
                            print("\n| WAR! |\n")
                            print("XXXXXXXX")

                            dial_key_1 = input(f"\nPlayer {player_one_deck.name} Press Enter to deal 10 cards :-\n")
                            dial_key_2 = input(f"\nPlayer {player_two_deck.name} Press Enter to deal 10 cards :-\n")

                            if len(player_one_deck.player_cards) < 10:
                                print("PLayer one is unable to declare war")
                                print(f"CONGRATULATIONS! Player {player_two_deck.name} YOU WON")
                                GAME_ON = False
                                break

                            elif len(player_two_deck.player_cards) < 10:
                                print("PLayer two is unable to declare war")
                                print(f"CONGRATULATIONS! Player {player_one_deck.name} YOU WON")
                                GAME_ON = False
                                break

                            else:
                                for num in range(10):
                                    player_one_cards.append(player_one_deck.remove_one())
                                    player_two_cards.append(player_two_deck.remove_one())

        elif start == "Q":
            print("THANK YOU FOR PLAYING THIS GAME")
            break

        else:
           print("\nSORRY WRONG INPUT\n")   