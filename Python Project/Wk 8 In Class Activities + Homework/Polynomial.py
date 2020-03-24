class Polynomial:
    def __init__(self, lst):
        self.coeff = [x for x in lst]

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            addition = Polynomial(self.coeff)
            for i in range(len(self.coeff)):
                try:
                    addition.coeff[i] = self.coeff[i] + other.coeff[i]
                except:
                    break
            return addition

        else:
            addition = Polynomial(other.coeff)
            for i in range(len(other.coeff)):
                try:
                    addition.coeff[i] = self.coeff[i] + other.coeff[i]
                except:
                    break

            return addition

    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            subtraction = Polynomial(self.coeff)
            for i in range(len(self.coeff)):
                try:
                    subtraction.coeff[i] = self.coeff[i] - other.coeff[i]
                except:
                    break
            return subtraction

        else:
            subtraction = Polynomial(other.coeff)
            for i in range(len(other.coeff)):
                try:
                    subtraction.coeff[i] = self.coeff[i] - other.coeff[i]
                except:
                    subtraction.coeff[i] = -other.coeff[i]

            return subtraction

    def __call__(self, x):
        total = self.coeff[0]

        for i in range(1, len(self.coeff)):
            total += self.coeff[i] * x ** i

        return total

    def __mul__(self, other):
        product = Polynomial([0 for i in range(1, len(self.coeff) + len(other.coeff))])

        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                product.coeff[i + j] += self.coeff[i] * other.coeff[j]

        return product

    def differentiate(self):
        for i in range(len(self.coeff) - 1):
            self.coeff[i] = self.coeff[i + 1] * (i + 1)

        self.coeff.pop()

        return None

    def derivative(self):
        product = Polynomial([0 for x in range(len(self.coeff) - 1)])

        for i in range(len(product.coeff)):
            product.coeff[i] = self.coeff[i + 1] * (i + 1)

        return product