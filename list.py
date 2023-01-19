circle

from math import pi
r=float(input("enter the radius"))
area=float(pi*r**2)
print("the area of the circle is:",area)

color
--------

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

color2
------------

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))


extns
------------
filename=input("enter the file name:")
f_extns=filename.split(".")
print("the extension of the file is:",f_extns[-1]

greater
---------
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2:
    if num1>num3:
        print(num1, "is greater")
elif num2>num3:
    print(num2, "is greater")
else:
    print(num3, "is greater")

lenn

--------------
lst1 = []
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    ele = int(input())
    lst1.append(ele)   
print("list one",lst1)
lst2 = []
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    ele = int(input())
    lst2.append(ele)   
print(lst2)
print("The length of list is: ", len(lst1))
print("The length of list is: ", len(lst2))
if lst1==lst2:
    print("list one is slarger")
else:
    print("list two is slarger")


 length
 ------------------

 list1=[]
list2=[]
n=int(input("enter the elements"))
for i in range(0,n):
    list1.append(int(input()))
print("first list is",list1)
num=int(input("enter the elements"))
for i in range(0,num):
    list2.append(int(input()))
print("first list is",list2)
len1=len(list1)
len2=len(list2)
if len1==len2:
    print("two list are smae length")
else:
    print("two list are not same")

n
--------------------
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

over
------------
list=[]
list=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    list.append(int(input()))
print("list is:",list)
for i in list:
    if i > 100:
      list.append("over")
    else:
          list.append(i)
          print("result list is:",list)


prgm
------------
list1 = []
list2 = []
n = int(input("enter the no of elements: "))
for i in range(0,n):
    list1.append(int(input()))
print("first list is",list1)
m = int(input("enter the no of  elements: "))
for i in range(0,m):
    list2.append(int(input()))
print("second list is",list2)
a=len(list1)
b=len(list2)
if a==b:
    print("lists are of same length")
else:
    print("not same")
s=0
for i in list1:
    s=s+i
    print(s)
t=0
for i in list2:
    t=t+i
    print(t)
if s==t:
    print("sum are equal")
else:
    print("sum is not equal")


num=int(input("enter a number"))
if num in list1 and list2:
    print(num)
else:
    print("no element in common")
common=set(list1).intersection(list2)
print(common,"occur in both")



pgrm 5
------

string = input("enter the string: ")
string = string(0) + string[1:].replace(string[0],"$")
print(string)

string
-----------

string = input("enter the string: ")
string = string[0] + string[1:] . replace(string[0],"$")
print(string)
          
