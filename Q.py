#Simulation of a quantum computer
#All function names are in camel case, and then prefixed with 'q'
#Alpha beta Convention taken from Michael Nielsen's Youtube series 'Quantum Computing for the Determined'

from random import random, randint
class qubit(object) :
    def __init__(self) :
        self.alpha = random()
        self.beta = (1 - self.alpha**2)**0.5
        self.measured = False
    
    def isValid(self, a, b) :
        if ((a**2 + b**2) > 1) or (a < 0) or (b < 0) or (a > 1) or (b > 1) or self.measured:
            return False
        else :
            return True
    def setStates(self, a, b) :
        if self.isValid(a, b) and not self.measured:
            self.alpha = a
            self.beta = b
            return True
        else :
            return False
    def getStates(self) :
        #only for verification, remove in end
        if not self.measured :
            return self.alpha, self.beta
        else :
            return False
    def negate(self):
        if not self.measured :
            self.alpha, self.beta = self.beta, self.alpha

    def hadamard(self) :
        if self.measured :
            return
        root2 = 2**0.5
        a = self.alpha + self.beta
        b = self.alpha - self.beta
        self.alpha = a/root2
        self.beta = b/root2
    
    def measure(self) :
        #not accurate probabilites
        if not self.measured :
            lim = 5 #10^lim will be the size of list
            proba = int(str(self.alpha**2)[2:lim+2])
            probb = 10**lim - proba
            L = [0 for x in range(proba)]
            for i in range(probb) : L.insert(randint(0, 10**lim-1), 1)
            result = L[randint(0, 10**lim-1)]
            self.measured = True #You lose the values of alpha and beta now
            del self.alpha
            del self.beta
            return result


a = qubit()
print(a.getStates())
print(a.measure())

'''
Float precision is only upto 16 decimal places which is going to be a drawback later
So I plan on making the '0.' irrelevant and make use of the infinite (i think) integer precision
that python offers. First priority is to get the fundamentals are right
'''
