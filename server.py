from flask import Flask, redirect, render_template, request, url_for
import wiki
import nlp

app=Flask(__name__)
app.config['SECRET_KEY'] = 'lololololol'


#--------------------------------------------------------------------------------------------

@app.route('/')

def ask_keyword():
    return render_template('home.html')

#--------------------------------------------------------------------------------------------

@app.route('/about')

def about():
    return render_template('about.html')

#--------------------------------------------------------------------------------------------
@app.route('/search', methods = ['POST', 'GET'])
    
def search():
    
    if request.method == 'POST':
        keyword = request.form
        keyword = keyword['Name']

    error_no = wiki.check(keyword)
    
    if error_no == 1:
        return render_template('no_page.html',keyword=keyword)
    
    elif error_no == 2:
        options = wiki.options(keyword)
        options_link = []
        
        for option in options:
            options_link.append(url_for('question',keyword=option))

        return render_template('multiple_results.html', keyword=keyword, option=zip(options,options_link))
    
    elif error_no == 3:
        return render_template('no_connection.html')

    

    return redirect(url_for('question',keyword=keyword))


#--------------------------------------------------------------------------------------------

@app.route('/questions/<keyword>', methods = ['POST', 'GET'])

def question(keyword):

    questions, answer, options = nlp.make_questions(keyword)

    return render_template('questions.html',questions=questions, answers=answer, options=options, keyword=keyword, length=len(questions))

#--------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()


