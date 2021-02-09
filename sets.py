#s = {1,2,3,4}

#s = {}      #create an empty set
s = set()   #create an empty set

s.add(1)    #since sets are mutable, we can add values using add method
s.add(5)    #Sets by default gets sorted
s.add(2)
s.add(3)
s.add(4)

s.add(3)    #set cannot have duplicate values. It will show only once

print(s)
#print(s[0]) #set object is not subscriptable

s.remove(2)     #you can also remove an element from a set using the remove method
print(s)

#All sequence have an ibuilt method to find out the elements within the string or list or tuple or set
# Using the len() method
# Number of items in a list
# number of elements in a set
# number of characters in a string

print(f"The set has {len(s)} number of elements")