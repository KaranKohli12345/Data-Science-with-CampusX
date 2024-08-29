def ner(text):
    import spacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")
    entities = []
    for ent in doc.ents: 
        entities.append((ent.text, ent.label_))

    print(entities)

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")
entities = []
for ent in doc.ents: 
    entities.append((ent.text, ent.label_))

print(entities)
