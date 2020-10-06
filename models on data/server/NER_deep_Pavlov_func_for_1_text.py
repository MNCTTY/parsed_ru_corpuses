import pandas as pd
import deeppavlov 
import fastText
import pymorphy2
import argparse
import os 
from deeppavlov import build_model, configs

def NER_func(news_text):
    ner_model = build_model(configs.ner.ner_rus , download=True) ##!!
	
    res = ner_model([news_text])
    tags = []
    words = []
    
    
    
    for i in range(0, len(res[1][0])):
        if res[1][0][i]!='O':
            tags.append(res[1][0][i])
            words.append(res[0][0][i])

    the_res = [tags, words]

    morph = pymorphy2.MorphAnalyzer()

    pers = []
    orgs = []
    locs = []
    for j in range(0, len(the_res[0])):
        if the_res[0][j]=='B-PER' or the_res[0][j]=='I-PER':
            text = the_res[1][j]
            pers.append(morph.parse(text)[0].normal_form)
        if the_res[0][j]=='B-ORG' or the_res[0][j]=='I-ORG':
            text = the_res[1][j]
            orgs.append(morph.parse(text)[0].normal_form)
        if the_res[0][j]=='B-LOC' or the_res[0][j]=='I-LOC':
            text = the_res[1][j]
            locs.append(morph.parse(text)[0].normal_form)
            
    print('news text: ', news_text, '\n')
    print('persons: ', pers, '\n')
    print('organizations: ', orgs, '\n')
    print('located in ', locs, '\n')
    
    
    return news_text, pers, orgs, locs

print('Start', '/n')	

parser = argparse.ArgumentParser(description='Parse input string')
parser.add_argument("--input", type=str, help="type news text", nargs='*')
args = parser.parse_args()
arg_str = ' '.join(args.input)
print('This is what I\'ve read: ', arg_str, '/n')

answer = NER_func(arg_str)

#%reset