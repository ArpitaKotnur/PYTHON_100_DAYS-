#doc_string and pep 8
#doc_string=this are the line of statement which will execute if and only if it is mentioned after the name of function or brfore the body of function
def num(n):
    '''this will give the number n which was passed through'''
    print(n)
    
num(6)
#can acess through attribute
print(num.__doc__)
#well comments and docstring are completing differnt cuz python ignore the comments but docstring are not they get accessed through attribute
'''pep-8 python enhancement propasal, guidelines and proposal for user kinda document which give updates for everthing related to python
ZEN OF PYTHON=import this will give a poem related to python '''
