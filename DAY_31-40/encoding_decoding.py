#encoding and decoding
choice=int(input("do you want to encode or decode?\ntype 1.for encode and 2.for decode\n"))
def encode(sting):
    result=""
    if(len(sting)<=3):
        for i in range(len(sting),0,-1):
            result+=sting[i-1]
        return result
    else:
        for i in range(len(sting),0,-1):
            result+=sting[i-1]
        result="bsk"+result+"jkl"
        return result
def decode(sting):
    result=""
    if(len(sting)<=3):
        for i in range(len(sting),0,-1):
            result+=sting[i-1]
        return result
    else:
        for i in range(len(sting)-3,0,-1):
            if(i>3):
                result+=sting[i-1] 
        return result  
        
if(choice==1):
    data=input("enter your string to encode\n")
    print("enoded string is ", encode(data))
elif(choice==2):
    data=input("enter your string to decode\n")
    print(decode(data))
else:
    print("invalid input\n")
