#rom functions import square    #specifically import a particular function from the module
import functions    #import the whole module. In this while calling we have to use functions.xyz

for i in range(10):
    #print(f"The square of {i} is {square(i)}") #specifically import a particular function from the module
    print(f"The square of {i} is {functions.square(i)}") #swhile importing whole module we have to write module.xyz
