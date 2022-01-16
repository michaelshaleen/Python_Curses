import curses
from curses import wrapper
import time

def main(stdscr):
  # 1 is ID, referenced later by stdscr
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
  curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
  curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
  MAGENTA_AND_YELLOW = curses.color_pair(1)
  CYAN_AND_RED = curses.color_pair(2)
  
  for i in range(100):
      stdscr.clear()
      color = MAGENTA_AND_YELLOW

      if i % 2 == 0:
        color = CYAN_AND_RED

      stdscr.addstr(f"Count: {i}", color)
      stdscr.refresh()
      time.sleep(0.75)


  stdscr.getch()
    
  # row and column
  # A_ == attributes
  # coordinates, string, curses attritbute
  # bitwise or operator combines attributes 
  # stdscr.addstr(15, 40,"Hello planet", MAGENTA_AND_YELLOW | curses.A_UNDERLINE)
  # stdscr.addstr(5, 5,"Solar System", curses.A_UNDERLINE)
  # stdscr.addstr(5, 5,"Solar System", curses.A_UNDERLINE)
  # stdscr.addstr(10, 10, "TenTen", CYAN_AND_RED)


# screen over terminal so print() wont work

  

wrapper(main)