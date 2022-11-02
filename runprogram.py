import time
import os

program = ["deletefiles.py", "reademail.py", "pandastomysql.py"]

while True:
    for p in program:
        string = "python " + p
        os.system(string)
        print("Finished: " + p) 
        time.sleep(10)
    
    os.systen("TASKKILL /F /IM msedge.exe")
    print("waiting a whole day") 
    time.sleep(86360)
