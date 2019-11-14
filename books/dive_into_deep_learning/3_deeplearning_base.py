from mxnet import nd
from time import time

a = nd.ones(shape=1000)
b = nd.ones(shape=1000)

### scalar calculation
start = time()
c = nd.zeros(shape=1000)
for i in range(1000):
    c[i] = a[i] + b[i]
cost_time = time() - start
print(cost_time) #0.06046462059020996

### vector calculation
start = time()
d = a + b
cost_time  = time() - start
print(cost_time) #1.4781951904296875e-05


### 线性回归从零开始实现 liner regression is implemented from scratch

from IPython import display
import matplotlib.pyplot as plt
from mxnet import nd, autograd
import random

# 构造真实数据 constructing real data
num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = nd.random.normal(loc=0,scale=1,shape=(num_examples, num_inputs))
labels = true_w[0] * features[:,0] + true_w[1] * features[:,1] + true_b
#print(features)
#print(labels)
labels = labels + nd.random.normal(loc=0,scale=0.01, shape=labels.shape)


def use_svg_display():
    # display by vector graphics
    display.set_matplotlib_formats("svg")

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # set the graphic's size
    plt.rcParams["figure.figsize"] = figsize

set_figsize()
plt.scatter(features[:,0].asnumpy(), labels.asnumpy(),s=1)
plt.show()


### read dataset
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    #print(indices[0:10]) # [530, 883, 76, 572, 830, 441, 685, 19, 663, 563]
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i: min(batch_size + i, num_examples)])
        # 根据索引返回对应的元素return the corresponding element according to the index
        yield features.take(j), labels.take(j)

for X, y in data_iter(10, features, labels):
    print(X, y)
    break


### 初始化模型参数 initialize the model parameters
w = nd.random.normal(loc=0, scale=0.1, shape=(num_inputs,1))
b = nd.zeros(shape=(1,))


