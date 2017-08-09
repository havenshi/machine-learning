# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from snownlp import SnowNLP

with open('company_title.txt', 'r', encoding='utf-8') as myfile:
    text = myfile.read()  # read file in form of string
s = SnowNLP(text)

hashing = {}
for item in s.words:  # s.words is array of split words
    hashing[item.lower()] = hashing.get(item.lower(), 0) + 1  # record all words and frequencies into hashing map

# sort hashing
key = sorted(hashing, key=hashing.get)[::-1]
value = sorted(hashing.values())[::-1]
print(value)
print (key)

# write key(word) and value(frequency) to a new file
newkey = np.array(key)
newvalue = np.array(value)

df = pd.DataFrame({"word" : newkey, "frequency" : newvalue})
df.to_csv("split_word.csv", index=False, encoding="utf-8")