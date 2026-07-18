import time
timestam=time.strftime('%H:%M:%s')
print(timestam)
timestam=int(time.strftime('%H'))
print(timestam)
'''timestam=time.strftime('%M')
print(timestam)
timestam=time.strftime('%S')
print(timestam)'''
if(0<timestam<12):
    print("good morning")
elif(12<timestam<22):
    print("good afternoon")
else:
    print("good night")
-------------------------------------------------------------------------------
num=int(input("enter a number\n"))
match num:
    case 0:
        print("number is zero")
    case _ if(num<100):
        print("number is 2 digit")
    case _ if(num<1000):
        print("number is 3 digit")
    case _ :
        print("more than 3 digit")
#no need of break statement 
