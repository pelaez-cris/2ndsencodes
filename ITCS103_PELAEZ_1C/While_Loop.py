import time
import os
os.system("cls")
tuloy = True
countdown = eval(input('\nEnter a Contdown Number--->   '))
print()
while tuloy:
    time.sleep(0.5)
    print(countdown)
    countdown -= 1
    if countdown == -1:
        print("\nBLAST OFF!!!\n")
        break
    else:
        continue