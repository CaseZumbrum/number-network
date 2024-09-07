from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
import sys
import os
import time

model = load_model("digit_Model")
fileName = 'back_Network/input.txt'
originalTime = os.path.getmtime(fileName)

while(True):
	if(os.path.getmtime(fileName) > originalTime):
		with open(fileName, 'r') as f:
			input1 = f.read().split(","),
		originalTime = os.path.getmtime(fileName)
		max = 0
		for i in range(0, len(input1[0])):
    			input1[0][i] = int(input1[0][i])

		out = model.predict([input1[0]])
		for x in range(10):
			if(out[0][max] < out[0][x]):
				max = x

		with open('back_Network/output.txt', 'w') as f:
    			f.write(str(max))
	time.sleep(1)








