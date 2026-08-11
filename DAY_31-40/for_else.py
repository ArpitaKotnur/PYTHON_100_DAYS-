#for and else
for i in range(5):
    print(i)
else:
    print(f"{i+1} is not in range")#will execute if condition dont meet
for p in range(10):
    if p==5:
        print(f"fuckk its {p} i am gonna break")#if we apply break it means the complete break of loop so execution of else cuz its the part of loop
        break;
else:
    print("hurrrrayyyyy")
s=1
while s<0:
    print("okay im negative person")#demo of how else works
else:
    print("omg i am positive")
