import spacy
import wikipedia
from nltk import sent_tokenize
from collections import defaultdict
import re
from random import sample, choice

ner = spacy.load('en', disable = ['parser', 'tagger'])
parse = spacy.load('en', disable = ['ner', 'tagger'])
tag = spacy.load('en', disable = ['ner', 'parser'])
nlp = spacy.load('en')

def named(line):
		line = ner(line)
		if len(line.ents)>0:
			return True
		return False


def make_questions(keyword):

	page = wikipedia.page(keyword)
	keyword = keyword.lower()

	lines = ''
	questions = []
	answers = []
	options =[]
	named_entities = defaultdict(set)


#-----------------------get content------------------------------------------------------

	content = page.content
	content = ner(content)


#-----------------------get sections-----------------------------------------------------

	sections = page.sections
	avoid = ['See also','Notes', 'References', 'Bibliography', 'External links', 'Sources', 'Footnotes', 'Further reading']
	sections = [sect for sect in sections if sect not in avoid]


#-----------------------get "label to entities" dictionary----------------------------------

	for entity in content.ents:
		named_entities[entity.label_].add(entity.text)

	
#------------------------making questions, answers, options-----------------------------------------

	for sect in sections:

		paragraph = page.section(sect)

#-----------------------selecting two best sentences for question framing--------------------------

		if not paragraph:
			continue

		paragraph = sent_tokenize(paragraph)
		paragraph = [re.sub(r'\([^\(]*?\)', r'', str(line)) for line in paragraph]
		paragraph = [line for line in paragraph if len(line.split())>5 and len(line.split())<26]
		paragraph = [line for line in paragraph if named(line)]

		if len(paragraph)>2:
			paragraph = sample(paragraph,2)

#-----------------------making question of the line--------------------------------

		for ques in paragraph:
			line = nlp(ques)

			
#----------------------forming questions-------------------------------------------

			answer = list(line.ents)

			answer = [ans for ans in answer if ans.text.lower() not in keyword \
						and keyword not in ans.text.lower() and ans.text != ' ']
			
			if len(answer) == 0 :
				continue			
			answer = choice(answer)
			
			if ques.count(answer.text)>1 and answer.text !='':
				continue
			
			question = ques.replace(answer.text, '____________')

#----------------------options generator-------------------------------------------
			option = named_entities[answer.label_]
			if len(option)<3:
				continue
			option3 = []
			for x in option:
				x = nlp(x)
				if x.similarity(answer) > 0.5 and x.similarity(answer) != 1:
					option3.append(x.text)

			if len(option3)<3:
				pass
			else:
				option3 = sample(option,3)
			
			questions.append(question)
			answers.append(answer)
			options.extend(option3)

#---------------------return everything------------------------------------------------

	
	return questions, answers, options
