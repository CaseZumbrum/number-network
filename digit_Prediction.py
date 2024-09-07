from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import sparse_categorical_crossentropy
#load the dataset
dataset = loadtxt('digit_Data.csv', delimiter = ',')
x = dataset[:,1:]
y = dataset[:,0]

#define the model
model = Sequential()
model.add(Dense(256,activation = 'relu'))
model.add(Dense(128,activation = 'relu'))
model.add(Dense(64,activation = 'relu'))
model.add(Dense(64,activation = 'relu'))
model.add(Dense(10,activation = 'softmax'))

#compile the model
model.compile(loss= sparse_categorical_crossentropy, optimizer='adam', metrics=['accuracy'])

#fit the model to the dataset (the real network thingy)
model.fit(x,y, epochs = 10, batch_size = 100)
model.save("digit_Model")

#determine accuracy
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))


