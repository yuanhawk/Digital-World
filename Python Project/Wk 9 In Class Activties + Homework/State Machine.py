# class SM:
#
#     def __init_(self): # self refers to the object instantiation
#         self.state = None
#
#     def start(self):    # starting state
#         self.state = self.start_state
#
    # def step(self, inp):
    #     # Moves state machine to the next stage based on the input
    #     state = self.state
    #     ns, out = self.get_next_values(state, inp), next state (ns) defined by child class
    #     self.state = ns
    #     return out
    #
    # def get_next_values(self, state, inp):
    #     pass

# from libdw.sm import SM
import libdw.sm as sm

class LightBox(sm.SM):
    start_state = 'OFF'

    def get_next_values(self, state, inp):

        if state == 'ON':
            if inp == 1:
                next_state = 'OFF'
                output = 0
            else:
                next_state = 'ON'
                output = 1
        else:
            return next_state, output

        return next_state, output

lb = LightBox() # Instantiation
lb.start() # Apply starting state to the state
print(lb.state)
print(lb.state)
print(lb.step(1))
print(lb.step(1))
print(lb.step(1))
print(lb.step(0))
print(lb.step(1))
print(lb.step(1))
print(lb.step(0))