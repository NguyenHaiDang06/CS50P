from twttr1 import shorten

def test_letters():
  assert shorten("twitter")=="twttr"
  assert shorten("TWITTER")=="TWTTR"
  assert shorten("TwItTeR")=="TwtTR"
  
def test_numbers():
  assert shorten("1234")=="1234"
  assert shorten("CS50")=="CS50"
  
def test_punctuation():
  assert shorten(",.?")==",.?"
  assert shorten("Hello, World!")=="Hll, Wrld!"
