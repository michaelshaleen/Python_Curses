import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
  # 1 is ID, referenced later by stdscr
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
  MAGENTA_AND_YELLOW = curses.color_pair(1)
  GREEN_AND_BLACK = curses.color_pair(2)

  stdscr.attron(GREEN_AND_BLACK)
  rectangle(stdscr, 1, 1, 5, 20)
  stdscr.attroff(GREEN_AND_BLACK)

  stdscr.refresh()

  stdscr.getch()

  

wrapper(main)