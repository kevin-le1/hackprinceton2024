import torch
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "bigscience/bloom-560m"
# You can also use any other supported model from 🤗 Model Hub
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, add_bos_token=False)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)
model = model.cuda()
inputs = tokenizer('A cat in French is "', return_tensors="pt")["input_ids"].cuda()
outputs = model.generate(inputs, max_new_tokens=3)
print(tokenizer.decode(outputs[0]))