 #error handling or exception handling
a=input("enter one number:")
print(f"multiplication of {a} is")
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")#will handle all error and make you to jump except part if there's error in try part so that program doesnt stop
except:
    print("told you to enter number not string idiot")
print("some imp lines.............")
#you can handle any kind of error 
try:
    n=int(input("enter num:"))
    a=[1,2]
    print(a[n])
except ValueError:
    print("bhai number enter kar")
except IndexError:
    print("aukat me soch saale")
