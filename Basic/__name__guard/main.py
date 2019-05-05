
#This is main.py
#It imports foo, but it will not call function A and B in foo

import foo

if __name__ == "__main__":
    print("welcome to main")


"""
Why Does It Work This Way?

You might naturally wonder why anybody would want this. Well, sometimes you want to write a .py file that can be both used by other programs and modules as a module and can be run as the main program. Examples:

Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.
Your module is only used as a main program, but it has some unit tests, and the testing framework works by importing .py files like your script and running special test functions. You don't want it to try running the script just because it's importing the module.
Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.
Beyond those examples, it's elegant that running a script in Python is just setting up a few magic variables and importing the script. "Running" the script is a side effect of importing the script's module.

"""
