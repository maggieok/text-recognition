import random
import re
from indexing import load_index


train_list = open('train.list', 'r')
train = open('dataset/train.txt', 'w')
val = open('dataset/val.txt', 'w')


char2index = load_index()
lines = train_list.readlines()
random.shuffle(lines)
for i, line in enumerate(lines):
    line = line.strip()
    chars = line.split('\t', 3)[-1]
    chars = re.sub(r'\s+', '', chars)
    indexs = [str(char2index[char]) for char in chars]
    newline = '\t'.join(line.split('\t', 3)[:-1]) +'\t'+ ','.join(indexs) + "\n"
    if i % 100 == 0:
        val.write(newline)
    else:
        train.write(newline)


train.close()
val.close()
train_list.close()
