#here we have all the built-in functions in python, these functions are shared by python 2 and python 3
#(1) abs(x) : return absolute value of a number, the number could be integer, float or complex
z = 3+4j #Define a complex number
magnitude = abs(z)
#(2) all(iterable): return True if all elements of the iterable is true or if the iterable is empty
logic_list_0 = [False, False]
logic_list_1 = [True, False]
logic_list_2 = [True, True]
logic_list_3 = []
logic_judge_0 = all(logic_list_0)
logic_judge_1 = all(logic_list_1)
logic_judge_2 = all(logic_list_2)
logic_judge_3 = all(logic_list_3)
#print logic_judge_0, logic_judge_1, logic_judge_2, logic_judge_3
#(3) any(iterable): return True if any elements of the iterable is true, if the iterable is empty return false
logic_judge_4 = any(logic_list_0)
logic_judge_5 = any(logic_list_1)
logic_judge_6 = any(logic_list_2)
logic_judge_7 = any(logic_list_3)
#print logic_judge_4, logic_judge_5, logic_judge_6, logic_judge_7
#(4) bin(x) : convert an integer to a binary string, e.g. bin(7) will give 0b111, 0b means the value is in binary format
binary7=bin(7)
#print binary7
#(5) bool([x]), return a Boolean value using standard truth test procedure, if x is omitted, it will return false
logic_value_0 = bool()              #False
logic_value_1 = bool(0)             #False
logic_value_2 = bool(99)            #True
logic_value_3 = bool([0,0])         #True
logic_value_4 = bool("string")      #True
#print logic_value_0, logic_value_1, logic_value_2, logic_value_3, logic_value_4
#(6) callable(object), Return True if the object argument appears callable
callable(int) #gives True
callable(1)   #gives False
#(7) chr(i), return a string of one character whose ASCII code is the integer i, note i should not be greater than 255
myStr = chr(97) #myStr = 'a', cauze ASCII code of a is 97