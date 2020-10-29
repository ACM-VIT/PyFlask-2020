#dictionary tutorial

dict1={1:"Monday", 2:"Tuesday", 3:"Wednesday"}
print(dict1)
print(dict1[2])

#get
print(dict1.get(3))

#copy
dict2=dict1.copy()
print(dict2)

#clear
dict1.clear()
print(dict1)

#values
dict1={1:"Monday", 2:"Tuesday", 3:"Wednesday"}
print(dict1.values())

#update
dict1[2]="Thursday"
print(dict1)

dict1.update({ 4:"Saturday",5:"Sunday"})
print(dict1)

#items
print(dict1.items())

#keys
print(dict1.keys())

#pop
a=dict1.pop(4)
print(a)
print(dict1)

#popitem
print(dict1.popitem())
print(dict1)

print(dict1.popitem())
print(dict1)

