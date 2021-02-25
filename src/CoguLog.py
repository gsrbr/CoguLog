import os
import time
import sys


def CoguLog(var,desc=""):
  if var=='0':
    text2log= "[0]["+time.ctime()+"]"+desc
  elif var=='1':
    text2log= "[1]["+time.ctime()+"]"+desc
  elif var=='2':
    text2log= "[2]["+time.ctime()+"]"+desc
  elif var=='3':
    text2log= "[3]["+time.ctime()+"]"+desc
  elif var=='4':
    text2log= "[4]["+time.ctime()+"]"+desc
  elif var=='5':
    text2log= "[5]["+time.ctime()+"]"+desc
  else:
    text2log= "["+time.ctime()+"] log called for unknown reason "
  print ("[LOG] "+text2log)
  f = open("log.clog", "a")
  f.write(text2log+ "\n")
  f.close()
