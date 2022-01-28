import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
  # 1 is ID, referenced later by stdscr
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
  curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
  curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
  MAGENTA_AND_YELLOW = curses.color_pair(1)
  CYAN_AND_RED = curses.color_pair(2)
  stdscr.nodelay(True)


  x, y = 0, 0
  while True:
    key = stdscr.getkey()
    if key == "KEY_LEFT":
      x -= 1
    elif key == "KEY_RIGHT":
      x += 1
    elif key == "KEY_UP":
      y -= 1 
    elif key == "KEY_DOWN":
      y += 1


    stdscr.clear()
    stdscr.addstr(y, x, "X")
    stdscr.refresh()
    

# string in terminal, use getkey, string asks for input
  # refresh upon next action
  # key = stdscr.getkey()
  # stdscr.addstr(5, 5, f"Key: {key}")
  # stdscr.refresh()
  # stdscr.getch()



  

wrapper(main)