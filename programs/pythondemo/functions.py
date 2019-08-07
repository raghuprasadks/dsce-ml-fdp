# -*- coding: utf-8 -*-
def greeting():
    print('say hello')

greeting()
    
'''  C    
void greeting()
{
 printf('hello')
}
'''
def add(num1,num2):
    res = num1 + num2
    return res

res = add (100,200)
print('result is',res)

name = input('Enter your name')
print('your name is ',name)
print(type(name))
#casting
age = int(input('Enter your age'))
print(type(age))
print(age)

def multivalue(num1,num2):
    return num1,num2
n1,n2 = multivalue(100,200)
print(n1,n2)





