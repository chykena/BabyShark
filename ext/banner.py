import random
from termcolor import cprint, colored

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
BOLD = '\033[1m'
END = '\033[0m'


def LoadBabysharkBanner():

  print(G + BOLD +'888888b.            888                     .d8888b.  888                       888')      
  print(G + BOLD +'888  "88b           888                    d88P  Y88b 888                       888')      
  print(G + BOLD +'888  .88P           888                    Y88b.      888                       888')     
  print(G + BOLD +'8888888K.   8888b.  88888b.  888  888       "Y888b.   88888b.   8888b.  888d888 888  888') 
  print(G + BOLD +'888  "Y88b     "88b 888 "88b 888  888          "Y88b. 888 "88b     "88b 888P"   888 .88P') 
  print(G + BOLD +'888    888 .d888888 888  888 888  888            "888 888  888 .d888888 888     888888K')  
  print(G + BOLD +'888   d88P 888  888 888 d88P Y88b 888      Y88b  d88P 888  888 888  888 888     888 88b') 
  print(G + BOLD +'8888888P"  "Y888888 88888P"   "Y88888       "Y8888P"  888  888 "Y888888 888     888  888') 
  print(G + BOLD +'                                  888                                                    ')
  print(G + BOLD +'                            Y8b d88P                                                    ')
  print(G + BOLD +'                            "Y88P"                                                     ')
  print(B + BOLD + "_____________________________________" + END)
  print(R + "-==[ " + BOLD + "A Network Traffic Interceptor" + END)
  print(R + "-==[ " + BOLD + "Developed By: GROUP SIX   " + END)
  print(B + BOLD + "_____________________________________\n" + END)

entry_phrases = [
    'Sniff All The Things.',
    'God Bless Telescopes.',
    'Wiretap The World.',
    'She Loves BABY SHARK.',
    'Be The Man-in-the-middle.',
    '<3 Sniff Responsibly.',
]


def BabysharkBreaker():

  breaker = colored('''
  ====================================================================================
  ''', 'grey', attrs=['bold'])
  print(breaker)
