import os
import time
import subprocess

cwd = os.getcwd()

os.chdir(os.path.join(cwd, "Python"))
start_time = time.time()
subprocess.call(["python", "lakeModelInPython.py"])
print("Lake Model in Python: " + str(time.time() - start_time))

print()

os.chdir(os.path.join(cwd, "C"))
start_time = time.time()
subprocess.call(["python", "lakeModelInC.py"])
print("Lake Model in C: " + str(time.time() - start_time))

print()
    
os.chdir(os.path.join(cwd, "R"))
start_time = time.time()
subprocess.call(["python", "lakeModelInR.py"])
print("Lake Model in R: " + str(time.time() - start_time))