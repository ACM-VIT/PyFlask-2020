#tuples tutorial

a=(1,2,3,4,5,6,7,8,9)
print(a)

b=1,2,3
print(b)

#accessing an item
print(a[1])
print(a[-1]) #last item

#slicing similar to lists
print(a[3:8])

#different types of data
a=(10,20,30,[40,50,60])
print(a)
print(a[3])
print(a[3][1])

#cannot change data
# a=(1,2,3)
# a[2]=9  #this line will give error

#joining two tuples
a=(1,2,3)
b=(4,5,6)
print(a+b)

#deleting a tuple
del a
#print(a)   #will raise error

#count
a=(1,1,1)
print(a.count(1))

#index
a=3,4,1
print(a.index(1))