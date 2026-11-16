# from datasets import load_dataset
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer

# # Load dataset for summarization
# dataset = load_dataset("abisee/cnn_dailymail","3.0.0")
# print(dataset['train'][0])

# # For translation
# # dataset = load_dataset("wmt14", "en-fr")

# # Load tokenizer
# tokenizer = AutoTokenizer.from_pretrained("t5-small")

# # Tokenize for summarization
# def tokenize_function(examples):
#     inputs = ["summarize: "+ doc for doc in examples["article"]]
#     model_inputs = tokenizer(inputs, max_length=512, truncation=True)

#     # Tokenize targets
#     # with tokenizer.as_target_tokenizer():
#     #     labels = tokenizer(examples["highlights"], max_length=150, truncation=True)
#     labels = tokenizer(text_target=examples["highlights"], max_length=128, truncation=True)

#     model_inputs['labels'] = labels['input_ids']
#     return model_inputs


# tokenized_datasets = dataset.map(tokenize_function, batched=True)


# model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

# training_args=TrainingArguments(
#     output_dir="./results",
#     eval_strategy="epoch",
#     learning_rate=2e-5,
#     per_device_eval_batch_size=8,
#     per_device_train_batch_size=8,
#     num_train_epochs=3,
#     weight_decay=0.01,
#     save_total_limit=2,
#     predict_with_generate=True
# )

# trainer=Trainer(
#     model = model,
#     args = training_args,
#     train_dataset=tokenized_datasets['train'],
#     eval_dataset=tokenized_datasets['validation'],
#     processing_class=tokenizer
# )

# trainer.train()

# # Evaluating the model
# sample_text = "The Transformer model has revolutionized NLP by enabling parallel processing of sequences."
# inputs = tokenizer("summarize: "+ sample_text, return_tensors='pt', max_length=512, truncation=True)

# outputs = model.generate(inputs['input_ids'], max_length=150, num_beams=4, early_stopping=True)

# print("generated Summary: ", tokenizer.decode(outputs[0], skip_special_token=True))



# from datasets import load_dataset
# from transformers import (
#     AutoTokenizer,
#     AutoModelForSeq2SeqLM,
#     Seq2SeqTrainingArguments,
#     Seq2SeqTrainer,
#     DataCollatorForSeq2Seq,
# )

# # Load dataset for summarization
# dataset = load_dataset("abisee/cnn_dailymail", "3.0.0")
# train_subset = raw_dataset["train"].select(range(500))       # 500 articles instead of 287,113
# val_subset = raw_dataset["validation"].select(range(100))    # 100 articles instead of 13,368
# print(dataset["train"][0])

# # Load tokenizer & model
# model_name = "t5-small"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# # Tokenize for summarization
# def tokenize_function(examples):
#     inputs = ["summarize: " + doc for doc in examples["article"]]
#     model_inputs = tokenizer(inputs, max_length=512, truncation=True)

#     labels = tokenizer(text_target=examples["highlights"], max_length=128, truncation=True)
#     model_inputs["labels"] = labels["input_ids"]
#     return model_inputs

# # Remove raw text columns so the collator only receives tensor fields
# tokenized_datasets = dataset.map(
#     tokenize_function,
#     batched=True,
#     remove_columns=dataset["train"].column_names,
# )

# # Data collator handles dynamic padding for both inputs and labels
# data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

# training_args = Seq2SeqTrainingArguments(
#     output_dir="./results",
#     eval_strategy="epoch",
#     learning_rate=2e-5,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     num_train_epochs=3,
#     weight_decay=0.01,
#     save_total_limit=2,
#     predict_with_generate=True
# )

# trainer = Seq2SeqTrainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenized_datasets["train"],
#     eval_dataset=tokenized_datasets["validation"],
#     processing_class=tokenizer,
#     data_collator=data_collator,
# )

# trainer.train()

# # Evaluating the model (move inputs to the same device as the trained model)
# sample_text = "The Transformer model has revolutionized NLP by enabling parallel processing of sequences."
# inputs = tokenizer(
#     "summarize: " + sample_text,
#     return_tensors="pt",
#     max_length=512,
#     truncation=True,
# ).to(model.device)

# outputs = model.generate(
#     inputs["input_ids"],
#     max_length=150,
#     num_beams=4,
#     early_stopping=True,
# )

# print("Generated Summary:", tokenizer.decode(outputs[0], skip_special_tokens=True))


# cpu version
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq,
)

# 1. Load dataset and slice a CPU-friendly subset BEFORE tokenizing
raw_dataset = load_dataset("abisee/cnn_dailymail", "3.0.0")
train_subset = raw_dataset["train"].select(range(500))       # 500 articles instead of 287,113
val_subset = raw_dataset["validation"].select(range(100))    # 100 articles instead of 13,368

# Load tokenizer & model
model_name = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 2. Tokenize with shorter max_length (256 instead of 512) for faster CPU attention
def tokenize_function(examples):
    inputs = ["summarize: " + doc for doc in examples["article"]]
    model_inputs = tokenizer(inputs, max_length=256, truncation=True)

    labels = tokenizer(text_target=examples["highlights"], max_length=64, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_train = train_subset.map(
    tokenize_function,
    batched=True,
    # num_proc=4,  # Parallelize across CPU cores
    remove_columns=train_subset.column_names,
)

tokenized_val = val_subset.map(
    tokenize_function,
    batched=True,
    # num_proc=4,
    remove_columns=val_subset.column_names,
)

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

# 3. CPU-friendly training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=3e-4,               # Slightly higher LR converges faster on small subsets
    per_device_train_batch_size=4,    # Lower RAM footprint on CPU
    per_device_eval_batch_size=4,
    num_train_epochs=1,               # 125 total steps (~2-3 mins on CPU)
    weight_decay=0.01,
    save_total_limit=1,
    predict_with_generate=False,      # Avoids slow CPU beam search during validation
    use_cpu=True,
    logging_steps=25,
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_val,
    processing_class=tokenizer,
    data_collator=data_collator,
)

trainer.train()

# 4. Run inference on your sample text
sample_text = (
    "The Transformer model has revolutionized NLP by enabling parallel processing "
    "of sequences through self-attention mechanisms, eliminating the sequential "
    "bottlenecks of recurrent neural networks."
)
inputs = tokenizer(
    "summarize: " + sample_text,
    return_tensors="pt",
    max_length=256,
    truncation=True,
)

outputs = model.generate(
    inputs["input_ids"],
    max_length=60,
    num_beams=2,          # 2 beams is twice as fast as 4 beams on CPU
    early_stopping=True,
)

print("Generated Summary:", tokenizer.decode(outputs[0], skip_special_tokens=True))


# metric = load_metric("rouge") # sacrenleu
# predictions = outputs['generated_text']
# references = dataset['validation']['highlights']

# results = metric.compute(predictions=predictions, references=references)
# print(results)