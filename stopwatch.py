# template for "Stopwatch: The Game"
import simplegui

# define global variables
currenttime = 0
totalstop = 0
perfectstop = 0
timer_run = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    B = (t - A * 600) / 100
    C = (t - A * 600 - B * 100) / 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global timer_run 
    timer_run = True
    timer.start()
    
def Stop():
    timer.stop()
    global totalstop, perfectstop, timer_run
    if timer_run:
        totalstop += 1
    if (currenttime % 10 == 0 and timer_run):
        perfectstop += 1
        timer_run = False
    
def Reset():
    timer.stop()
    global currenttime, totalstop, perfectstop, timer_run 
    currenttime = 0
    totalstop = 0
    perfectstop = 0
    timer_run = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global currenttime
    if currenttime <= 600 * 10:
        currenttime += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(currenttime), [100, 150], 50, 'Red')
    canvas.draw_text(str(perfectstop) + '/' + str(totalstop), [260, 20], 20, 'Red')

# create frame
frame = simplegui.create_frame("StopWatch", 300, 300)

# register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.stop()
# Please remember to review the grading rubric
              
              