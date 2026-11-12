"""Download DistilGPT2 files into a local folder for TorchServe packaging."""
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "distilgpt2"
OUTPUT_DIR = "model_files"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
tokenizer.save_pretrained(OUTPUT_DIR)
model.save_pretrained(OUTPUT_DIR)
print(f"Saved model and tokenizer to {OUTPUT_DIR}")
