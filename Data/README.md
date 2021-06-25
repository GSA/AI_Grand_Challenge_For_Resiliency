# ADDITIONAL RESOURCES

This document contains additional NLP resources relevant to the challenge. It is divided into three categories: data, software and literature. Note these are merely a fraction of NLP resources available: if you would like to contribute, please either submit a pull request. Note we can only publish non-commerical and open-source tools and libraries and we cannot host datasets published by state and local entities. For commercial tools and state and local data, contributors are encouraged to fork this repo and add to their version.

For a comprehensive list of NLP sources, see [here](https://github.com/keon/awesome-nlp).


## Data


### Policy

* [Regulations.gov](https://www.regulations.gov/)

	- This is a platform that publishes public policy and rule changes made by the federal government in. They come from through the Federal Register and are associated with a variety of contributing and non-contributing federal agencies. Announcement includes a mix of HTML, Word docs, PDFs, and JSON files. The HTML file contains the text of the announcement whereas the JSON file contains metadata. Some important information in the JSON files include the subject, topics, link to attached documents, and posted date. 
	- Information on the Regulations.gov API <a href="https://open.gsa.gov/api/regulationsgov/">can be found here</a>. 
	- The Challenge team pulled ~4GB of <a href="https://ai-challenge-regulations-gov-data.s3.amazonaws.com/regulations-gov-data.zip">starter data here</a>. This data contains documents pulled from Regulations.gov under the keyword search terms “COVID”, “COVID-19”, and “coronavirus” from Nov 2020-Mar 2021. The docs are a mix of JSON, HTML, and PDF formats.
	

* [Code of Federal Regulations](https://www.govinfo.gov/app/collection/cfr/2020/) \[[2019](https://github.com/GSA/AI_Grand_Challenge_For_Resiliency/tree/main/Data/CFR-2019) | [2020](https://github.com/GSA/AI_Grand_Challenge_For_Resiliency/tree/main/Data/CFR-2020)\]

	- The CFR is the codification of the general and permanent rules published in the Federal Register by the departments and agencies of the Federal Government produced by the Office of the Federal Register (OFR) and the Government Publishing Office. It is divided up into 50 titles (subject areas), allowing competitors to view the impact of COVID-19 across different industries and sectors. The data is stored in XML format.

* [Coronavirus.gov](https://www.coronavirus.gov/)

	- [Search logs](https://github.com/GSA/AI_Grand_Challenge_For_Resiliency/blob/main/Data/Coronavirus.gov%20Search%20Logs-20210309T185408Z-001.zip) pulled from Coronavirus.gov may provide some insight into the questions the federal government received from the public at different stages of the pandemic.

* Executive Orders post-pandemic 2020 \[[Archive](https://github.com/GSA/AI_Grand_Challenge_For_Resiliency/blob/main/Data/2020%20Covid%20Relevant%20EOs-20210309T190708Z-001.zip)\]


### COVID-19

* Literature

	- [CORD-19](https://allenai.org/data/cord-19) - CORD-19 is a resource of over 500,000 scholarly articles, including over 200,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses which can be used as additional data for training various models.
	- [TREC-COVID](https://academic.oup.com/jamia/article/27/9/1431/5828938) - An information retrieval benchmark included 60,000 articles with a set of 35 topics related to COVID-19.
These topics include natural questions such as: what is the origin of COVID-19 and how does the coronavirus respond to changes in the weather which is complex enough to deal with real word queries.

* Other

	- [COVID-Q](https://openreview.net/pdf/e364ccc8d2bf9f6521e0071cc9e162aab0a9ff4e.pdf) - A Question Classification Dataset comprises 1,690 questions about COVID-19 from 13 sources, which we annotate into 15 question categories and 207 question clusters. They found that many questions that appeared in multiple sources were not answered by any FAQ websites of reputable organizations such as the CDC and FDA.
	- [COVID-19 Public Repository Data](https://github.com/github/covid-19-repo-data) - A comprehensive versioned dataset of the repositories and relevant related metadata about public projects hosted on GitHub related to the 2019 Novel Coronavirus and associated COVID-19 disease.
	- [COVID-19 Weekly Cases and Deaths per 100,000 by Age, Race/Ethnicity, and Sex](https://covid.cdc.gov/covid-data-tracker/#demographicsovertime)
	- [State-Issued Prevent Measures at the State-Level](https://covid.cdc.gov/covid-data-tracker/#state-level-covid-policy)
	- [County Risk Tracker published by FEMA](https://experience.arcgis.com/experience/d67c068233ef4a3283776df0ac31e888/)
	- [Awesome Coronavirus](https://github.com/soroushchehresa/awesome-coronavirus#open-source-projects) - Huge collection of useful projects and resources for COVID-19 (2019 novel Coronavirus)


## Software


### NLP-related

* General

	- [Spark NLP](https://github.com/JohnSnowLabs/spark-nlp) - Natural Language Processing library built on top of Apache Spark ML. Provides simple, performant & accurate NLP annotations for machine learning pipelines that scale easily in a distributed environment. Comes with 1100+ pretrained pipelines and models in more than 192+ languages. 
	- [spaCy](https://spacy.io) - Library for advanced Natural Language Processing in Python and Cython.
	- [Stanza](https://github.com/stanfordnlp/stanza) - The Stanford NLP Group's official Python NLP library. It contains support for running various accurate natural language processing tools on 60+ languages and for accessing the Java Stanford CoreNLP software from Python.
	- [Flair](https://github.com/flairNLP/flair) - A very simple framework for state-of-the-art NLP.
	- [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) -  Library of deep learning models and datasets designed to make deep learning more accessible and accelerate ML research. 

* Topic Modeling

	- [Top2Vec](https://github.com/ddangelov/Top2Vec) - Top2Vec is an algorithm for topic modeling and semantic search. It automatically detects topics present in text and generates jointly embedded topic, document and word vectors. Technical information can be found [here](https://arxiv.org/abs/2008.09470).
	- [BERTopic](https://github.com/MaartenGr/BERTopic) - Topic modeling technique that leverages transformers and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions. Even supports visualizations similar to LDAvis!

* Embeddings

	- [SimCSE](https://github.com/princeton-nlp/SimCSE) - Sentence embedding using contrastive learning.
	- [Awesome Sentence Embedding](https://github.com/Separius/awesome-sentence-embedding) - A curated list of pretrained sentence and word embedding models.

* Data Mining / Information Extraction

	- [Textract](https://github.com/deanmalmgren/textract) - Extract text from any document. No muss. No fuss.
	- [ELKI](http://elki-project.github.io/) - Open source (AGPLv3) data mining software written in Java.
	- [Snips NLU](https://github.com/snipsco/snips-nlu) - Python library for extracting structured information from sentences written in natural language.
	- [Kashgari](https://github.com/BrikerMan/Kashgari) - Production-level NLP Transfer learning framework built on top of tf.keras for text-labeling and text-classification, includes Word2Vec, BERT, and GPT2 Language Embedding.
	- [NCRF++](https://github.com/jiesutd/NCRFpp) - Neural Sequence Labeling Toolkit. Easy-to-use for any sequence labeling tasks (e.g. NER, POS, Segmentation). It includes character LSTM/CNN, word LSTM/CNN and softmax/CRF components.
	- [MITIE](https://github.com/mit-nlp/MITIE) - Provides free (even for commercial use) state-of-the-art information extraction tools. Current release includes tools for performing named entity extraction and binary relation detection as well as tools for training custom extractors and relation detectors.
	- [Yake](https://github.com/LIAAD/yake) - Library implementing automatic keyword extraction method: identifying most important keywords in a document.

* Summarization

	- [Summa](https://github.com/summanlp/textrank) - A text summarization and keyword extraction package based on TextRank in Python.
	- [Fast Abstractive Summarization-RL](https://github.com/ChenRocks/fast_abs_rl) - Code for ACL 2018 paper: "Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting."
	- [Extreme Summarization](https://github.com/EdinburghNLP/XSum) - Topic-Aware Convolutional Neural Networks for Extreme Summarization. Data and code for 2018 EMNLP paper "Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization."
	- [Bert Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer) - Easy to use extractive text summarization with BERT in Python.

* Machine Translation

	- [Marian](https://marian-nmt.github.io/) - Fast Neural Machine Translation in C++.
	- [OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py) - Open Source Neural Machine Translation in PyTorch.
	- [NEMATUS](https://github.com/EdinburghNLP/nematus) - Open-Source Neural Machine Translation in Tensorflow.
	- [NMT-Keras](http://nmt-keras.readthedocs.io/) - Neural Machine Translation in Keras.
 

### Policy-related
	
* Tools

	- [The Language Interpretability Tool (LIT)](https://ai.googleblog.com/2020/11/the-language-interpretability-tool-lit.html) - An interactive platform for NLP model understanding.
	- [Scattertext](https://github.com/JasonKessler/scattertext) - A tool for finding distinguishing terms in corpora and displaying them in an interactive HTML scatter plot.
	- [eRegulations](https://eregs.github.io) \[[Description](https://eregs.github.io/story/) | [Features](https://eregs.github.io/features/)\] -  Web-based application that makes regulations easier to find, read, and understand. Specific to agencies and hosted individually. Only works on the Code of Federal Regulations.
	- [QuantGov](https://www.quantgov.org/) \[[Description](https://www.quantgov.org/about)\] - The Home of Open-Source Policy Analysis - Open-source platform, a collection of unique, relational data, and a toolbox for researchers and policymakers alike. Enables users to retrieve specific data from large amounts of text by "quantifying" data.
	- [Gamechanger](https://github.com/dod-advana/gamechanger) - Central repository of governing documents for the US Department of Defense (DoD). Utilizes AI for ease-of-use of navigating DoD requirements.
	- [Policynet](https://github.com/mitre/policynet) - Exploration of the U.S. rulesets as a network.

* Ontology Libraries - Various representations of legal ontologies. Most use the W3C Web Ontology Language ([OWL](https://www.w3.org/OWL/)), which is commonly used to "to represent rich and complex knowledge about things, groups of things, and relations between things."

	- [The LKIF Core Ontology of Basic Legal Concepts](https://github.com/RinkeHoekstra/lkif-core) - Library of ontologies for the legal domain. Consists of 15 modules in a hierarchical manner consisting of three levels (abstract, basic, legal and framework). Repository consists of .OWL files for each module. 
	- [Lexicog](https://jogracia.github.io/ontolex-lexicog/) - Module of the Lexicon Model for Ontologies. Used to create representations of any linguistic resource containing lexographic and other associated data. Extension of the *lemon* core module, OntoLex, to better model lexographic information as linked data.
	- [CEN MetaLex](http://www.metalex.eu/) - Standard for representing legal information and references to it in a XML format; primarily used in Europe. Intends to act as a universal format that all legal documents can be converted into, allowing for better transfer and standardization of representation of information.
	- [Akoma Ntoso](http://www.akomantoso.org/) - Defines a set of simple technology-neutral electronic representations in XML format of parliamentary, legislative and judiciary documents. Primarily used by entities in Africa. Provides the semantic representation of various documents, allowing for them to be "machine readable" and improving data exchange.
	- [USLM Schema](https://github.com/usgpo/uslm/) - XML information model desgined to represent the legislation of the US Congress. Primarily used to convert titles of the United States Code into XML but also supports other legislative materials. Utilizes the XML Schema Definition Language (XSD). White paper can be found [here]((https://github.com/usgpo/uslm/blob/master/USLM-User-Guide.pdf)).


## Literature


### Research Conferences

* [JURIX](http://jurix.nl/) - The Foundation for Legal Knowledge Based Systems - Organization of legal informatics researchers in the Netherlands and Flanders. Proceedings published in the journal *Frontiers of Artifical Intelligence*.
* [ReMap](https://www.remep.net/) - Hybrid legal informatics conference. Each year focuses on a subtopic. Unique in that businesses looking for solutions are invited as well to initiate application of research presented. Rubric for submissions can be found [here](https://www.remep.net/submissions/).

### Research Papers

#### Information Extraction

* Named Entity Recognition

	- [A Survey of Deep Learning for Named Entity Recognition](https://arxiv.org/pdf/1812.09449.pdf)
	- [A Survey on Recent Advances in Named Entity Recognition from Deep Learning models](https://www.aclweb.org/anthology/C18-1182.pdf)

* Recent Papers

	- [Knowledge Router: Learning Disentangled Representations for Knowledge Graphs](http://dx.doi.org/10.18653/v1/2021.naacl-main.1)
	- [Distantly Supervised Relation Extraction with Sentence Reconstruction and Knowledge Base Priors](http://dx.doi.org/10.18653/v1/2021.naacl-main.2)
	- [Cross-Task Instance Representation Interactions and Label Dependencies for Joint Information Extraction with Graph Convolutional Networks](http://dx.doi.org/10.18653/v1/2021.naacl-main.3)
	- [Abstract Meaning Representation Guided Graph Encoding and Decoding for Joint Information Extraction](http://dx.doi.org/10.18653/v1/2021.naacl-main.4)
	- [A Frustratingly Easy Approach for Entity and Relation Extraction](http://dx.doi.org/10.18653/v1/2021.naacl-main.5)
	- [Document-Level Event Argument Extraction by Conditional Generation](http://dx.doi.org/10.18653/v1/2021.naacl-main.69)


#### Machine Translation

[Here](https://machinelearningmastery.com/introduction-neural-machine-translation/) is an introduction to neural machine translation.

* Statistical Machine Translation

	- [A Statistical Approach to Machine Learning](https://dl.acm.org/doi/pdf/10.5555/92858.92860)

* Neural Machine Translation

	- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)
	- [Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](https://arxiv.org/abs/1609.08144)
	- [Sequence to sequence learning with neural networks](https://arxiv.org/abs/1409.3215)
	- [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078)
	- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
	- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)

* Recent Papers

	- [Data Filtering using Cross-Lingual Word Embeddings](http://dx.doi.org/10.18653/v1/2021.naacl-main.15)
	- [Improving the Lexical Ability of Pretrained Language Models for Unsupervised Neural Machine Translation](http://dx.doi.org/10.18653/v1/2021.naacl-main.16)
	- [Neural Machine Translation without Embeddings](http://dx.doi.org/10.18653/v1/2021.naacl-main.17)
	- [Counterfactual Data Augmentation for Neural Machine Translation](http://dx.doi.org/10.18653/v1/2021.naacl-main.18)
	- [Multilingual BERT Post-Pretraining Alignment](http://dx.doi.org/10.18653/v1/2021.naacl-main.20)
	- [Harnessing Multilinguality in Unsupervised Machine Translation for Rare Languages](http://dx.doi.org/10.18653/v1/2021.naacl-main.89)
	- [The Curious Case of Hallucinations in Neural Machine Translation](http://dx.doi.org/10.18653/v1/2021.naacl-main.92)
	- [Towards Modeling the Style of Translators in Neural Machine Translation](http://dx.doi.org/10.18653/v1/2021.naacl-main.94)


#### Summarization

* Extractive Summarization
	
	- [Text summarization using Latent Semantic Analysis](https://www.researchgate.net/publication/220195824_Text_summarization_using_Latent_Semantic_Analysis)
	- [Extractive document summarization based on convolutional neural networks](https://ieeexplore.ieee.org/abstract/document/7793761) - [Code](https://github.com/alexvlis/extractive-document-summarization)

* Abstractive Summarization 

	- [A Neural Attention Model for Abstractive Sentence Summarization](https://arxiv.org/pdf/1509.00685.pdf) - [Code](https://github.com/facebookarchive/NAMAS)
	- [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf) 
	- [Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting](https://arxiv.org/pdf/1805.11080.pdf)
	- [Generative Adversarial Network for Abstractive Text Summarization](https://arxiv.org/pdf/1711.09357.pdf)

* Recent Papers

	- [Noisy Self-Knowledge Distillation for Text Summarization](http://dx.doi.org/10.18653/v1/2021.naacl-main.56)
	- [Improving Zero and Few-Shot Abstractive Summarization with Intermediate Fine-tuning and Data Augmentation](http://dx.doi.org/10.18653/v1/2021.naacl-main.57)
	- [Enhancing Factual Consistency of Abstractive Summarization](http://dx.doi.org/10.18653/v1/2021.naacl-main.58)
	- [A New Approach to Overgenerating and Scoring Abstractive Summaries](http://dx.doi.org/10.18653/v1/2021.naacl-main.110)
	- [Efficient Attentions for Long Document Summarization](http://dx.doi.org/10.18653/v1/2021.naacl-main.112)


#### Syntax

* Tagging

	- [Larger-Context Tagging: When and Why Does It Work?](https://www.aclweb.org/anthology/2021.naacl-main.115.pdf)
	- [Learning Better Internal Structure of Words for Sequence Labeling](https://www.aclweb.org/anthology/D18-1279.pdf)
