from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("nlpaueb/legal-bert-base-uncased")

# Example legal text
#legal_text = "This contract shall be governed by and construed in accordance with the laws of the State of New York."
legal_text = "Seek employment advise from a US lawyer"

# Tokenize the text
inputs = tokenizer(legal_text, return_tensors="pt", padding=True, truncation=True)

# Run inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Get the predicted class
predicted_class = logits.argmax().item()
print(f"Predicted class: {predicted_class}")
