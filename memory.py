# implementation of card game - Memory

import simplegui
import random

deck = []
exposed = []
state = 0
turned = []
count = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, state, turned, count
    deck = range(0,8)
    deck += range(0,8)
    exposed = [False] * 16
    state = 0
    turned = [-1, -1]
    count = 0
    random.shuffle(deck)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, turned, count
    cardnum = pos[0] // 50
    if not exposed[cardnum]:
        exposed[cardnum] = True
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
        elif state == 2:
            if deck[turned[0]] != deck[turned[1]]:
                exposed[turned[0]] = False
                exposed[turned[1]] = False
            state = 1
            count += 1
    turned[0] = turned[1]
    turned[1] = cardnum
    label.set_text("Turns = " + str(count))
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i, num in enumerate(deck):
        if exposed[i]:
            canvas.draw_text(str(num), [i * 50 + 10, 75], 65, 'White')
        else: 
            canvas.draw_polygon([(i * 50, 0), (i * 50, 100), ((i + 1) * 50, 100), ((i + 1) * 50, 0)], 1, 'Red', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric