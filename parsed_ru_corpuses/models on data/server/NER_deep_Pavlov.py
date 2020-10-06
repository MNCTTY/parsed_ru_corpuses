import pandas as pd
import deeppavlov 
import fastText
import pymorphy2
import argparse
import os 
from deeppavlov import build_model, configs




##################################################################################################
######################args parsing####################################

parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, help="type the path to the input file")
parser.add_argument("--output", type=str, help="type the path to the output file")

args = parser.parse_args()

if not os.path.exists(args.input):
	print("Your input filePath is Invalid")
	exit()
	
test_output = os.path.splitext(args.output)
if test_output[1] != '.csv':
	print('Your output filename is not csv!')
	print(test_output[1])

	
##################################################################################################


inp = args.input
data = pd.read_csv(inp)
print('Input done')
ner_model = build_model(configs.ner.ner_rus , download=True) ##!!

print('Ner_model downloaded')

######################################################################################################
#####################################NER Task##########################################################
model_result = []
the_result = []
end = len(data['full_text'])
for i in range(0, end):
    if (i % 100) == 0:
      print(i)
    if type(data['full_text'][i]) != float:
        text = data['full_text'][i]
        textid = data['textid'][i]
        textname = data['textname'][i]
        res = ner_model([text])
        model_result.append(res)
        tags = []
        words = []
        for i in range(0, len(res[1][0])):
          if res[1][0][i]!='O':
            tags.append(res[1][0][i])
            words.append(res[0][0][i])

        the_res = [textid, textname, tags, words]
        the_result.append(the_res)


#####################################################################################################
########################################make result good-looking################################		
final_data = []

morph = pymorphy2.MorphAnalyzer()

for i in range(0, len(the_result)):
    textid = the_result[i][0]
    textname = the_result[i][1]
    pers = []
    orgs = []
    locs = []
    for j in range(0, len(the_result[i][2])):
        if the_result[i][2][j]=='B-PER' or the_result[i][2][j]=='I-PER':
            text = the_result[i][3][j]
            pers.append(morph.parse(text)[0].normal_form)
        if the_result[i][2][j]=='B-ORG' or the_result[i][2][j]=='I-ORG':
            text = the_result[i][3][j]
            orgs.append(morph.parse(text)[0].normal_form)
        if the_result[i][2][j]=='B-LOC' or the_result[i][2][j]=='I-LOC':
            text = the_result[i][3][j]
            locs.append(morph.parse(text)[0].normal_form)
    final_data.append([textid, textname, pers, orgs, locs])

	
	
dataframe = pd.DataFrame(final_data, columns=['textid', 'textname', 'persons', 'organizations', 'locations'])

dataframe.to_csv(args.output,index=False)



