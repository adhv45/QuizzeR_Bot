# QuizzeR

Quizzer is an online quiz making bot which fetches information from Wikipedia
and analyses the received information using spaCy and nltk. The accuracy is 70-80 % for questions.


### Prerequisites

Things you need to install:
first get pip for python3 (included env is based on python3.7 so use new env if needed)

	Debian/Ubuntu : sudo apt-get install python3-pip
	arch : sudo pacman -S python-pip
	
 python3 
		libraries required: spacy, flask, Wikipedia, hunspell.
	already included wikipedia as there were issues with originel api.
	And already included nltk with tokeniser data.
	
	first enter virtual env 
		source QUIZZER_DIR/.env/bin/activate
		
	install these packages using pip (pip3 for python3):

	i.e.
	```
 		pip3 install -v spacy (do the same for flask, hunspell)
			google if u face some error installing hunspell
			
		download spacy database for english
			python3 -m spacy download en
	```
using new environment 
	
	rm -rf QUIZZER_DIR/.env
	virtualenv .env
	source .env/bin/activate
	install wikipedia using pip
		edit .env/lib/pythonX.X/site-packages/wikipedia/wikipedia.py
			aroung line no. 646
			     - query_params.update(self.__title_query_param)
			     + if not getattr(self, 'title', None):
			     + query_params['pageid'] = self.pageid
			     + else:
			     + query_params['page'] = self.title
	install nltk using pip
		got to python cli
			import nltk
			nltk.download('punkt')
	install spacy (refer to above para)
	
	install hunspell(refer to google for any error)
	install flask

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
