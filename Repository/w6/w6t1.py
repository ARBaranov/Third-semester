class Complex:
    __a = None
    __b = None
    def __init__(self, Re, Im):
        self.__a = Re
        self.__b = Im
    def __str__(self):
        if self.__b < 0:
            return (str(self.__a) + ' ' + str(self.__b)+'i')
        if self.__b == 0:
            return (str(self.__a))
        return (str(self.__a) + ' ' + str(self.__b)+'i')
    def __addition__(self, other):
        return Complex(self.__a + other.__a, self.__b + other.__b)
    def __multiplication__(self, other):
        return Complex((self.__a*other.__a - self.__b*other.__b) + (self.__a*other.__a + self.__b*other.__b)+'i')
    def __substraction__(self, other):
        return Complex((self.__a - other.__a) + (self.__b - other.__b)+'i')
    def __division__(self, other):
        return Complex(((self.__a*other.__a + self.__b*other.__b)/(other.__a**2 +other.__b**2)) + ((other.__a*self.__b - self.__a*other.__b)/(other.__a**2 + other.__b*2))+'i')

    def __pow__(self, power, modulo=None):
        a = self
        print(power)
        for i in range(power - 1):
            a = a.__multiplication__(self)
        return a
    def __neg__(self):
        return Complex(self.__a - self.__b)
    def __abs__(self):
        return Complex(self.__a**2 + self.__b**2)**0.5
