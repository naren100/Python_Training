# Sample App "For Loop"
for countdown in 5, 4, 3, 2, 1, "hey!":
    print(countdown)
# Lists
spells = [
    "Riddikulus!",
    "Wingardium Leviosa!",
    "Avada Kedavra!",
    "Expecto Patronum!",
    "Nox!",
    "Lumos!",
    ]
print(spells[3])

# Python has a built-in interactive interpreter
# Python Data are objects
# Python wraps each data value — booleans, integers, floats, strings,
# Python Object - Has a Type, Unique ID, Value and a reference count
# even large data structures, functions, and programs — in memory as an object.
# Basic Data Types in Python - Integer, Floating point, Complex, Text String, List,
# Tuple. Bytes, ByteArray and Set
###########################################
# What is a Variable?
# What does it mean to Strongly Typed?
# What is Explicit and Implicit Type
# Python is a dynamically-typed language, which means the
# A variable is determined automatically based on
# the value assigned to it. You can simply assign a value to a variable,
# and Python will figure out its type at runtime.
# What is runtime vs Compile Time? - Homework
# Naming and Using Variables
# lowercase letters, Uppercase letters, Digits, underscore - cant begin with digit and reserved words
# Properly name the variable
# A traceback is a record of where the interpreter ran into trouble
# when trying to execute your code.

# How to find list of keywords?
help ("keywords")
# = to assign a value to a variable.
x = 12
y = x + 12
print(y)

a = 12
b = 2
c = "this is a text"
if a == b:
    print(a)
else:
    print("They are not equal")

print(type(a))
print(type(c))

# In Python,especially when we get to mutable objects like lists. Assignment does not copy a value;
# it just attaches a name to the object that contains the data.
# The name is a reference to a thing rather than the thing itself.
# Visualize a name as a tag with a string attached to the object box somewhere else in the computer’s memory

message = "Please do your goals"
print(message)
message = " Jack Please do your goals on time"
print(message)

# STRINGS
# Anything inside quotes is a string
name = "Dave Thomas"
print(name)
print(name.title())  # Title is a method. What is a method?
print(name.upper())
print(name.lower())

naren = dave = mallesh = "What a long day"
print(naren)
print(dave)
print(mallesh)
