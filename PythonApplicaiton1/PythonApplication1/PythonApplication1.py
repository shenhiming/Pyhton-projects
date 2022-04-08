#################################################
#                   printf
#################################################
def printf(*args):
    print(*args, end='')
    return;
#################################################
#                   printTab
#################################################
def printTab(*args):
    print("\t", *args)
    return;
#################################################
#                   printfTab
#################################################
def printfTab(*args):
    print("\t", *args, end='')
    return;
#################################################
#                   Add
#################################################
def Add():
    num1 = 1.5
    num2 = 6.302
    # Add two numbers
    sum = num1 + num2
    # Display the sum
    printTab('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    return sum;
#################################################
#                   Sqrt
#################################################
def Sqrt():
    import cmath
    num = 25
    num_sqrt = cmath.sqrt(num)
    printTab('The sqrt of {0} and {1} '.format(num, num_sqrt))
    printTab('The sqrt of {0} and {1} '.format(num, num ** 0.5))
    return; 
#################################################
#                   Random
#################################################
def Random():
    import random
    for i in range(0, 9):
        printfTab(random.randint(0, 99))
    print()
    return;

#################################################
#                   Digit
#################################################
# Python program to convert decimal number into binary, octal and hexadecimal number system
# Change this line for a different result
def Digit():
    dec = 344
    printTab("The decimal value of",dec,"is:")
    printTab(bin(dec),"in binary.")
    printTab(oct(dec),"in octal.")
    printTab(hex(dec),"in hexadecimal.")
    return;
#################################################
#                   RunTurtle
#################################################
def RunTurtle():
    import turtle
    bob = turtle.Turtle()
    printTab(bob)
    turtle.mainloop()
    return;
#################################################
#                   RunTuple
#################################################
def RunTuple():
    t1 = tuple('abcde')
    printTab("t1 = ", t1)
    t2 = ('A',) + t1[1:]
    printTab("t2 = ", t2)
    t1, t2 = t2, t1             #swap
    printTab("swap")
    printTab("t1 = ", t1)
    printTab("t2 = ", t2)
    addr = "monty@python.org"
    uname, domain = addr.split("@");
    printTab("tuname = ", uname, ", domain = ", domain)
    s = "abc"
    t = [0, 1, 2]
    #zip(s, t)
    for pair in zip(s, t):
        printfTab(pair)
    print()
    printTab(list(zip('Anne', 'Elk')))
    d = dict(zip('abc', range(3)))
    printTab(d)
    from structshape import structshape
    t = [1, 2, 3]  
    printTab(structshape(t))
    t2 = [[1, 2], [3, 4], [5, 6]]
    printTab(structshape(t2))
    t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
    printTab(structshape(t3))
    lt = list(zip(t, s))
    printTab(structshape(lt))
    return;
#################################################
#                   RunTool
#################################################
def RunTool():
    import string
    printTab(string.punctuation)
    import random
    for i in range(3):
        x = random.random()
        printTab(x)
    printTab(random.randint(5, 10))
    t1 = [1, 2, 3]
    printTab(random.choice(t1))
    printTab('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
    import os
    printTab("Current working directory is", os.getcwd())
    import pickle
    s = pickle.dumps(t1);
    printTab("pickle.dumps(t) = ", s)
    t2 = pickle.loads(s)
    printTab("pickle.loads(s) = ", t2)
    printTab("t1 == t2 ?", t1 == t2, ", t1 is t2 ?", t1 is t2)
    return;
#################################################
#                   Class Animal
#################################################
class Animal(object):
    from multipledispatch import dispatch
    @dispatch()
    def __init__(self):
        self.name = []
        self.edge = []
        self.__owner = []
    @dispatch(str, int, str)
    def __init__(self, name, edge, owner):
        self.name = name
        self.edge = edge
        self.__owner = owner    # cannot direct access
    def ShowInfomation(self):
        printTab(self.name, self.edge, self.__owner)
#################################################
#                   Class People
#################################################

class People(Animal):
    def __init__(self):
        super(People, self).__init__()
        self.gender = "M";
    def ShowInfomation(self):
        printTab(self.name, self.gender)
class Man(People):
    def __init__(self, gender):
        super(Man, self).__init__(gender)
        self.height = 180
    def ShowInfomation(self):
        a = self.gender
        printTab(self.height)

#################################################
#                   RunClass
#################################################
def RunClass():
    a = Animal("dog", 8, "Louis")
    printTab(a.name, a.edge);
    a.ShowInfomation()
    b = Animal()
    b.ShowInfomation()
    c = People();
    c.ShowInfomation();
    #d = Man("");
    #d.ShowInfomation();
   
    
    return;
#################################################
#                   Main
#################################################

result = Add();
print("result of Add() is", result);
Sqrt();
Random();
Digit();
#RunTurtle();
RunTuple();
RunTool();
RunClass();
