from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load CodeT5 model
model_name = "Salesforce/codet5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def predict_code(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=100)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
