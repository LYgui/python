#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import math

a = float(input('a='))

b = float(input('b='))

c = float(input('c='))


def quadratic(a, b, c):

    x = float((-b+math.sqrt(b**2-4*a*c))/(2*a))

    y = float((-b-math.sqrt(b**2-4*a*c))/(2*a))

    return x, y


print(quadratic(a, b, c))
