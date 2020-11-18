import os
import time

while True:
    # time.sleep(4)
    os.system("git add .")
    print("git add .")
    # time.sleep(3)
    os.system("""git commit -m "auto commits" """)
    print("""git commit -m "auto commits" """)
    os.system("""git push """)
    print("""git push https://github.com/ShaneWD/Unreal_Engine_test.git """)
    # time.sleep(10)
    os.system("""git pull """)
    print("""git pull """)
    print("111")