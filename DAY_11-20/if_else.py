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
