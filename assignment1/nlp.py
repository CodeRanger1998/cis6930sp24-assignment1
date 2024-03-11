import spacy
from commonregex import CommonRegex

# Load English tokenizer, tagger, parser and NER
# Load the pre-trained English transformer-based pipeline for tokenization, tagging, parsing, and NER
nlp = spacy.load("en_core_web_trf")

# Process whole documents

def redactPhones(text):
    # Parse the text using CommonRegex to extract phone numbers
    parsed_text = CommonRegex(text)
    phones = parsed_text.phones
    # Replace each phone number with the full block character (█)
    for phone in phones:
        text = text.replace(phone, '\u2588')
    # Return the redacted text and the number of phone numbers found
    return (text, len(phones))

def redactDates(text, doc):
    dates = []
    # Iterate through entities recognized by SpaCy
    for entity in doc.ents:
        # Check if the entity is a date or time
        if entity.label_ == 'DATE' or entity.label_ == 'TIME':
            dates.append(entity.text)
    # Sort the dates by length in descending order
    dates.sort(key=len, reverse=True)
    # Replace each date with the full block character (█)
    for date in dates:
        text = text.replace(date, '\u2588')
    # Return the redacted text and the number of dates found
    return (text, len(dates))

def redactNames(text, doc):
    names = []
    persons = []
    # Iterate through entities recognized by SpaCy
    for entity in doc.ents:
        # Check if the entity is a person
        if entity.label_ == 'PERSON':
            persons.append(entity.text)
    # Sort the persons by length in descending order
    persons.sort(key=len, reverse=True)
    # Replace each person's name with the full block character (█)
    for person in persons:
        text = text.replace(person, '\u2588')
        # Split the person's name into individual components and replace each component with the full block character (█)
        namesplits = person.split(' ')
        for namesplit in namesplits:
            if len(namesplit) > 3:
                text = text.replace(namesplit.lower(), '\u2588')
    # Return the redacted text and the number of names found
    return (text, len(names) + len(persons))

def redactAddresses(text, doc):
    # Parse the text using CommonRegex to extract street addresses
    parsed_text = CommonRegex(text)
    street_addresses = parsed_text.street_addresses
    # Replace each street address with the full block character (█)
    for street_address in street_addresses:
        text = text.replace(street_address, '\u2588')
    
    locations = []
    for entity in doc.ents:
        # Check if the entity is a date or time
        if entity.label_ == 'GPE' or entity.label_ == 'LOC':
            locations.append(entity.text)
    # Sort the dates by length in descending order
    locations.sort(key=len, reverse=True)
    # Replace each date with the full block character (█)
    for location in locations:
        text = text.replace(location, '\u2588')
    # Return the redacted text and the number of street addresses found
    
    return (text, len(street_addresses))

def getDocFromText(text):
    # Parse the text using SpaCy to extract named entities, phrases, and concepts
    doc = nlp(text)
    return doc
    
# Find named entities, phrases, and concepts