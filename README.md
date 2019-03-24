# parsed_ru_corpuses

There could be some mistakes / inaccuracies: feel free to text me about or fix it.

### NOTEBOOKS:

* **RIA corpuses opening.ipynb** 

it is just opening of the RIA jsons.
* **Lenta tagged texts 2 csv 4 NLU task.ipynb**

it is a parcing of data in a folder tagged texts to format, you can deal with. Use the same notebook for other parts of Taiga news dataset.
* **Lenta Crime Tagging for NER (entities OFF, SUF, DAT, LOC, CRI).ipynb**

It is a custom text tagging notebook. I take top100 Lenta news with a criminality topic and mark them with tags OFFender, SUFferer, DATe, LOCation, CRIme to use in some NER models. Just for experiment how it could predict such entities.
* **FactRuEval Parcing.ipynb**

This one is a parcing data in FactRuEval format to comfortable DataFrame that can be usesd in NER tasks.

Also this repository has a folder **data**, which contains some results of the notebooks' runs.

All 3 data sourses can be found freely in the Internet:

  * [Taiga news dataset (Fontanka, Lenta, KP, Interfax)](https://tatianashavrina.github.io/taiga_site/downloads)
  * **[RIA news dataset]** <https://github.com/RossiyaSegodnya/ria_news_dataset>
  * **[FactRuEval 2016 dataset]** <https://github.com/dialogue-evaluation/factRuEval-2016>
  
