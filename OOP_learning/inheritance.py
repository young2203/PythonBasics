#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent : #Define superclass
    parentAttr = 100
    def __init__(self) :
        print "Call constructor of superclass"
        
    def parentMethod(self) :
        print "Call method of superclass"
        
    def setAttr(self, attr) :
        Parent.parentAttr = attr
        
    def getAttr(self) :
        print "Attributes of superclass : ", Parent.parentAttr
        
class Child (Parent) :
    def __init__(self) :
        Parent.__init__(self) #call constructor of superclass explicitly
        # Or you could use super(Child,self).__init__() to instead
        # in this case, if this subclass has inheritated properties from 
        # more than one superclass, using super function will be more
        # efficient
        print '#' * 12
        print "Call constructor of subclass"
        
    def childMethod(self) :
        print "Call method of subclass"
        
c = Child()  #Create an instance c of subclass Child
c.childMethod()  #Call method of subclass
c.parentMethod() #Call method of superclass through the instance of a subclass
###############################################################################
# Here is something interesting, be careful about the results printed on screen
c.parentAttr = 300 #in this case, you did not touch the class variable of superclass
print 'c.parentAttr =', c.parentAttr # the only thing you changed is __dict__ profile of subclass
c.getAttr()    #therefore, when you recall superclass method, the attribute is still 100

c.setAttr(200) #Call method of superclass again 
c.getAttr()    #Recall superclass method

