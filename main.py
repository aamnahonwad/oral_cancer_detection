import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# 📁 Dataset paths
train_dir = "dataset/train"
val_dir = "dataset/val"

# 🔄 Image generators (with augmentation)
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'   # 🔥 important (for 3 classes)
)

val = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# 🧠 Load MobileNetV2
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# 🔥 Freeze first layers
for layer in base_model.layers[:-30]:
    layer.trainable = False

# 🔥 Custom head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(train.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=outputs)

# ⚙️ Compile
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# 📉 Callbacks
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.3,
    patience=3,
    min_lr=1e-6
)

# 🚀 Train
history = model.fit(
    train,
    validation_data=val,
    epochs=20,
    callbacks=[early_stop, reduce_lr]
)

# 📊 Evaluate
loss, acc = model.evaluate(val)
print(f"Validation Accuracy: {acc * 100:.2f}%")

# 💾 Save model
model.save("oral_model.keras")

print("✅ Model training complete and saved!")