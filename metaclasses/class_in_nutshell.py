"""
Let's see how a class gets actually created
define a body of class with constructor and methods
create dictionary to have constructor and methods in it.
Create a new class Spam using type method, class name as first
argument, second base classes from which it inherits and pass
clsdict as third argument as dictionary that contains attributes
and functions/methods.
"""

class Base:
	pass

# Class Body
body = '''
def __init__(self, name):
	self.name = name
def bar(self):
	print("I am in Spam.bar")
'''
# Class dictionary
clsdict = type.__prepare__("Spam", (Base,))
exec(body, globals(), clsdict)
print(clsdict)

# Create a class named Spam
Spam = type("Spam", (Base,), clsdict)
print(Spam)
s = Spam("Mat") # call __init__
s.bar() # call bar method