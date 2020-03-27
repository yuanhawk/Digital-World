from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world

class MySMClass(sm.SM):
    start_state = io.Action(0, 0)

    def get_next_values(self, state, inp):
        # These two lines is to stop the robot
        # by pressing the backward button.
        # This only works when using the real robot.
        # It will not work in simulator.
        if inp.button_backward:
            return 'halt', io.Action(0, 0)
        #####################################

        states = ['start', 'next']

        ground = inp.prox_ground.reflected
        # ground = inp.prox_ground.ambiant

        # ground = inp.prox_ground.delta

        # define White and Black based on the sensor data
        left = 'white' if ground[0] > 400 else 'black'
        right = 'white' if ground[1] > 400 else 'black'

        print(left,right)
        next_state = 'start'



        # reach white
        if state == 'start':
            if left == 'black' or right == 'black':
                return 'next', io.Action(0.01, 0.2)
            else:
                return 'start', io.Action(0.05,0)


        elif state == 'next':
            if left == 'white' and right == 'black':
                return 'next', io.Action(0.05, 0)
            elif left == 'black' and right == 'white':
                return 'next', io.Action(0.05, 0)
            elif left == 'white' and right == 'white':
                return 'next', io.Action(0.005, -0.2)
            elif left == 'black' and right == 'black':
                return 'next', io.Action(0.005, 0.2)



        return next_state, io.Action(fv=0, rv=0)

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self, state):
        if state == 'halt':
            return True
        else:
            return False

MySM = MySMClass()

############################

m = ThymioSMReal(MySM, thymio_world)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()