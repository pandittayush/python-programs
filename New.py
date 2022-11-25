'''P=eval(input("Enter the value of Principal:"))
ROI=eval(input("Enetr the value of Rate of intrest:"))
years=eval(input('Enter the number of years:'))
SI=P*ROI*years/100
print('simple intrest=',SI)'''

#Write a program to convert temperature from celsius to fahrenheite

'''celsius=eval(input("Enter degree in Celsius"))
print("celsius=",celsius)
Fahrenhiet=(9/5)*celsius+32
print('Fahrenhiet=',Fahrenhiet)'''

from __future__ import print_function
from cgi import print_exception


'''x=6
y= 'prince'
print(x)
print(y)'''

'''x=str(4)
y=int(4)
z=float(4)
print(x)
print(y)
print(z)'''

'''x=9
y=('prince')
print (type(x))
print (type(y))'''

'''x= "john"
x= 'john'
print (x)'''

'''x,y,z = "lauda" ,"lehsun" ,'muh me lele'
print(x)
print(y)
print(z)'''

#many variable but single value

'''x=y=z= 'lauda'
print(x)
print(y)
print(z)'''

'''fruits=["apple", "banana", "cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)'''

'''x='ankit'
y='bihari'
z='hai'
print(x+y+z)'''

'''x=5
y="ashwani"
print(x+y)'''

'''x=5
y="ashwani"
print(x,y)'''

'''x= "awesome"
def myfunc():
    x= 'fantastic'
    print("Ankit is" +x)
    
    myfunc()
print("Ankit is" +x)'''

'''x = "awesome"

def myfunc():
  global x
  x = "lauda fantastic"

myfunc()

print("python is " + x)'''

'''x=1
y=2.6

a=int(y)

print(a)'''

'''import random

print(random.randrange(1 , 7))'''

'''hey guys this is ayush here currently i am sitting 
in the library in front 
of a chutiya whose 
name is prince 
print(a) '''

''''a= 'hello ayush'
print(len(a))'''

'''a= 'tell me you are bihari without telling that you are from bihar'
print('bihar' in (a))'''

'''txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")'''


'''a= "fuckyoubehanchod"
print(a[2:6])'''

'''fck="I love my country"
if "expensive" not in fck:
  print("no, 'expensive' is not present")'''

'''a="hello bacha log kaise ho aap log"
print(a.replace ("h"," k"))'''

'''a= "arnav"
b= "birla"
c= a +" " +b
print(c)'''

'''age = 36
name= "anuj"
buy="mac"
worth=100000
isha="parvati"
txt = "My name is John, and I am {} my friend name is {} i want to buy {}  worth off {} Shiva isha ka matlb jante ho tum  {}"
print(txt.format(age,name,buy,worth,isha))'''


'''a=[1,2,3,4,5]
print(a[3] )'''
#list slicing

'''friends = ["harry", "tom" , "rohan" , "sam", "divya",]
print(friends[-4:4])'''

l1= [1,2,5,6,87,36,]
print(11)
#l1.sort()
#print(l1)
#l1.append(76)
#print(l1)
#l1.insert(3,544)
#print(l1)
#l1.remove(87)
#print(l1)
#l1.pop(2)
#print(l1
#t=(1,2,3,4,5)
#print(t[0])
#print(t[1,])
#print(t.count(2))
#anaconda=["apple","banana","mango", "cherry", "baby"]
#anaconda.insert(2,"blackcurrent")
#print(anaconda)
#ayush=["apple", "banana", "cherry"]
#anuj=["orange", "papaya", "mango"]
#ayush.extend(anuj)
#print(ayush)

#ayush=["apple", "banana", "cherry"]
#ayush.remove("apple")
#print(ayush)

#ayush=["apple", "banana", "cherry"]
#ayush.pop(1)
#print(ayush)

#ayush= ["apple", "banana" ,"cherry"]
#ayush.clear()
#print(ayush)

#ayush=["apple", "banana", "cherry"]
#for i in range(len(ayush)):
#  print(ayush[i])

#ayush=["apple", "banana", "cherry"]
#i=0
#while i < len(ayush):
  #print(ayush[i])
  #i=i+1

#ayush = ["banana" , "cherry" , "orange"]
#[print(x) for x in ayush] 

'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
ayush= []

for x in fruits:
  if "a" in x:
   ayush.append(x)


  print(ayush)'''

'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
ayush = [x for x in fruits if "a" in x]
print(ayush)'''

'''def myfunc(n):
    return abs(n - 50)

ayush = [100 ,50,63,45,46]
ayush.sort(key=myfunc)
print(ayush)'''

'''def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)'''



