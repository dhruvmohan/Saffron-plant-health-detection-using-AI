import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

IMAGE_SIZE = (224,224)
BATCH_SIZE = 32
EPOCHS = 15

train_dir = "dataset"


datagen = ImageDataGenerator(rescale=1./255)

 #datagen = ImageDataGenerator(
   #  rescale=1./255,
   #  validation_split=0.2,
  #   rotation_range=20,
   #  zoom_range=0.2,
  #   horizontal_flip=True
 #)

train_data = datagen.flow_from_directory(
    train_dir,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_data = datagen.flow_from_directory(
    train_dir,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
   #  subset='validation'
)

base_model = MobileNetV2(
    include_top=False,
    input_shape=(224,224,3),
    weights='imagenet'
)

base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
output = Dense(6, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# model.fit(train_data, validation_data=val_data, epochs=EPOCHS)

model.fit(train_data, epochs=EPOCHS)


model.save("saffron_model.h5")
