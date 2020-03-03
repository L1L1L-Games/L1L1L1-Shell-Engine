import L1L1L1Engine

from time import sleep

from L1L1L1Engine import clear, start


with open('code.xeq', 'w') as file:
  while True:
    try:
      command = input(">>")
      if(command == '[exit]'):
        for i in range(1, 7):
          clear()
          c = i * '.'
          print('Exiting Engine' + str(c))
          sleep(0.5)
        clear()
        print("Exited")
        break
      if(command == '[clear]'):
        clear()
        start()
      exec(command)
      file.write(command + '\n')
    except:
      print('Error')