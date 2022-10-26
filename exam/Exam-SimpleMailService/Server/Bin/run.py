import os
import sys

cur_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(cur_path, "../Src/SimpleServer.py")
os.system(f"python3 {script_path}")