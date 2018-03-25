# QuizzeR

Quizzer is an online quiz making bot which fetches information from Wikipedia
and analyses the received information using spaCy and nltk. The accuracy is 70-80 % for questions.


### Prerequisites

Things you need to install:
 
 python3 
		libraries required: spacy, nltk, beautifulsoup, flask, Wikipedia, hunspell.

	install these packages using pip (pip3 for python3):

	i.e.
	```
 		pip3 install spacy
	```

## Running the tests
	
	Goto cloned directory (cd '/path /to /directory') using terminal

	run using python3
	
	'''
		python3 server.py
		open the output link using any borwser (firefox, chorme etc.) 
	'''

## Built With

	* [spaCy](https://github.com/explosion/spaCy/blob/master/README.rst) - Natural Language Processing
	* [NLTK](https://www.nltk.org/) - Natural Language Toolkit
	* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML parser
	* [Flask](http://flask.pocoo.org/) - Web Development Framework
	* [Wikipedia](https://github.com/goldsmith/Wikipedia/blob/master/README.rst)- Wikipedia API

## Algorithm

	* Search the content from Wikipedia. 
	* Divide into sections.
	* Filter the sentences by length and no. of named entities after than pick two random sentences from each section.
	* To make question remove the most important keyword and replace it with blank string.
	* Use similarity to generate options.
	(Go through the code to see how we did it and what criteria we have used to pick two sentences and make question.)


## Contributers

	* Aayush Sharma - aayush1771
	* Anil Chhipa	- adhv45
	* Sameer Mansuri- sameer91
	* Akash Soni	- soniakash1998
	* Divyanshu Dhawan - dextroxd
