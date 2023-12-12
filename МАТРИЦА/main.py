import math
import matrix

def sigma(x):
    return 1 / (1 + math.exp(-x))

I = [[0.2], [0.12], [0.3]]
t = [[0.5], [0.1], [0.75]]
W_i_h = [[0.1, 0.3, 0.4], [0.11, 0.05, 0.6], [0.15, 0.2, 0.22]]
W_h_o = [[0.1, 0.2, 0.05], [0.02, 0.4, 0.13], [0.2, 0.5, 0.09]]

X = matrix.mult(W_i_h, I)
O_h = [[sigma(x[0])] for x in X]

X1 = matrix.mult(W_h_o, O_h)
O_o = [[sigma(x[0])] for x in X1]

E_o = matrix.minus(t, O_o)
E_h = matrix.mult(matrix.transponirovanie(W_h_o), E_o)

dW_h_o = [[0]*len(I) for i in range(len(W_h_o))]
dW_h_o = matrix.multConst(E_o, 0.1)
dW_h_o = matrix.mult(dW_h_o, O_o)
dW_h_o = matrix.mult(dW_h_o, matrix.minusConst(O_o, 1))
print(matrix.transponirovanie(O_h))
dW_h_o = matrix.mult(dW_h_o, matrix.transponirovanie(O_h))
print(dW_h_o)


dw_i_h
a = 0.1



