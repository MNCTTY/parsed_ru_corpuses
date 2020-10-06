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


parser = argparse.ArgumentParser(description='input csv path and koef')
parser.add_argument('path', help='path to csv file')
parser.add_argument('koef', default=2.5, type=float, help='koef for distinguish between russian and not-russian')


args = parser.parse_args()
data = pd.read_csv(args.path, delimiter=',', names= ['message', 'topic'])
#data = pd.read_csv("export_12.2018.csv", delimiter=',', names= ['message', 'topic'])

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased', do_lower_case=True)

for i in range(0, len(data['message'])):
    tokens = tokenizer.tokenize(data['message'][i])
    num_tokens = len(tokens)
    num_words = len(data['message'][i].split(' '))

    if num_tokens/num_words < args.koef: #на счет значения коэффициента надо экспериментально подбирать
        #russian_phrase
        data['message'][i] = data['message'][i]
    else:
        #not russian_phrase
        data['message'][i] = '_______________________________________'

data.to_csv('cleared_1ep.csv',index=False)




for i in range(0, len(data['message'])):
    #print('hey')
    data['message'][i] = remove_nums(data['message'][i])

data.to_csv('cleared_2ep.csv', index=False)





ner_model = build_model(configs.ner.ner_rus, download=True)
#ner_model2 = build_model(configs.ner.ner_bert, download=True)

for i in range(0, len(data['message'])):
   # print('hey')
    data['message'][i] = remove_ner(data['message'][i])

data.to_csv('cleared_3ep.csv', index=False)
