import wikipedia
import sys
import spacy
import operator
import re
import random

nlp=spacy.load('en')

keyword = input("Enter the keyword: ")

try:
    search = wikipedia.page(keyword,redirect=False)

except wikipedia.exceptions.PageError:
    print("The page was not found, sorry.")
    
    #return to the enter keyword page.
    sys.exit()

except wikipedia.exceptions.DisambiguationError:
    print("Multiple Results Found.")
   
    options = wikipedia.search(keyword)
    options.pop(0)

    i=1
    for option in options:
        print(i,option)
        i=i+1

    option = int(input("Which one did you mean: "))
    print(f"You choosed to search for {options[option-1]}")

    search = wikipedia.page(options[option-1])
    #return to the enter keyword page.

except:
    print("Connection Error")
    sys.exit()

print(search)
sections = search.sections

needed_sent=[]
final_sent=[]

def gen_sents(doc):
    for line in doc.sents:
        string = (re.sub(r'\([^\(]*?\)',r'', str(line)))
        value=0
        tmp = nlp(str(string))
        for ne in tmp.ents:
            value = value+1
        if(len(line)>5 and len(line)<25 and value>1 and value<6):
            #print(string, len(string), value)
            needed_sent.append(string)
    if(len(needed_sent)>2):
        temp = (random.sample(needed_sent, 2))
        for x in temp:
            final_sent.append(x)
    else:
        for x in needed_sent:
            final_sent.append(x)


for sectio in sections:
    doc = nlp(search.section(sectio))
    gen_sents(doc)

#sorted_list = sorted(no_of_ner.items(), key=operator.itemgetter(1), reverse=True)
#to sort dict in descending order


final_text = ' '.join(final_sent)
#print(final_text)

#text = nlp(final_text)

for line in final_text:
	tp = nlp(line)
	for word in tp:
		if(word.tag_ == 'PRP' or word.tag_ == 'PRP$'):
			line.replace(word.text,keyword)

print(final_text)