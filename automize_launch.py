import os
import time
import datetime
from datetime import datetime

startCountTime = time.time()
os.system("python summary.py")
os.system("move " + str(datetime.now().date())+".txt log")

while 1:
	if time.time() - startCountTime > 24*3600:
		os.system("python summary.py")
		os.system("move " + str(datetime.now().date())+".txt log")
		startCountTime = time.time()






