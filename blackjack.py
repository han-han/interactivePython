# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
guide = ""
score = 0
deck = []
playerhand = []
dealerhand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def drawfront(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def drawback(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0] * 0, 
                    CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1] * 0)
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        handstr = ''
        for card in self.cards:
            handstr += str(card) + ' '
        return handstr

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        handval = 0
        handrank = []
        for card in self.cards:
            handval += VALUES[card.get_rank()]
            handrank.append(card.get_rank())
        if 'A' in handrank:
            if 10 + handval <= 21:
                handval += 10
        return handval
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i, card in enumerate(self.cards):
            card.drawfront(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
              
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                newcard = Card(suit, rank)
                self.deck.append(newcard)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        dealt = self.deck[len(self.deck)-1]
        self.deck.pop(len(self.deck)-1)
        return dealt
    
    def __str__(self):
        # return a string representing the deck
        deckstr = 'Deck contains: '
        for card in self.deck:
            deckstr += str(card) + ' '
        return deckstr

#define event handlers for buttons
def deal():
    global outcome, in_play, playerhand, dealerhand, deck, outcome, guide, score 
    if in_play:
        outcome = "You forfeit..."
        score -= 1
        guide = "New deal?"
        in_play = False
    else:
        deck = Deck()
        guide = 'Hit or Stand?'
        outcome = ""
        playerhand = Hand()
        dealerhand = Hand()
        deck.shuffle()
        card1 = deck.deal_card()
        card2 = deck.deal_card()
        card3 = deck.deal_card()
        card4 = deck.deal_card()
        playerhand.add_card(card1)
        playerhand.add_card(card3)
        dealerhand.add_card(card2)
        dealerhand.add_card(card4)
        in_play = True
    
def hit():
    global score, outcome, in_play, guide
    # if the hand is in play, hit the player
    if in_play:
        if playerhand.get_value() <= 21:
            card = deck.deal_card()
            playerhand.add_card(card)
        # if busted, assign a message to outcome, update in_play and score
        if playerhand.get_value() > 21:
            outcome = "You busted!"
            guide = "New deal?"
            score -= 1
            in_play = False
    else:
        guide = "Not in play!"
        
def stand():
    global score, outcome, guide, in_play
    pv = playerhand.get_value()   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if pv > 21:
        outcome = "You busted!"
        guide = "New deal?"
        in_play = False
    # assign a message to outcome, update in_play and score
    elif in_play:
        while(dealerhand.get_value() < 17):
            card = deck.deal_card()
            dealerhand.add_card(card)
        dv = dealerhand.get_value()
        if dv > 21:
            score += 1
            outcome = "Dealer busted!"
        else:
            if dv >= pv:
                outcome = "Dealer win " + str(dv) + " : " + str(pv)
                score -= 1
            else:
                outcome = "You win  " + str(pv) + " : " + str(dv)
                score += 1
        guide = "New deal?"
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [100, 100], 50, 'LightBlue')
    canvas.draw_text("Score: " + str(score), [400, 100], 35, 'Black')
    canvas.draw_text("Dealer", [100, 170], 35, 'Black')
    canvas.draw_text(outcome, [300, 170], 35, 'Black')
    dealerhand.draw(canvas, [100,200])
    if in_play:
        newcard = Card("S", "A")
        newcard.drawback(canvas, [100, 200])
    playerhand.draw(canvas, [100,400])
    canvas.draw_text("Player", [100, 370], 35, 'Black')
    canvas.draw_text(guide, [300, 370], 35, 'Black')
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric