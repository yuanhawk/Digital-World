class Diff:
    def __init__(self, f, h=1e-4):
        self._f = f
        self._h = h

    def __call__(self, x):
        return (self._f(x + self._h) - self._f(x)) / self._h