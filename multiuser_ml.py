import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.optimizers import Adam
from sklearn import preprocessing
import matplotlib.pyplot as plt

#
mm_scaler = preprocessing.MinMaxScaler()

# numpy 2D data array preparation #
train = pd.read_csv('finaldata_training1.csv')
test = pd.read_csv('finaldata_testing1.csv')

target_train = train['network']
target_train = pd.DataFrame(target_train).to_numpy()

features_train = train.drop(columns='network')
features_train = pd.DataFrame(features_train).to_numpy()

target_test = test['network']
target_test = pd.DataFrame(target_test).to_numpy()

features_test = test.drop(columns='network')
features_test = pd.DataFrame(features_test).to_numpy()

# print(features_train.shape)
# print(features_test.shape)
## 2D to 3D arrays ##

features_train_minmax = mm_scaler.fit_transform(features_train)
mm_scaler.transform(features_test)

X_train = features_train.reshape(400, 10, 35)
X_test = features_test.reshape(100, 10, 35)

target_train = target_train.reshape(400, 1, 10)
target_test = target_test.reshape(100, 1, 10)

Y_train = []
Y_test = []

for i in range(400):
    Y_train.append(target_train[i][0][0])

for i in range(100):
    Y_test.append(target_test[i][0][0])

Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# Building the model #
np.random.seed(12345)

model = Sequential()
model.add(LSTM(256, input_shape=(10, 35), activation='relu', return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(4, activation='softmax'))

## defining the optimizer and compiling the model ##

opt = Adam(learning_rate=1e-2, decay=1e-3)
model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

history = model.fit(X_train, Y_train, epochs=100, validation_data=(X_test, Y_test))
print(model.summary())

## Getting model accuracy ##
score, acc = model.evaluate(X_test, Y_test, verbose=2)
print('The ' + model.metrics_names[1] + ' of this model is ' + str(acc * 100)[:5] + ' %')
print('The ' + model.metrics_names[0] + ' of this model is ' + str(score)[:7])

# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
