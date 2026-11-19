from transformers import T5Tokenizer, T5ForConditionalGeneration
import datasets

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def preprocess_t5(examples):
    inputs = ["classify sentiment: "+ doc for doc in examples['text']]
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length", padding="max_length")
    model_inputs["labels"] = tokenizer(examples['labels'], max_length=16, trucation=True, padding='max_length')["input_ids"]
    return model_inputs

tokenized_t5 = datasets.map(preprocess_t5, batched=True)
