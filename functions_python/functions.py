# A simple Python function to check
# whether x is even or odd
def square_value(num):
    return num**2
    	
def myFun(x):
    x[0] = 20
   

def evenOdd(x):
	if (x % 2 == 0):
		print ("even")
	else:
		print ("odd")
  
  
def say_Hi():
    	"Hello! master!"

def swap(x, y):
    temp = x
    x = y
    y = temp
    

def student(firstname, lastname):
	print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')
 

# Driver code to call the function
evenOdd(2)
evenOdd(3)
print(say_Hi.__doc__)

print(square_value(2))

print(square_value(-4))

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

x = 2
y = 3
swap(x, y)
print(x)
print(y)


#Special Symbols Used for passing arguments:-
#1.)*args (Non-Keyword Arguments)
#2.)**kwargs (Keyword Arguments)


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


# Python code to illustrate the cube of a number
# using lambda function


def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))

slave_Artemida = lambda x : print("is Artemida slave? ",x)

slave_Artemida(True)
