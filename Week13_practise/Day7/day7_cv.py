# Applying Transfer Learning Technique to a Custom Project
# - Project Objective
# -- Leverage transfer learning to solve a specific task in either computer vision or NLP
# -- Fine-tune a pre-trained model for domain-specific data to achieve optimal performance

# - Steps to Follow
# -- Dataset Selection
# --- Computer Vision: Custom image dataset(e.g., animal species classification)
# --- NLP: Text classification task(e.g., sentiment analysis, product categorization)

# -- Pre-Trained Model
# --- Computer Vision: Models like ResNet, EfficientNet, or MobileNet
# --- NLP: BERT, RoBERTa, or T5

# -- Fine-Tuning Techniques
# --- Regularization, hyperparameter tuning, data augmentation, discriminative learning rates

# Analyzing the Fine-Tuning Techniques

# - Fine-Tuning Process
# -- Freeze the pre-trained layers and train the custom classifier head first
# -- unfreeze some pre-trained layers for domain adaptation
# -- Gradually reduce the learning rate to avoid catastrophic forgetting
# 
# - Key Techniques
# -- Regularization
# --- Dropout, L2 regularization to prevent overfitting
# -- Data Augmentation
# --- Enhance diversity in training data(rotation, cropping, or text paraphrasing)
# -- Hyperparameter Tuning
# --- Experiment with learning rate, batch size, and optimizer

# Documenting Results and Baseline Comparisions
# - Steps
# -- Evaluate the baseline performance of the pre-trained model without fine-tuning
# -- Track performance improvements after fine-tuning and hyperparameter optimization
# -- Use metrics like accuracy, F1-score, BLEU, or ROC-AUC to compare results


# Objective:
# - Fine-tune a pre-trained model(ResNet for computer vision or BERT for NLP) to solve a custom task
# - Evaluate and document results against a baseline


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# Data agmentation and preprocessing
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    "PATH To DATASET",
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = datagen.flow_from_directory(
    "PATH To DATASET",
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

base_model = ResNet50(weights="imagenet", include_top=False, input_shape=(224,224,3))

for layer in base_model.layers:
    layer.trainable = False

x = GlobalAveragePooling2D()(base_model.output)
output = Dense(1, activation="sigmoid")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

val_loss, val_accuracy = model.evaluate(val_data)
print(f"Validation Accuracy {val_accuracy}")

