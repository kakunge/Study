import numpy as np

def step_function1(x):#간단한 계단 함수
    if x > 0:
        return 1
    else:
        return 0
#넘파이 배열 사용 불가

def step_function2(x):#넘파이 배열 사용
    y = x > 0
    return y.astype(np.int)
#astype()은 넘파이 배열의 자료형을 바꿔준다

#시그모이드 함수 : 신경망에서 자주 쓰이는 활성화 함수의 하나
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#신경망에서 활성화 함수로 선형 함수를 사용하게 되면 신경망을 여러 층으로 구성하는 이점이 없기 때문에 활성화 함수는 반드시 비선형 함수를 이용해야 한다.

#ReLU 함수 : 입력이 0을 넘으면 입력을 그대로 출력하고, 0 이하이면 0을 출력
def ReLU(x):
    return np.maximum(0, x)

#넘파이를 이용한 행렬 계산과 신경망 신호 전달

#항등 함수
def identity_function(x):
    return x

#3층 신경망
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([0.1, 0.5])
y = forward(network, x)
print(y)#[0.31234736 0.6863161 ]