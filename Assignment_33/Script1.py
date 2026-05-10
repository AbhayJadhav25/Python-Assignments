import sys
import os
import time
import psutil
def create_log(DirName):
  Ret = os.path.exists(DirName)
  if(Ret == True):
    Ret = os.path.isdir(DirName)
    if(Ret == False):
      print("Unable to scan.")

  else:
    os.makedirs(DirName)
    print("Folder Created.")

  ctime = time.strftime("%Y-%m-%d_%H-%M-%S")   
  filename = "System_%s.log" %(ctime) 
  filename = os.path.join(DirName ,filename )  #Information/log file
  print(filename)
  fobj = open(filename , "w")
  print("CPU Usage : %s %%\n" %psutil.cpu_percent())
  fobj.close()
def main():
  dir_name = sys.argv[1]
  create_log(dir_name)

if __name__ == "__main__":
  main()