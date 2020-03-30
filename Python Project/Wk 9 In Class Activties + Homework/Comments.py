import libdw.sm as sm

class CommentsSM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        if state == 0:
            if inp == '#':
                next_state = 1
                output = "#"
                return next_state, output
            else:
                next_state = 0
                output = None
                return next_state, output
        elif state == 1:
            if inp == '\n':
                next_state = 0
                output = None
                return next_state, output
            else:
                next_state = 1
                output = inp
                return next_state, output
        else:
            return None