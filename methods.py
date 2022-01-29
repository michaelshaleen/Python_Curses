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
  # echo keystrokes that user types
  curses.echo()
  

  # border colors
  stdscr.attron(MAGENTA_AND_YELLOW)
  stdscr.border()
  stdscr.attroff(MAGENTA_AND_YELLOW)




  # attribute on offs
  stdscr.attron(GREEN_AND_BLACK)
  rectangle(stdscr, 1, 1, 5, 20)
  stdscr.attroff(GREEN_AND_BLACK)
  stdscr.addstr(5, 30, "Hello Mars")
# moves cursor
  stdscr.move(10, 20)

  stdscr.refresh()


  while True:
    key = stdscr.getkey()
    if key == "q":
      break

  

wrapper(main)