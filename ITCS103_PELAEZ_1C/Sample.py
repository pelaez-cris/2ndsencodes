import os
os.system("cls")
for x in range(5):
    grrt = eval(input("\nInput your grade--->   "))
    if grrt > 100:
        print("\nInvalid Grade, Please try again")
        continue
    elif grrt >= 95 and grrt <= 100:
        print("\nCongrats you got A")
    elif grrt >= 90 and grrt <= 94:
        print("\nCongrats you got B")
    elif grrt >= 85 and grrt <= 89:
        print("\nCongrats you got C")
    elif grrt >= 80 and grrt <= 84:
        print("\nCongrats you got D")
    elif grrt >= 75 and grrt <= 79:
        print("\nCongrats you got E")
    else:
        print("\nSorry you failed\n")
        break
