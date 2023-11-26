#helloworld

print("This line will be printed.")

#variablesandtypes

#ints
myint = 7
print(myint)

#floats
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#excercise
# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)