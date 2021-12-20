import numpy as np

X = np.array(([2,9],[1,5],[3,6]),dtype = float)
y = np.array(([92],[86],[89]),dtype = float)

X = X / np.amax(X,axis = 0)
y = y/100

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

epochs = 5000
lr = 0.01

neuron_i = 2
neuron_h = 3
neuron_o = 1

weight_h = np.random.uniform(size = (neuron_i,neuron_h))
bias_h = np.random.uniform(size = (1,neuron_h))
weight_o = np.random.uniform(size = (neuron_h,neuron_o))
bias_o = np.random.uniform(size = (1,neuron_o))


for i in range(epochs):
    
    inp_h = np.dot(X,weight_h) + bias_h
    out_h = sigmoid(inp_h)
    
    inp_o = np.dot(out_h,weight_o) + bias_o
    out_o = sigmoid(inp_o)
    
    err_o = y - out_o
    grad_o = derivative_sigmoid(out_o)
    delta_o = err_o * grad_o
    
    err_h = delta_o.dot(weight_o.T)
    grad_h = derivative_sigmoid(out_h)
    delta_h = err_h * grad_h
    
    weight_o += out_h.T.dot(delta_o) * lr
    weight_h = X.T.dot(delta_h) * lr
    

print("Input :: ",X)
print("Actual : " , y)
print("Predicted : " , out_o)