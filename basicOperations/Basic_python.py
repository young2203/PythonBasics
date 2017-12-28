#!/usr/bin/python
# -*-coding: UTF-8 -*-
# This is script is used to show some basic concepts in Python programming

#import modules that will be used in this script
import numpy as np
import math
import sys
#from numpy import array

print "**************Case study starts **************"
###########################Basic concepts in Python############################
#Tips: if we want to check all the methods we could use for a object we can call
# list.__doc__ or use dir(list)
# Even more, we could use an instance to check method information of that object
# like dir(1) , dir ('A') will return method information for integer (object)
# and for string (object) respectively

# (1) Here we showed some basic usages related with strings
print "*********string study *********"
ThisIsNumber = 1
print ThisIsNumber
ThisIsString = "I'm Mike, I come from U.S. "
print ThisIsString
ThisIsAlsoString= 'I said "what\'s up" '
print ThisIsAlsoString
TripleString='''
This is a triple line string
we don't need \\n here to initiate a new line 
'''
print TripleString

# (2) Here we are going to define list, list is mutable and inhomogenous
# we have: append, extend, insert, pop, remove, reverse, sort methods for list
print "*********list study *********"
newlist = [ 'rice', 798, 2.25, 'John', 70.2]
print newlist
newlist.append('NewItem') #list is mutable
print newlist
print newlist[0]  # list numbering will start from 0, as in C language
print newlist[-3:0:-1] # -1 is a pointer of the last element in this list
                      # newlist[ start_no : end_no : step ]
                      # when step is negative, items will show from backwards
                      # to forwards
list_1=[ 1, 2, 3]; list_2= [ 4, 5, 6 ]
newlist=[ list_1, list_2 ]
print newlist[1][1] #This will give you 5, refer to the 2nd element of list_2

# (3) Here we are going to define tuple, tuple is immutable and inhomogenous
# you can treat tuple as read-only file that we don't have write access
print "*********tuple study *********"
newtuple = ( "string", 798, 2.2, 'John')
print newtuple * 2
print newtuple[::-1] #print tuple reversely

# (4) Here we are going to define dictionary, dictionary is mutable and inhomogenous
# you can use key value to refer to elements in a dictionary, it is a very important
# data structure in python programming which is very powerful
# REMEMBER there is no pre-defined order of elements in dictionary !!!! see results
print "*********dictionary study *********"
myDict = {} #initiate an empty dictionary
myDict['one'] = 'This is the 1st element'
myDict[2] = "This is the 2nd one"  
print "This is the print-out of the whole dictionary"; print myDict
print "These are all the keys: "; print myDict.keys()
print "These are all the corresponding values: "; print myDict.values()
print "Use key to print out specific element: " + myDict['one'] # myDict [ key] refers 
                                        # to the value corresponding to this key
# Create a dictionary from a list of tuples in (key, value) form
d = [ ('1st',1), ('2nd','2nd'), (3,5)]
myNewDict = dict(d) 
print myNewDict 
# Fill the dictionary when initiate it
myNewNewDict = { 'key1' : 1 , 'key2' : 2}
print myNewNewDict

# (4) Here we are going to define a array, array is mutable and homogenous
# we need import numpy module before we use properties of array
print "*********array study *********"
myArray = np.array( [ [1, 2], [2, 4], [4, 8] ] ) #np is abbr. of module numpy
my2ndArray = np.array( [ [1, 2], [2, 4], [4, 8] ] ) 
print myArray * my2ndArray

###########################Basic operations in Python##########################
print "*********basic operation study *********"
print "Exponential 2^3 2**3 = " + str( 2**3 )
print "Exact divition 5//2 = " + str( 5 // 2 )
print "mod 5%2 = " + str( 5 % 2 )
print "5 is not equal to 4 : " + str( 5 != 4)  #in python, boolean values are
                                               # True and False
print " (2>1) AND (2<3) : " + str( ( 2 > 1 ) and ( 2 < 3 ) ) # and, or, not
myList = [2.25, '2.23', 'abc']
print "myList = " + str(myList)
print " Is 2.23 in myList? " + str( 2.23 in myList)
print " Is '2.23' in myList? " + str( '2.23' in myList)

###########################Control Blocks in Python############################
# (1) if-elif-else switch control
print "*********if-elif-else control *********"
flag = 2
if flag == True:
    print "This is true" 
elif flag == False :
    print "This is false"
else: 
    print "Something goes wrong"
    
# (2) while-else loop control
print "*********while-else loop control *********"
myFavorList = [ 1, 5, 5.3, 6 , 10, 15, 2.5]
even_number= []; odd_number= []
while len(myFavorList) > 0 :
    myItem = myFavorList.pop()
    if myItem % 2 == 0 :
        even_number.append( myItem ) 
    elif myItem % 2 == 1 :
        odd_number.append( myItem )
    else :
        print "This item is not an integer : " + str( myItem )
else :
    print "Classification is done"; print "Even number:" + str(even_number)

# (3) for-else loop control

print "*********for-else loop control *********"
for i in range(10,20) : # check numbers from 10 to 20, determine whether they are prime or not
    for j in range(2, i):
        if i % j == 0:
            factor_1 = j
            factor_2 = i/j
            print " %d = %d * %d " % (i, factor_1, factor_2)
            break #if we know i is resoluble, there is no need to do 
                  #rest of the nested loop
        else :
            pass # No function, occupy the position to make structure complete
else:
    print " %d is a prime" % i

###########################Function definition in Python#######################
# (1) general function definition
print "*********function definition *********"
def printinfo ( name = 'Mike', age = 35 ) : #Set default value for function variables
    "Printing name and age info in pairs"
    print "Name: " + str(name)
    print "Age: " + str(age)
    return None 
printinfo() #no input, use default values
printinfo( age=50, name = 'Emma') 

# (2) anonymous function definition / or lambda function
# define a sum function to perform addition, this is similar to @ in MATLAB (function handle)
print "*********anonymous function definition *********"
mySum = lambda var_1, var_2 : var_1 +var_2
print mySum(20, 30) 

##########################Object-Orientated Programing in Python###############
print "*********class concept study *********"
class Employee:
    'Base class for all the empolyees' #help information, print module_name.Employee.__doc__ to check it
    empCount = 0 #class variable        #in this case, module_name = Basic_python
    
    def __init__( self, name, salary ) : # __init__ is used as constructor, create instance based on this class
        self.name=name  # In this case, you can use Employee (name, age) to create an instance
        self.salary=salary
        Employee.empCount += 1
        
    def displayCount(self) :
        print "Total Employee %d" % Employee.empCount
        
    def displayEmployee(self) :
        print "Name : " + str(self.name) + ", Salary: " + str(self.salary)

# if we import this file as a module in a new script, e.g. import Basic_python as bp
# then we could call the methods of class Employee we have already defined here
# Karel = bp.Employee(name='Karel',salary=100000000) will create an instance: Karel
# Mike =bp.Employee(name='Mike', salary=16000) will generate another instance: Mike
# To call the methods of Class Employee, we could do something like this:
# Karel.displayCount() or Mike.displayCount(), these two will have the same function
