# this is an example showing the dynamic property of python
# Observe the definition of the following function
# and pay attention to the result!

def builder (type, value): # This function will transfer the given variable to the type you want
	return type(value)     # By using python, the realization is extremely terse and totally readable
						   # Basically, this is the powerful dynamic property of python language
	
myStr = '10'
myNum = builder(int, myStr)
print myNum
print type (myNum)

#Another two examples
def impose(func, value):
        return func(value)
		
def anyfunc(value):
        return value*value
