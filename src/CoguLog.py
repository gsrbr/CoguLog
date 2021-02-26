import os
import time
import sys


def CoguLog(var,var1="",var2="",var3="",var4="",var5="",var6=""):
  if var=='0' or var==0:
    text2log= "["+time.ctime()+"][FATAL]"+var1
  elif var=='1' or var==1:
    text2log= "["+time.ctime()+"][ERROR]"+var1
  elif var=='2' or var==2:
    text2log= "["+time.ctime()+"][WARNING]"+var1
  elif var=='3' or var==3:
    text2log= "["+time.ctime()+"][INFO]"+var1
  elif var=='4' or var==4:
    text2log= "["+time.ctime()+"][DEBUG]"+var1
  elif var=='5' or var==5:
    text2log= "["+time.ctime()+"][TRACE]"+var1
  elif var=='6' or var==6:
    text2log= "["+time.ctime()+"][SECURITY]"
    if var1==1:
      text2log=text2log+"[Foreign Access]"
      if var2==1:
        text2log=text2log+"[ACCEPTED]"
      elif var2==0:
        text2log=text2log+"[DROPED]"
      else:
        text2log=text2log+"[UNKNOW]"
      if var3==1:
        text2log=text2log+"[IP: "+var4+"]"+var5
      elif var3==2:
        text2log=text2log+var3
    elif var1==2:
      text2log=text2log+"[Local Access]"
      if var3==1:
        text2log=text2log+"[IP: "+var4+"]"+var5
      elif var3==3:
        text2log=text2log+var3
  else:
    text2log= "["+time.ctime()+"] log called for unknown reason "
  print ("[LOG] "+text2log)
  f = open("log.clog", "a")
  f.write(text2log+ "\n")
  f.close()
