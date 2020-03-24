class Line:
    def __init__(self, c0=0, c1=0):
        self._c0 = c0
        self._c1 = c1

    def __call__(self, x):
        return self._c0 + self._c1 * x

    def table(self, l, r, n):
        x = l  # Start from l
        string = ''

        # boundary cases
        if r < l:  # t > 0
            pass
        if n < 1:  # n -1 = 0 -> xx / 0
            y = self(x)
            string += '%10.2f' % x
            string += '%10.2f' % y
            return string
        if l == r:  # similar to above case
            y = self(x)
            string += '%10.2f' % x
            string += '%10.2f' % y
            return string
        else:
            t = (r - l) / (n - 1)

            while x <= r:
                y = self(x)
                string += '%10.2f' % x
                string += '%10.2f' % y
                string += '\n'
                x += t
            return string

line = Line(3, 4)
print(line(2))
print(line.table(1, 5, 0))