# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 06:08:10 2022

@author: aleyn
"""

"""git cmd yaz git clone https://github.com/huggingface/transformers.git
cd transformers
pip install -e ."""
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model= model, tokenizer = tokenizer)
results = classifier(["I go to school", 
                     "Maneskin won Eurovision this year but i don't think it was a good choise, because it was the the best choise."])
for result in results:
    print (result)
tokens = tokenizer.tokenize("Maneskin won Eurovision this year but i don't think it was a good choise, because it was the the best choise.")
token_ids = tokenizer.convert_tokens_to_ids(tokens)
input_ids = tokenizer("Maneskin won Eurovision this year but i don't think it was a good choise, because it was the the best choise.")

print(f'  Tokens: {tokens}')
print(f'Token IDs: {token_ids}')
print(f'Input IDs: {input_ids}')

""" 
X_train= ["I go to school",
          "Maneskin won Eurovision this year but i don't think it was a good choise, because it was the the best choise."]
batch= tokenizer(X_train, padding= True, truncation=True, max_lenght=512, return_tensors="pt")

with torch.no_grad():
    outputs= model(**batch, label=torch.tensor([1,0]) )
    print(outputs)
    predictions= F.softmax(outputs.logits, dim=1)
    print(predictions)
    labels= torch.argmax(predictions, dim=1)
    print(labels)
    labels= [model.config.id for label_id in labels.tolist()]
    print(labels)

#save_directory = "saved"
#tokenizer.save_pretrained(save_directory)
#model= AutoModelForSequenceClassification.from_pretrained(save_directory)
model_name = "savasy/bert-base-turkish-sentiment-cased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification. from_pretrained(model_name)
X_train_tr= ["Kod yazmaktan beynim eridi.", "Çok yorgunum", "Gözlerim yanıyor.", "Seni sevmiyorum.", "Galiba ona aşık oldum."]

batch= tokenizer(X_train, padding= True, truncation=True, max_lenght=512, return_tensors="pt")
batch= torch.tensor(batch["input_ids"])
print(batch)

with torch.no_grand():
    outputs = model(batch)
    label_ids = torch.argmax(outputs.logits, dim=1)
    print(label_ids)
    labels = [model.config.id2label[label_id] for label_id in labelids.tolist()]
    print(labels)
"""