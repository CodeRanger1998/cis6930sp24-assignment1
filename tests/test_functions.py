import sys
from ..assignment1.nlp import redactAddresses,redactNames,redactPhones,redactDates,getDocFromText

"""
Testing functions redactNames
"""
def test_redactNames():
    try:
        text = "John Smith"
        doc = getDocFromText(text)
        redacted = redactNames(text=text,doc=doc)
        if redacted[0] == "\u2588":
            pass
        else:
            print("Error while redacting names",file=sys.stderr)
            assert False
    except Exception as e:
        print("Error while redacting names "+ str(e),file=sys.stderr)
        assert False

"""
Testing functions redactDates
"""
def test_redactDates():
    try:
        text = "4 November 2024"
        doc = getDocFromText(text)
        redacted = redactDates(text=text,doc=doc)
        if redacted[0] == "\u2588":
            pass
        else:
            print("Error while redacting dates",file=sys.stderr)
            assert False
    except Exception as e:
        print("Error while redacting dates "+ str(e),file=sys.stderr)
        assert False

"""
Testing functions redactPhones
"""
def test_redactPhones():
    try:
        text = "352-176-7481"
        redacted = redactPhones(text=text)
        if redacted[0] == "\u2588":
            pass
        else:
            print("Error while redacting phone",file=sys.stderr)
            assert False
    except Exception as e:
        print("Error while redacting phone "+ str(e),file=sys.stderr)
        assert False

"""
Testing functions redactAddresses
"""
def test_redactAddresses():
    try:
        text = "3800 SW 34TH ST"
        redacted = redactAddresses(text=text)
        if redacted[0] == "\u2588":
            pass
        else:
            print("Error while redacting addresses "+redacted,file=sys.stderr)
            assert False
    except Exception as e:
        print("Error while redacting adrresses "+ str(e),file=sys.stderr)
        assert False
