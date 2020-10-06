# parsed_ru_corpuses



### NOTEBOOKS:
* **Collection3 Open.ipynb**
* **FactRuEval Open.ipynb**

This one is a parcing data in FactRuEval format to a comfortable DataFrame that can be usesd in NER tasks.

If you really needs full and complete FactRuEval opening, use this [code:](https://github.com/bond005/deep_ner/blob/master/deep_ner/utils.py)

* **Lenta Conllu Open.ipynb**
* **Lenta Tag for CustomNER.ipynb**

Hand labeled 100 texts. The notebook contains exactly annotations.

* **Lighttag Annotations Open.ipynb**

An ultimate version of my relationships with resulting data format. It deals with multi-dim lighttag jsons correctly.
Sometimes lighttag annotation tool renders a damaged json with shifted values. My code doesn't deal with such cases.


* **Lighttag Text Form.ipynb**

This code is forming text corpuses for next lighttag annotations. Given number of original news join to one text with special separators for future easy splitting.

* **RBC Open.ipynb**
* **RIA Open.ipynb**


All data sourses can be found by provided links:

  * [Taiga news dataset (Fontanka, Lenta, KP, Interfax)](https://tatianashavrina.github.io/taiga_site/downloads)
  * **[RIA news dataset]** <https://github.com/RossiyaSegodnya/ria_news_dataset>
  * **[FactRuEval 2016 dataset]** <https://github.com/dialogue-evaluation/factRuEval-2016>
  * **[Collection3]** <http://labinform.ru/pub/named_entities/descr_ne.htm>
  * **[rbc]** <https://drive.google.com/drive/u/0/folders/1meQQrEa45PkSmBmgMbPiMUppXLWXEhR7>
  * **[RBC lighttag annotated]** <https://drive.google.com/drive/u/0/folders/1meQQrEa45PkSmBmgMbPiMUppXLWXEhR7>


Also this repo contains old repo called 'nlp' that contained Bert models to which parsed ru corpuses data were sent. For sake of legacy I decided to keep them all and unite, since I did this stuff very long time ago for one united project.


-- -- -- -- nlp read.me

# nlp

Here are Kashgari implementation of NER task with rubert / multi bert embeddings. In server folder deeppavlov NER implementation can be found in format, that are ready to deploy on server. Must warn, that leaks of memory and often breakdowns characterize it very well.

## Some important to understanding and inspiration links:

* **[Google Researh Bert]**(https://github.com/google-research/bert)

* **[Collection of BERT resources for every task that you ever need]**(https://github.com/Jiakui/awesome-bert)

That are an original implementation of BERT by Google and a collection of custom libs with BERT implementations for different tasks and in diffirent variations. You'll find there something for baseline for sure. 

* **[The Illustrated BERT, ELMo, and co.]**(https://jalammar.github.io/illustrated-bert/v)

The most complete and cool visualised article about modern nlp architectures, such as BERT, ELMo, ULMFit - what are they, how and what for they were created, diffirencies.

* **[Туториал по запуску BERT локально и на Google Colab]**(https://habr.com/ru/post/436878/)


* **[Complexity / generalization /computational cost in modern applied NLP for morphologically rich languages]**(https://spark-in.me/post/bert-pretrain-ru)

A criticism of Bert.

* **[Sequence Tagging with Tensorflow]**(https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html)

* **[Tensorflow - Named Entity Recognition]**(https://github.com/guillaumegenthial/tf_ner)

That are very complete and visualised articles about NER task itself,  and its implementation, builded on pure Tensorflow without hypefull stuff. What's just Doc has recommended. 

* **[DeepPavlov NER](http://docs.deeppavlov.ai/en/master/components/ner.html)**


  
