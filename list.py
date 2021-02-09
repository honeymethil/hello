#names = ["Honey", "Seena", "Anu"]
#print(names)

#names = []      #create an empty list

names = list()  # create an empty list

names.append("Honey") # since list are immutable you can add values using append method
names.append("Seena")
names.append("Anu")
print(names)

names.append("Shiva")
print(names)

names.append("Honey") #list and tuples can have duplicate values

# List by default does not get sorted. We can sort a list using sort method. 
# Sort affects the actual list values

names.sort()   
print(names)


print(names[0]) #since list is a sequence of (mutable) values, it can be called using indexing

# Using the len() method

print(len(names))