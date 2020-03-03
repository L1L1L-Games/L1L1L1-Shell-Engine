from subprocess import call
import os
from time import sleep

def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls') 

def start():
  print("L1L1L1 Shell Engine")
  print('_' * 25)
  print('Basic Syntax:')
  print('\t[exit] - exits the shell')
  print('\t[clear] - clears the screen')
  print('_' * 35)
  print()
start()