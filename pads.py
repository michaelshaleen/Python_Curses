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
# height width row column of window within screen

  pad = curses.newpad(100, 100)
  stdscr.refresh()
  for i in range(100):
    for j in range(26):
      char = chr(67 + j)
      pad.addstr(char, MAGENTA_AND_YELLOW)


# pad relative to window
# start at 0, 0 relative to pad, 5, 5, on screen pad will be
# end 25, 75
  for i in range(50):
      stdscr.clear()
      stdscr.refresh()
      pad.refresh(0, 0, 5, i, 10, 25 + i)
      time.sleep(0.2)
      stdscr.getch()
  

wrapper(main)