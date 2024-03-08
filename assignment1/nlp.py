import spacy
from commonregex import CommonRegex
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_trf")

# Process whole documents

def redactPhones(text):
    parsed_text = CommonRegex(text)
    phones = parsed_text.phones
    for phone in phones:
        text = text.replace(phone,'*'*len(phone))
    return (text,len(phones))

def redactDates(text,doc):
    dates = []
    for entity in doc.ents:
        if entity.label_ == 'DATE' or entity.label_ == 'TIME':
            dates.append(entity.text)
    dates.sort(key=len,reverse=True)
    for date in dates:
        text = text.replace(date,'*'*len(date))
    return (text,len(dates))

def redactNames(text,doc):
    names = []
    persons = []
    for entity in doc.ents:
        if entity.label_ == 'ORG' or entity.label_ == 'PRODUCT':
            names.append(entity.text)
        elif entity.label_ == 'PERSON':
            persons.append(entity.text)
    names.sort(key=len,reverse=True)
    persons.sort(key=len,reverse=True)
    for name in names:
        text = text.replace(name,'*'*len(name))
        text = text.replace(name.lower(),'*'*len(name))
    for person in persons:
        text = text.replace(person,'*'*len(person))
        namesplits = person.split(' ')
        for namesplit in namesplits:
            if len(namesplit) > 3:
                text = text.replace(namesplit.lower(),'*'*len(namesplit))

    return (text,len(names)+len(persons))

def redactAddresses(text):
    parsed_text = CommonRegex(text)
    street_addresses = parsed_text.street_addresses
    for street_address in street_addresses:
        text = text.replace(street_address,'*'*len(street_address))
    return (text,len(street_addresses))

def getDocFromText(text):
    doc = nlp(text)
    return doc
    
# Find named entities, phrases and concepts


