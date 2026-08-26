#enumerete- its a function which will give me index+value for example
lis=["apple","banana","grapes","orange","pineapple"]
index=0
for i in lis:
    print(i)
    if index==2:
        print("aare bhai aap")
    index=index+1
#instead of doing this kind of shitt enumerarate will itself count or give index+value
toing=["nithin","theja","pranav","teji","kshama"]
for chutiya_level,name in enumerate(toing):
    print(chutiya_level,name)
    if chutiya_level==0:
        print("you are the most disrespect person i ever met")
#you can also mention the index to start with any number like
num=[1,2,3,4,5,6,7,8]
for index,value in enumerate(num,start=5):
    print(f"for index={index},we have {value} value")
#why to use? no need to count the index evrytime you go through and also you can modify the index staring value accoeding to your way 
