import libdw.sm as sm

class SimpleAccount(sm.SM):
    start_state = 0

    def __init__(self, init_bal): #initialise with some values
        self.start_state = init_bal

    def get_next_values(self, state, inp):
        if state < 100 and inp < 0:
            next_state = state + inp - 5
            output = next_state
        else:
            next_state = state + inp
            output = next_state
        return next_state, output

acct = SimpleAccount(110)
acct.start()
# transduce 1) call start(),
print(acct.transduce([10, -25, -10, -5, 20, 20]))