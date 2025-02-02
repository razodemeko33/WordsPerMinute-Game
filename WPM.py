import curses 
import time
import random
from curses import wrapper #diff terminal ya side ko lagi

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(" Welcome to the Speed Typing Test")
    stdscr.addstr(" \nPress any key to begin") 
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    for i, char in enumerate (current): #if ["a","b","c"] cha so i would index 0 and then char would have a 
       correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
            
        stdscr.addstr(0, i, char, color) #(0,i) pverwrite garcha line stdscr.addstr(y, x, text, color) here y=row and x=column

def load_text():
    with open("text.txt" , "r") as f:
        lines = f.readlines()
        return random.choice(line).strip()
        #gives random lines form text file and strip gets rid of whitespaces



def wpm_test(stdscr):
    target_text = load_text()
    current_text=[]
    wpm = 0
    #stdscr.addstr(target_text)
    #stdscr.refresh()
    start_time = time.time() #gives number of seconds but really large
    stdscr.nodelay(True)

    while True:
        time_elapsed = max (time.time() - start_time , 1) #(larger time - larger time kinda thing)
        wpm = round (( len(current_text) / (time_elapsed / 60))) / 5
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        #stdscr.addstr(target_text)
        if "".join(current_text) == target_text: #takes list and combines every char into one
            stdscr.nodelay(False)
            break

        try:
        key = stdscr.getkey() 
        #current_text.append(key)
        except:
            continue # brings to the top of while loop

        if ord(key) == 27: #ascii representation 27 is escpae key
            break
        if key in ("KEY>BACKSPACE", '\b', "\x7f"): # representation of backspace
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
                current_text.append(key)

        #stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # the 1 represents the pair like pair of green and white
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # the 2 represents the pair like pair of yellow and white id same vayo vane it overwrites
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # the 3 represents the pair like pair of white and black id same vayo vane it overwrites

    
   # key = stdscr.getkey() # to not immediately close the program and wait for the user to do so
    start_screen(stdscr) 
    while True:
        wpm_test(stdscr)

stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
key = stdscr.getkey()
if ord(key) == 27:
    break



wrapper(main) # passing main inside wrapper
