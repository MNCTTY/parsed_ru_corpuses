import csv
import pandas as pd
from pytorch_pretrained_bert import BertTokenizer, BertModel
from deeppavlov import configs, build_model
import re
import argparse

def remove_nums(s):
    s = re.sub(r'\d-\d{3}-\d{3}-\d{2}-\d{2}', '____', s)
    s = re.sub(r'\d-\d{3}-\d{3}-\d{4}', '____', s)
    s = re.sub(r'\d \d{3} \d{3} \d{2} \d{2}', '____', s)
    s = re.sub(r'\d \d{3} \d{3} \d{4}', '____', s)
    s = re.sub(r'\d{3}-\d{3}-\d{2}-\d{2}', '____', s)
    s = re.sub(r'\d{3}-\d{3}-\d{4}', '____', s)
    s = re.sub(r'\d{3} \d{3} \d{2} \d{2}', '____', s)
    s = re.sub(r'\d{3} \d{3} \d{4}', '____', s)
    # тел номера

    # нс
    # re.sub(r'\d{9, }', ' ', s)
    s = re.sub(r'\d{5,100}', '____', s)

    # номер паспорта
    s = re.sub(r'\d{4} \d{6}', '____', s)

    return s

def remove_ner(s):
    result = ner_model([s])
    for i in range(0, len(result[0])):
        for j in range(0, len(result[0][i])):
            if result[1][i][j] == 'B-PER' or result[1][i][j] == 'I-PER' or result[1][i][j] == 'B-LOC' or \
                    result[1][i][j] == 'I-LOC':
                result[0][i][j] = '______'
    return ' '.join(result[0])


parser = argparse.ArgumentParser(description='input txt path')
parser.add_argument('path', help='path to txt file')
parser.add_argument('koef', default=2.5, type=float,help='koef for distinguish between russian and not-russian')


args = parser.parse_args()

with open(args.path, 'r', encoding='utf-8') as f:
    raw = f.readlines()
data_raw = []
for line in raw:
    data_raw.append(line)
    
data_raw_pieces = []
for line in data_raw:
    pieces = line.split('.')
    for piece in pieces:
        data_raw_pieces.append(piece)
        
        
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased', do_lower_case=True)

for line in data_raw_pieces:
    tokens = tokenizer.tokenize(line)
    num_tokens = len(tokens)
    num_words = len(line.split(' '))

    if num_tokens/num_words < args.koef: #на счет значения коэффициента надо экспериментально подбирать, 2.5
        #russian_phrase
        line = line
    else:
        #not russian_phrase
        line = '_______________________________________'

with open('cleared_1ep.txt', 'w', encoding='utf-8') as f:
    for line in data_raw_pieces:
        f.write(line + '\n')



for line in data_raw_pieces:
    print('hey')
    line = remove_nums(line)
with open('cleared_2ep.txt', 'w', encoding='utf-8') as f:
    for line in data_raw_pieces:
        f.write(line + '\n')



ner_model = build_model(configs.ner.ner_rus, download=True)
#ner_model2 = build_model(configs.ner.ner_bert, download=True)

for line in data_raw_pieces:
    line = remove_ner(line)
with open('cleared_3ep.txt', 'w', encoding='utf-8') as f:
    for line in data_raw_pieces:
        f.write(line + '\n')
