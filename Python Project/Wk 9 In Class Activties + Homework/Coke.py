import libdw.sm as sm

class CM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == 100:
                output = (0, 'coke', 0)
                next_state = 0
            elif inp == 50:
                output = (50, '--', 0)
                next_state = 1
            else:
                output = (0, '--', inp)
                next_state = 0
        else:
            # state is 1, when 50 cent is inside
            if inp == 100:
                output = (0, 'coke', 50)
                next_state = 0
            elif inp == 50:
                output = (0, 'coke', 0)
                next_state = 0
            else:
                output = (50, '--', inp)
                next_state = 1
        return next_state, output

# Object instantiation
cm = CM()
cm.start()
# transduce 1) call start(),
print(cm.transduce([100, 50, 50,10, 50, 80, 100]))
# print(cm.state)
# print(cm.step(100))
# print(cm.step(50))
# print(cm.step(10))
# print(cm.step(50))
# print(cm.step(80))