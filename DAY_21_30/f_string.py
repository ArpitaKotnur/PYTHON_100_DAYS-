#fstring= mostly for formating the string 
letter="hey my name is {} and i am from {}"
country="india"
name="arpiii"
print(letter.format(country,name))#argument passing
#letter="hey my name is {1} and i am from {0}" even by passing arguments you can give it
print(letter.format(name,country))#this was the old method and now we decided to use string formating in differnt way
print(f"heyy guyssssss this is {name} from the very crazy country {country}")
#can also give decimal specaialization
price=7.949494949
txt=f"will sell at {price:2f} rupess"
print(txt)
print(type(txt))
#how to retain my fstring as fstring
print(f"heyy guyssssss this is {{name}} from the very crazy country {{country}}")
