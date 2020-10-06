import pickle
import configparser
import pandas as pd
from nltk.corpus import stopwords
from string import punctuation
from deeppavlov.core.common.file import read_json
from deeppavlov import build_model, configs
from tqdm import tqdm
import os

config_path = "config.ini"
config = configparser.ConfigParser()
config.read(config_path, encoding='UTF-8')

bert_config = read_json(configs.embedder.bert_embedder)
bert_config['metadata']['variables']['BERT_PATH'] = config['MandatoryRequirementClassifier']['bert_path']
m = build_model(bert_config)

mr_path = config['MandatoryRequirementClassifier']['mr_path']
mandatory_requirements_info = pd.read_csv(mr_path, sep=';', header=0)

available_kns = mandatory_requirements_info.mkn.unique()


def normalize(text):
    normalized_text = [word.strip(punctuation) for word in text.lower().split()]
    stops = stopwords.words("russian")
    normalized_text = [word for word in normalized_text if word not in stops]

    return ' '.join(normalized_text)


dic = {}
for kn_name in tqdm(available_kns):
    mandatory_requirement_candidates = mandatory_requirements_info[mandatory_requirements_info.mkn == kn_name]
    possible_reqs = mandatory_requirement_candidates.mr.tolist()
    possible_reqs_norm = [normalize(x) for x in possible_reqs]
    _, _, _, _, _, sent_mean_embs, _ = m(possible_reqs_norm)
    pairs = zip(possible_reqs, sent_mean_embs)
    dic.update({kn_name: pairs})

filename = 'ot_embs.pkl'
outfile = open(os.path.join('Data', filename), 'wb')
pickle.dump(dic, outfile)
outfile.close()

