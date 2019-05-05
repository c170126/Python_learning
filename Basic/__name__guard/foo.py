
#To understand how if __name__ works
#Reference: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#This foo.py

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")



"""
Only When Your Module Is the Main Program

If your module is the main program, then it will see that __name__ was indeed set to "__main__" and it calls the two functions, printing the strings "Function A" and "Function B 10.0".

Only When Your Module Is Imported by Another
(instead) If your module is not the main program but was imported by another one, then __name__ will be "foo", not "__main__", and it'll skip the body of the if statement.

"""

