#!/usr/bin/python
# -*- coding:UTF-8 -*-

print "#" * 30
class JustCounter:
    __secretCount = 0 # Private class variable, could not be accessed outside of this class
    publicCount = 0 # This is public class variable
    class_counter = 0
    
    def count(self) :
        self.__secretCount += 1         # In this case, the self denotes that this variable should be used through an instance, 
        self.publicCount += 1           # which will not touch the value in this class, be careful about the printed results 
        JustCounter.class_counter += 1  # While When instance of this class call count method, this variable will change its value
        # print self.__secretCount

# Create two objects        
counter = JustCounter() 
myCount = JustCounter()
# Call methods of class through instance
counter.count() 
counter.count()
myCount.count()
myCount.count()
print "This is dict of instance : counter"
print counter.__dict__
print "This is dict of instance : myCount"
print myCount.__dict__
print "This is dict of class"
print JustCounter.__dict__
print "This is the value of private variable of instance: counter"
print counter._JustCounter__secretCount
