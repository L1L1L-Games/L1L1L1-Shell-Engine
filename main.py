from subprocess import call
import os
from time import sleep

def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls') 

print("L1L1L1 Shell Engine")
print('_' * 25)
print('Basic Syntax:')
print('\t[exit] - exits the shell')
print('\t[clear] - clears the screen')
print('_' * 35)
print()
with open('code.xeq', 'w') as file:
  while True:
    try:
      command = input(">>")
      if(command == '[exit]'):
        break
      if(command == '[clear]'):
        clear()
      exec(command)
      file.write(command + '\n')
    except:
      print('Error')