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
s=0
for i in lst1:
     s=s+i
     print(s)
t=0
for i in lst2:
    t=t+i
    print(t)
if s==t:
     print("sum are equal")
else:
     print("sum is not equal")


if num in lst1 and lst2:
    print(num)
else:
    print("no element in common")
common=set(lst1).intersection(lst2)
print(common,"occur in both")
   
