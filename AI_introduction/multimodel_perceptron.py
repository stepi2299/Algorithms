#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# ToDo tu prosze podac pierwsze cyfry numerow indeksow
p = [2, 3]

L_BOUND = -5
U_BOUND = 5
INPUT_SIZE = 100

np.random.seed(1)


def q(x):
    return np.sin(x * np.sqrt(p[0] + 1)) + np.cos(x * np.sqrt(p[1] + 1))


x = np.linspace(L_BOUND, U_BOUND, INPUT_SIZE)
x = x.reshape((1, x.size))
y = q(x)


# f logistyczna jako przykĹad sigmoidalej
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# pochodna fun. 'sigmoid'
def d_sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)


# f. straty
def nloss(y_out, y):
    return (y_out - y) ** 2


# pochodna f. straty
def d_nloss(y_out, y):
    return 2 * (y_out - y)


class DlNet:
    def __init__(self, x: np.ndarray, y: np.ndarray, h_l_size=9, lr=0.003):
        self.x = x
        self.y = y
        self.y_out = 0
        self.input_len = self.x.size

        self.HIDDEN_L_SIZE = h_l_size
        self.LR = lr
        self.w1, self.b1, self.w2,self.b2 = self.initialize()


    def initialize(self):
        W1 = np.random.normal(0, 0.1, size=(self.HIDDEN_L_SIZE, 1))
        b1 = np.zeros(shape=(self.HIDDEN_L_SIZE, 1))
        W2 = np.random.normal(0, 0.1, size=(1, self.HIDDEN_L_SIZE))
        b2 = np.zeros(shape=(1, 1))
        return W1, b1, W2, b2

    def forward(self, x: np.ndarray):
        # calculate output and values in hidden layers
        x1 = np.dot(self.w1, x) + self.b1
        a1 = sigmoid(x1)
        x2 = np.dot(self.w2, a1) + self.b2
        return x1, a1, x2

    def predict(self, x: np.ndarray):
        return self.forward(x)[2]

    def backward(self, x: np.ndarray, y: np.ndarray, a1: np.ndarray, a2: np.ndarray):
        da2 = d_nloss(a2, y)
        dW2 = (1 / self.input_len) * np.matmul(da2, a1.transpose())
        db2 = (1 / self.input_len) * np.sum(da2, axis=1, keepdims=True)
        dx1 = np.matmul(self.w2.transpose(), da2) * d_sigmoid(np.dot(self.w1, x) + self.b1)
        dW1 = np.matmul(dx1, x.transpose())
        db1 = (1 / self.input_len) * np.sum(dx1, axis=1, keepdims=True)
        return dW2, db2, dW1, db1

    def _update(self, dW2, dW1, db2, db1):
        self.w2 = self.w2 - self.LR * dW2
        self.w1 = self.w1 - self.LR * dW1
        self.b2 = self.b2 - self.LR * db2
        self.b1 = self.b1 - self.LR * db1

    def train(self, x_set: np.ndarray, y_set: np.ndarray, iters: int):
        history = []
        for _ in range(0, iters):
            _, a1, x2 = self.forward(x_set)
            history.append(nloss(x2, y_set))
            dw2, db2, dw1, db1 = self.backward(x_set, y_set, a1, x2)
            self._update(dw2, dw1, db2, db1)
        return history



nn = DlNet(x, y, h_l_size=55, lr=0.07)
history = nn.train(x, y, 200000)

x = np.linspace(L_BOUND, U_BOUND, 500)
x = x.reshape((1, x.size))
y = q(x)

yh = nn.predict(x) # ToDo tu umiesciÄ wyniki (y) z sieci

avg_error = np.round(np.average(nloss(yh, y)), 4)
print("Average error: ", avg_error)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x[0], y[0], 'ro', label='Funkcja aproksymowana')
plt.plot(x[0], yh[0], 'bo', label='Aproksymacja')
plt.legend()
plt.show()
