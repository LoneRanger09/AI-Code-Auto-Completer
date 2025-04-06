from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Load dataset
dataset = load_dataset("code_search_net", "python", split="train[:1%]", trust_remote_code=True)

# Initialize tokenizer and model (using GPT-2 instead of T5)
model_name = "gpt2"  # or "EleutherAI/gpt-neo-1.3B" for larger model
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Set pad token
model = GPT2LMHeadModel.from_pretrained(model_name)

# Tokenization function
def tokenize_function(examples):
    tokenized = tokenizer(
        examples["func_code_string"],
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )
    # For causal LM, labels are same as input_ids
    tokenized["labels"] = tokenized["input_ids"].clone()
    return tokenized

# Tokenize dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True)
tokenized_datasets.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=100,
    save_strategy="steps",
    save_steps=500,
    learning_rate=5e-5,
    weight_decay=0.01,
    fp16=torch.cuda.is_available()
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Train
trainer.train()