import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization
from keras.optimizers import Adam
from keras.utils import to_categorical


# Set random seed for reproducibility
np.random.seed(1000)


if __name__ == '__main__':
    # Load and normalize the dataset
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    width = height = X_train.shape[1]

    X_train = X_train.reshape((X_train.shape[0], width * height)).astype(np.float32) / 255.0
    X_test = X_test.reshape((X_test.shape[0], width * height)).astype(np.float32) / 255.0

    Y_train = to_categorical(Y_train, num_classes=10)
    Y_test = to_categorical(Y_test, num_classes=10)

    # Create model
    model = Sequential()

    model.add(Dense(2048, input_shape=(width * height,)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(Dense(1024))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(Dense(1024))
    model.add(BatchNormalization())
    model.add(Activation('relu'))

    model.add(Dense(10))
    model.add(BatchNormalization())
    model.add(Activation('softmax'))

    # Compile model
    model.compile(optimizer=Adam(lr=0.001, decay=1e-6),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history_bn = model.fit(X_train, Y_train,
                           epochs=200,
                           batch_size=256,
                           validation_data=(X_test, Y_test))

    # Show the results
    fig, ax = plt.subplots(1, 2, figsize=(18, 6))

    fig.suptitle('MLP with Batch Normalization. Adam with learning rate equal to 0.001')

    ax[0].plot(history_bn.history['acc'], label='Training accuracy')
    ax[0].plot(history_bn.history['val_acc'], label='Validation accuracy')
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylabel('Accuracy')
    ax[0].legend()
    ax[0].grid()

    ax[1].plot(history_bn.history['loss'], label='Training loss')
    ax[1].plot(history_bn.history['val_loss'], label='Validation loss')
    ax[1].set_xlabel('Epoch')
    ax[1].set_ylabel('Loss')
    ax[1].set_yticks(np.linspace(0.0, 1.0, 10))
    ax[1].legend()
    ax[1].grid()
    plt.show()