class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    

    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    
cal = Calculator(6, 2)
add = cal.addition()
print("The summation of numbers:" , add)

cal = Calculator(6, 2)
sub = cal.subtraction()
print("The difference of numbers:" , sub)

cal = Calculator(6, 2)
mul = cal.multiplication()
print("The product of numbers:" , mul)

cal = Calculator(6, 2)
div = cal.division()
print("The quotient of numbers:" , div)
