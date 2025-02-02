import curses 
from curses import wrapper #diff terminal ya side ko lagi

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(" Welcome to the Speed Typing Test")
    stdscr.addstr(" \nPress any key to begin") 
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(target_text)

    for i, char in enumerate (current_text): #if ["a","b","c"] cha so i would index 0 and then char would have a 
        stdscr.addstr(0, i, char, curses.color_pair(1)) #(0,i) pverwrite garcha line stdscr.addstr(y, x, text, color) here y=row and x=column




def wpm_test(stdscr):
    target_text = "Hello World this is some text for the app!"
    current_text=[]
    #stdscr.addstr(target_text)
    #stdscr.refresh()
    

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        stdscr.addstr(target_text)

        key = stdscr.getkey() 
        #current_text.append(key)

        if ord(key) == 27: #ascii representation 27 is escpae key
            break
        if key in ("KEY>BACKSPACE", '\b', "\x7f"): # representation of backspace
            if len(current_text) > 0:
                current_text.pop()
        else:
                current_text.append(key)

        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # the 1 represents the pair like pair of green and white
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # the 2 represents the pair like pair of yellow and white id same vayo vane it overwrites
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # the 3 represents the pair like pair of white and black id same vayo vane it overwrites

    
   # key = stdscr.getkey() # to not immediately close the program and wait for the user to do so
    start_screen(stdscr) 
    wpm_test(stdscr)


wrapper(main) # passing main inside wrapper
