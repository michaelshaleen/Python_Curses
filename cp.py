import curses
from curses import wrapper

def main(stdscr):
  # 1 is ID, referenced later by stdscr
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
  MAGENTA_AND_YELLOW = curses.color_pair(1)
  stdscr.clear()
  # row and column
  # A_ == attributes
  # coordinates, string, curses attritbute
  stdscr.addstr(15, 40,"Hello planet", MAGENTA_AND_YELLOW)
  stdscr.addstr(5, 5,"Solar System", curses.A_UNDERLINE)
  stdscr.addstr(5, 5,"Solar System", curses.A_UNDERLINE)


# screen over terminal so print() wont work

  stdscr.refresh()
  stdscr.getch()

wrapper(main)