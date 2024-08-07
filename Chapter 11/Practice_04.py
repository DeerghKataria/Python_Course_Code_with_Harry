class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    # For adding two complex number
    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    # For multiplying two complex numbers
    def __mul__(self, c):
        # Formula: (a + bi)(c +di) = (ac - bd) + (ad + bc)i
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImag = self.real * c.imaginary + self.imaginary * c.real

        return Complex(mulReal, mulImag)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(1, -4)
c2 = Complex(331, -37)

print(c1+c2)
print(c1*c2)
