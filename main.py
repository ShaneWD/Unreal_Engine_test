import os
import time

while True:
    time.sleep(3)
    os.system("git add .")
    time.sleep(3)
    os.system(""" git commit -m "auto commits" """)
    os.system(""" git push """)
    time.sleep(3)