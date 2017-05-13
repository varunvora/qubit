#Simulation of a quantum computer
#All function names are in camel case, and then prefixed with 'q'
#Alpha beta Convention taken from Michael Nielsen's Youtube series 'Quantum Computing for the Determined'

from random import random
class qubit(object) :
    def __init__(self) :
        self.alpha = random()
        self.beta = (1 - self.alpha**2)**0.5
    
    def qisValid(self, a, b) :
        if ((a**2 + b**2) > 1) or (a < 0) or (b < 0) or (a > 1) or (b > 1):
            return False
        else :
            return True
    def qset(self, a, b) :
        if self.qisValid(a, b):
            self.alpha = a
            self.beta = b
            return True
        else :
            return False
    
    def qnot(self):
        self.alpha, self.beta = self.beta, self.alpha
    
    def qgetStates(self) :
        return self.alpha, self.beta

    def qgetAlpha(self) :
        return self.alpha
 
    def qgetBeta(self) :
        return self.beta


a = qubit()
print(a.qgetStates())
a.qnot()
print(a.qgetStates())
a.qset(0.6, 0.8)
print(a.qgetStates())
a.qnot()
print(a.qgetStates())

'''
Float precision is only upto 16 decimal places which is going to be a drawback later
So I plan on making the '0.' irrelevant and make use of the infinite (i think) integer precision
that python offers. First priority is to get the fundamentals are right
'''