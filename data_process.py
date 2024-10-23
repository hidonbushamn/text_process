from PyPDF2 import PdfReader
import spacy
from tqdm import tqdm
import pandas as pd


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 0 and y < 570:
        parts.append(text)

def page2text(index):
    temppage=reader.pages[index].extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)
    parts.clear()
    return text_body

parts = []
allsentences=[]
text=''

nlp=spacy.load("en_core_web_trf")

reader=PdfReader('test.pdf')

for i in tqdm(range(16,223)):
    text=text+page2text(i)

doc=nlp(text.replace("\n",''))
for sent in doc.sents:
    allsentences.append(sent.text)

df=pd.DataFrame(allsentences,columns=['content'])

df['label']='wrong'

df.to_csv('data.csv',sep="|")