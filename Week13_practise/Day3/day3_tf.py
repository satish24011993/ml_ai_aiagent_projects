# FineTuning techniques in Computer Vision

# - Feature Extraction in Pre-Trained Models
# -- Early layer capture low-level features(eg., edges, textures)
# -- Middle layers capture mid-level features(e.g., edges, textures)
# -- Late layers capture high-level features(e.g., specific objects, task-specific patterns)

# - Choosing Layers to Fine-Tune
# -- Freeze Early Layers: Retain general features learned during pre-training
# -- Unfreeze Late Layers: Allow the model to adapt high-level features to the new task

# - Best Practices
# -- For small datasets: Fine-tune only the last few layers
# -- For large datasets: Unfreeze more layers and fine-tune with a smaller learning rate

# Data Augmentation for Improving Generalization
# - What is Data Augmentation?
# -- Artificially increase the diversity of training data by applying transformations like:
# --- Like Rotation|Horizontal/vertical flipping|Scaling/zooming|Cropping|Color jittering
# - Why Use Data Augmentation?
# -- Reduces overfitting by introducing variability
# -- Improves the model's ability to generalize to unseen data
# - Examples of Augmentation
# -- Rotation: Rotate images by random degrees(e.g.,+/- 15 degrees)
# -- Flip: Apply horizontal/vertical flips
# -- Zoom: Randomly zoom in/out on images

# Hyperparameter Tuning for Transfer Learning
# - Key Hyperparameters

# -- Learning Rate

# --- A smaller learning rate is recommended for fine-tuning pre-trained models
# --- Too large: Overshoots the optimal solution
# --- Too small: Slow convergence

# -- Batch Size

# --- Larger batches stabilize training but require more memory
# --- Smaller batches may lead to noisier updates but help with resource constraints

# -- Optimizer

# --- SGD: Works well with transfer learning when paired with momentum
# --- Adam: Faster convergence but may require fine-tuning for stability

# -- Tuning Process

# --- Start with default settings(eg., learning rate: 1e-4, batch size: 32)

# Objective: Apply data augmentation to a dataset and train a fine-tuned model.
# Experiment with hypeparameters to observe their impact on performance.

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDatagenerator

# Load pretrained MobileNetV2
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))

# Freeze all the layers
for layer in base_model.layers:
    layer.trainable=False

# Add Classification head
x = GlobalAveragePooling2D()(base_model.output)
output = Dense(5, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=output)

# Define data augmentation
datagen = ImageDatagenerator(
    rescale=1./255,
    rotation_range=20,
    width_shape_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    "PATH_TO_DATASET",
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

val_data = datagen.flow_from_directory(
    "PATH_TO_DATASET",
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5), loss='categorical_crossentropy', metrics='accuracy')

# Train the model
history = model.fit(
    train_data, validation_data=val_data, epochs=10, steps_per_epoch=len(train_data),
    validation_steps=len(val_data)
)


