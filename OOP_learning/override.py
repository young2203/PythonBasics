#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This script is used to show the override property of python
# As you can see, we have defined a method named myMethod inside superclass
# while we also re-define it in subclass with same name but with different
# functionality. When we call this method through an instance of subclass (Child),
# we are actually running the method defined in subclass body, and has nothing
# to do with the method in superclass with the same name
# This is so-called override (重载)
# Another thing worth to mention here is that there is no explicit
# definition of __init__ method here, that because python compiler
# will automatically add it as:
# def __init__:
#   pass
# pass will do nothing, but it will make class definition complete
class Parent :
    def myMethod(self) :
        print "Call method of superclass"

class Child (Parent) :
    def myMethod(self) :
        print "Call method of subclass 重载"
        
c = Child()
c.myMethod()
