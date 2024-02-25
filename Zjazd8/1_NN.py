import numpy as np
import pandas as pd

#komponenty do budowy sieci
from tensorflow.keras.models import Sequential  #szkielet
from tensorflow.keras.layers import Dense #wszystkie połączenia
from tensorflow.random import set_seed #losowość

set_seed(0)

model = Sequential()
model.add(Dense(4, input_shape=[1], activation='linear'))
model.add(Dense(2, activation='linear'))
model.add(Dense(1))

# kompilacja
model.compile(optizer='rmsprop', loss='mse', metrics=['mae'])


