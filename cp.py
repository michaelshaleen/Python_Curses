import curses
from curses import wrapper

def main(stdscr):
  stdscr.clear()
  # row and column
  stdscr.addstr(15, 40,"Hello planet", curses.A_BOLD)
  stdscr.addstr(5, 5,"Solar System", curses.A_UNDERLINE)

# screen over terminal so print() wont work

  stdscr.refresh()
  stdscr.getch()

wrapper(main)