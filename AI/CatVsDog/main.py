import keras
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense,Flatten
from keras.layers import Conv2D,MaxPooling2D
from keras import optimizers
tf.config.list_physical_devices('GPU')
train_data_dir = 'D:/Users/Kaede159/Documents/a/KCT/AI/datasets/train'
test_data_dir = 'D:/Users/Kaede159/Documents/a/KCT/AI/datasets/test'

train_datagen = ImageDataGenerator(rescale= 1.0/255)
test_datagen = ImageDataGenerator(rescale= 1.0/255)

train_generator = train_datagen.flow_from_directory(directory=train_data_dir,target_size= (150,150),batch_size=32,class_mode="binary")
test_generator = test_datagen.flow_from_directory(directory=test_data_dir,target_size=(159,159),batch_size=32,class_mode="binary")

model = Sequential()

model.add(Conv2D(64,kernel_size=(5,5),activation="relu",input_shape = (150,150,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128,kernel_size=(5,5),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(128,kernel_size=(5,5),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(256,activation = "relu"))
model.add(Dense(1,activation = "sigmoid"))

sgd = optimizers.SGD(lr = 0.1)
model.compile(loss = "mean_squared_error",optimizer= sgd,metrics=["accuracy"])

history = model.fit_generator(train_generator,epochs =80,verbose = 1,validation_data=(test_generator),steps_per_epoch=4000/32,validation_steps=1000/32)

