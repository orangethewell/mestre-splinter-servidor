from spacy import load, displacy

nlp = load("pt_core_news_lg")

doc = nlp("Allan é gay")

displacy.serve(doc)
