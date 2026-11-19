# Understanding Domain Adaptation and Handling Domain-Specific Data
# - What is Domain Adaptation?
# -- Domain adaptation involves transferring a model trained on one domain(source domain) 
# to perform tasks in a different domain(target domain)
# - Example
# -- Source domain: General news articles
# -- Target domain: Medical Text

# Understanding Domain Adaptation and Handling Domain-Specific Data
# - Why Domain Adaptation?
# -- Many real-world tasks involve domain-specific data
# -- Pre-trained models on general datasets might not perform optimally without adaptation
# - Steps in Domain Adaptation
# -- Fine-tune the pre-trained model on a domain-specific dataset
# -- Incorporate domain-specific embeddings or vocabulary
# -- Apply additional pre-training on the domain data if necessary

# Challenges in Transfer Learning
# - Data Mismatch
# -- The source domain may not represent the target domain adequately
# -- Example: General text(Wikipedia)vs. technical medical jargon
# - Catastrophic Forgetting
# -- During fine-tuning, the model may forget the knowledge learned from the source domain
# - Computational Constraints
# -- Fine-tuning large pre-trained models(e.g., BERT, GPT) requires significant computational resources

# Strategies to Address Challenges
# - Transfer Learning from Related Domains
# -- Fine-tune on an intermediate domain dataset before adapting to the target domain
# - Data Augmentation
# -- Generate synthetic domain-specific data to augment the target dataset
# -- Example
# --- Use paraphrasing techniques to increase dataset diversity
# - Domain-Specific Embeddings
# -- Use pre-trained embeddings tailored to the target domain
# (e.g., BioBERT for biomedical data, LegalBERT for legal text)


# Objective
# - Fine-tune a pre-trained model on a domain-specific dataset(e.g., BERT for medical text
# classification) and experiment with domain-specific embeddings


from datasets import load_dataset

# Load PubMed 20k RCT dataset
dataset = load_dataset("armanc/pubmed-rct20k")
print(dataset['train'][0])

from transformers import AutoTokenizer

# Load BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def preprocess_data(examples):
    return tokenizer(examples['text'], truncation=True, padding="max_length", max_length=512)

tokenized_datasets = dataset.map(preprocess_data, batched=True)
tokenized_datasets = tokenized_datasets.rename_column("label","labels")
tokenized_datasets.set_format("torch")

from transformers import AutoModelForSequenceClassification

# model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=5)

model = AutoModelForSequenceClassification.from_pretrained('dmis-lab/biobert-base-cased-v1.1', num_labels=5)

from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01
)


from transformers import Trainer

trainer=Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset = tokenized_datasets['validation'],
    tokenizer=tokenizer
)

trainer.train()

# Evaluate Model
results = trainer.evaluate()
print(f"Evaluation Results: {results}")

import random

def augment_text(text):
    synonyms = {
        "cancer":["tumor", "malignancy"], "study":["research", "experiment"],
    }
    words=text.split()
    new_words = [random.choice(synonyms[word]) if word in synonyms else word for word in words]
    return " ".join(new_words)

augmented_data = [augment_text(sample["text"]) for sample in dataset["train"]]
print(augmented_data[:5])

