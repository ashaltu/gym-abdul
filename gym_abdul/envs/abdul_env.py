import gym
import math
import random
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
from sympy.solvers import solve
from sympy import Symbol

"""
Mini-Assignment #2: Create a gym environment for 2 functions
that intersect at least once, the agent can move along
the x-axis in either direction, but doesn’t know where it is. 
The agent gets a reward when it finds an x coordinate where the 
functions intersect. The agent only knows the difference of the 
functions at its location on the x-axis.

Default Equations:
    y= -x^2 - x + 1
    y= x

Observation: |y1 - y2| where y1 and y2 are functions that intersect at least once
Action: delta x (-5.0 to 5.0)
"""


class AbdulEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def diff(self, T, x):
        y1 = T[0]*(x**2) + T[1]*x + T[2]
        y2 = T[3]*x
        return math.fabs(y1-y2)

    def intersect(self):
        y1 = self.A[0]*(self.x**2) + self.A[1]*self.x + self.A[2]
        y2 = self.A[3]*self.x
        is_intersection = True if y1 == y2 else False
        if is_intersection:
            return True
        return False

    def reward_system(self):
        if self.intersect():
            return 100
        return 0

    def __init__(self, new_variables=False):
        generated = False
        self.new_variables = new_variables
        self.A = np.array([-1, -1, 1, 1])
        self.step = 0
        if self.new_variables:
            while not generated:
                A = np.random.uniform(-4, 4, 4)
                theta = Symbol('x')
                size = len(solve(A[0]*(theta**2)+A[1] *
                                 (theta)+A[2] - [3]*theta, theta))
                generated = True if size > 0 else False
        self.A = A if generated else self.A
        self.x = random.uniform(-1.0, 1.0)
        self.dif = self.diff(self.A, self.x)

    def step(self, action):
        self.x += action
        self.step += 1
        self.dif = self.diff(self.A, self.x)
        reward = 1 if self.intersect() else False
        return self.dif, self.reward_system, self.intersect(), {}

    def reset(self):
        generated = False
        if self.new_variables:
            while not generated:
                A = np.random.uniform(-4, 4, 4)
                theta = Symbol('x')
                size = len(solve(A[0]*(theta**2)+A[1] *
                                 (theta)+A[2] - [3]*theta, theta))
                generated = True if size > 0 else False
        self.A = A if generated else self.A
        self.step = 0
        self.x = random.uniform(-1.0, 1.0)
        self.dif = self.diff(self.A, self.x)
        return [self.dif], 0 , False, {}

    def render(self, mode='human', close=False):
        print("x:", self.x, "\ty1-y2:", self.dif)
