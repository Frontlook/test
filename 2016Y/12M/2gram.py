from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict,Counter
import re
import string

def cleanInput(input):
    input = input.lower()
    input = re.sub('\n+', " ", input)
    input = re.sub('\t+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, encoding="utf-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput
def ngrams(input, n):
    input = cleanInput(input)
    # print(input)
    # print(Counter(input))
    # print(Counter(input).items())
    return Counter(input)

html = urlopen("http://www.51voa.com/Voa_English_Learning/donald-trump-inauguration-speech-73535.html")
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find("div", id="content").get_text()
ngrams = ngrams(content, 1)
# ngrams=dict(ngrams)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams, '\n')
print("2-grams count is: ", str(len(ngrams)))