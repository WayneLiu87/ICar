from rrb2 import *

class controller:
    def __init__(self):
        self.rr = RRB2()
        self.speed = 0.3
        self.turn_speed = 0.8
        self.runtime = 1

    def forward(self):
        self.rr.left(self.runtime, self.speed)
        self.rr.set_led1(True)
        self.rr.set_led2(True)

    def reverse(self):
        self.rr.set_led1(True)
        self.rr.set_led2(True)
        self.rr.right(self.runtime, self.speed)

    def right(self):
        self.rr.set_led1(False)
        self.rr.set_led2(True)
        self.rr.forward(self.runtime, self.speed)

    def left(self):
        self.rr.set_led1(False)
        self.rr.set_led2(True)
        self.rr.reverse(self.runtime, self.speed)
