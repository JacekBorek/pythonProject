import random

random.seed(10)
print(random.random())
random.seed(0)
print(random.random())
random.seed(10)
print(random.random())

set_seed(10)

model = Sequential()
model.add(Dense(4, input_shape=[1], activation='linear'))