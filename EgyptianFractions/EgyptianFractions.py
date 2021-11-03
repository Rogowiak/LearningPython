#An Egyptian fraction is the sum of finitely many rational numbers, each of which can be expressed in the form 1/q, where q is a positive integer.
#For example, the Egyptian fraction 61/66 can be written as 61/66 = 1/2 + 1/3 + 1/11


def EuclidesDivision(a,b):  #Will be used later to get the greatest common divisor to reduce the fractions
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a 
    else:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    return EuclidesDivision(a,b)

class fraction: #defining the fraction class
    def __init__(self, counter, denominator):
        self.counter = counter
        self.denominator = denominator

    def __sub__(self, other): #overloading "-" operator
        if self.denominator == other.denominator:
            cnt = self.counter - other.counter
            fr = fraction(cnt, self.denominator)
            return fr.reduce()
        else:
            self.counter *= other.denominator
            other.counter *= self.denominator
            self.denominator *= other.denominator
            cnt = self.counter - other.counter
            fr = fraction(cnt, self.denominator)
            return fr.reduce()
   
    def reduce(self):
        divider = EuclidesDivision(self.counter, self.denominator)
        if divider == 1:
            return self
        else:
            self.counter /= divider
            self.denominator /= divider
            return self

    def print(self):
        print(self.counter, '/',self.denominator)


ułamek = fraction(1,4)
ułamek.print()
ułamek2 = fraction(1,2)
ułamek2.print()
ułamek3 = fraction(1,5) - fraction(1,10)
ułamek3.print()

    


    

