import configparser
import pandas as pd
from nltk.corpus import stopwords
from string import punctuation
from deeppavlov.core.common.file import read_json
from deeppavlov import build_model, configs
import collections
import numpy as np
import pickle
from copy import deepcopy


class MandatoryRequirementClassifier:
    def __init__(self, config_path="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_path, encoding='UTF-8')

        bert_config = read_json(configs.embedder.bert_embedder)
        bert_config['metadata']['variables']['BERT_PATH'] = config['MandatoryRequirementClassifier']['bert_path']
        self.m = build_model(bert_config)

        mr_path = config['MandatoryRequirementClassifier']['mr_path']
        self.mandatory_requirements_info = pd.read_csv(mr_path, sep=';', header=0)

        self.available_kns = self.mandatory_requirements_info.mkn.unique()

        pickle_path = config['MandatoryRequirementClassifier']['pickle_path']
        infile = open(pickle_path, 'rb')
        self.embs_dict = pickle.load(infile)
        infile.close()

    @staticmethod
    def normalize(text):
        normalized_text = [word.strip(punctuation) for word in text.lower().split()]
        stops = stopwords.words("russian")
        normalized_text = [word for word in normalized_text if word not in stops]

        return ' '.join(normalized_text)

    def predict(self, text, kn_name):
        text = self.normalize(text)
        possible_reqs = deepcopy(self.embs_dict[kn_name])
        _, _, _, _, _, sent_mean_emb_tgt, _ = self.m(text)
        dic = {}
        for pair in possible_reqs:
            score = np.inner(pair[1], sent_mean_emb_tgt[0]) / (
                        np.linalg.norm(pair[1]) * (np.linalg.norm(sent_mean_emb_tgt[0])))
            dic.update({score: pair[0]})
        od = collections.OrderedDict(sorted(dic.items(), reverse=True))
        result = list(od.values())[0]
        df = self.mandatory_requirements_info[self.mandatory_requirements_info.mr == result]
        return df

        
def test():
    MRClassifier = MandatoryRequirementClassifier()
    print(MRClassifier.available_kns)
    predicted = MRClassifier.predict("Крыша дома протекает, никто не производит провеки!", "Жилищный")
    print(predicted.mr.values[0].strip())
    if not predicted.npa_fed.isnull().values[0]:
        print(predicted.npa_fed.values[0].strip())
    if not predicted.npa_reg_mun.isnull().values[0]:
        print(predicted.npa_reg_mun.values[0].strip())
    print("Test passed")


if __name__=="__main__":
    test()

