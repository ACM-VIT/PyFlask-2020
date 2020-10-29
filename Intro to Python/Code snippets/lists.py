#lists tutorial

list1=[7,5,6,1,12]
print(list1)
print(len(list1))

#length of a list
print(len(list1))

#iterating through a list
for i in range(0,5):
    print(list1[i])

#sort()
list1.sort()
print(list1)

#reverse() 
list1.reverse()
print(list1)

#list comprehension
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print(odd_square)

#list slicing
list2 =list(range(1, 11)) 
print (list2) 
print(list2[2:5]) #from the third to 5th element
print(list2[2:9:2]) #in steps of 2

#string lists
str=["monday","tuesday","wednesday"]
print(str)

str2="Monday,Tuesday,Wednesday"
print(str2.split(","))

str3="Monday Tuesday Wednesday"
print(str3.split(" "))

