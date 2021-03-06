import numpy as np
from step01 import Variable
from step02 import Function

#수치미분
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)

    return (y1.data - y0.data) / (2 * eps)

from step02 import Square

f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f, x)

print(dy)#4.000000000004

from step03 import Exp

def f2(x):
    A = Square()
    B = Exp()
    C = Square()

    return C(B(A(x)))

x = Variable(np.array(0.5))
dy = numerical_diff(f2, x)

print(dy)#3.2974426293330694