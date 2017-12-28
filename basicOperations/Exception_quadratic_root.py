# This is a script to show the usage of exception handling of python
# It's mainly about solving a quadratic equation when all the coefficients
# are given. The details is self-explained in script
from math import sqrt

print(\
'This program is trying to find real roots \
(if there is any) of a quadratic equation: \
a*x^2+b*x+c=0')

print('\
Please input three coefficients in order of \
a b c, and separated with comma "," ')

try: 
    a,b,c = eval(input('a,b,c='))
    delta = b**2 - 4*a*c
    root_1 = (-b - sqrt(delta) )/(2*a)
    root_2 = (-b + sqrt(delta) )/(2*a)
    print("The roots are",root_1,'and',root_2)
except ValueError as excObj:
    if str(excObj) == "math domain error":
        print("No real roots for given coefficients") 
    else:
        print("You didn't give me real coefficients!")
except ZeroDivisionError:
    print("a=0, this is not quadratic equation")
except NameError:
    print("\nYou didn't enter three numbers.")
except TypeError:
    print("\nYour inputs were not all numbers")
except SyntaxError:
    print("\nYou didn't input number in right format, check it again")
except:
    print("\nSomething went wrong, sorry...")

