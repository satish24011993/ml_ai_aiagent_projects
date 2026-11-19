# Popular Pre-Trained NLP Models

# - BERT(Bidirectional Encoder Representations from Transformers)
# -- Architecture: Transformer-based encoder model
# -- Training Tasks
# --- Masked Language Modeling(MLM)
# --- Next Sentence Prediction(NSP)
# -- Applications
# --- Text classification, sentiment analysis, question answering

# - GPT(Generative Pretrained Transformer)
# -- Architecture: Transformer-based decoder model
# -- Training Task
# --- Casual Language Modeling(predicting next word)
# -- Applications
# --- Text generation, summarization, dialogue systems

# - T5(Text-to-Text Transfer Transformer)
# -- Treats all NLP tasks as text-to-text transformations
# -- Applications
# --- Summarization, translation, text classification

# - RoBerta(Robustly Optimized BERT)
# -- Remove Next Sentence Prediction
# -- Pre-trained on a larger dataset with optimized training strategies
# -- Applications
# --- Similar to BERT but with better performance on downstream tasks


# Tokenization and Text Preprocessing for Fine-Tuning NLP Models

# - Tokenization
# -- Converts raw text into numerical representations
# -- Types
# --- WordPiece Tokenization: Used in BERT
# --- Byte-Pair Encoding(BPE): Used in GPT and RoBERTa

# - Text Preprocessing
# -- Cleaning
# --- Remove unnecessary characters(e.g., URLs, special symbols)
# -- Normalization
# --- Convert text to lowercase
# --- Remove stopwords if necessary
# -- Tokenization
# --- Break text into tokens compatible with the pre-trained model


# Adapting Pre-Trained Models for NLP Tasks
# - Common Tasks
# -- Text Classification
# --- Categorize text into predefined labels(e.g., positive/negative sentiment)
# -- Sentiment Analysis
# --- Determine the sentiment polarity of text(e.g., positive, neutral, negative)
# -- Summarization
# --- Generate consice summaries from lengthy texts

# - Steps
# -- Load pre-trained model
# -- Add a task-specific head(e.g., classification layer)
# -- Fine-tune the model on task-specific data.

# Objective: 
# -Fine-tune a pre-trained BERT or T5 model for sentiment analysis using Hugging Face's
#  Transformers library

# -Preprocess the text data, tokenize it, and evaluate the model


# pip install transformers and datasets

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

dataset = load_dataset("imdb")

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding='max_length', max_length=120)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
tokenized_datasets = tokenized_datasets.remove_columns(["text"])
tokenized_datasets = tokenized_datasets.rename_column("label",'labels')
tokenized_datasets.set_format("torch")

train_dataset = tokenized_datasets['train']
test_dataset = tokenized_datasets['test']

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased",num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset = test_dataset,
    processing_class=tokenizer
)

trainer.train()

results = trainer.evaluate()
print(f"Evaluation Results: {results}")
