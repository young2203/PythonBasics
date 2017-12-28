def helloFunc():
    print "Hello world!"
    
def newWorld():
    print "New world!"
    
print "Guess will I be printed?"
import sys
print sys.argv[0]

import os
myrealpath = os.path.realpath(__file__)
print "my real path" + myrealpath
myabspath = os.path.abspath(__file__)
print "my abs path" + myabspath