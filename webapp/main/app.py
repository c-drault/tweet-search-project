import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, redirect, url_for, render_template
import pandas as pd
app = Flask(__name__)
import sys

from prometheus_client import start_http_server

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_similarity(row):
    tfidf = vectorizer.fit_transform([row.input, row.text])
    return ((tfidf * tfidf.T).A)[0,1]
	
def sorting_tweet (input_user,df): 
    
    # Introducing data in the dataframe as a new column
    df['input'] = input_user
    
    # Applying cosine_sim function to a new column 
    df['similarity'] = df.apply(cosine_similarity, axis=1)
    
    # Sorting dataframe by similarity highest value
    df = df.sort_values(by='similarity', ascending=False)
    
    # Reseting the index to get dataframe indexed after sorted
    df = df.reset_index(drop=True)
    
    # Creating output list appending the top 20 tweets
    output = []
    for i in range(0, 20): 
        output.append((df['text'][i])) 
        
    return output

df = pd.read_csv('../dataset/tweets_clean.csv', index_col=0)

	
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['phrase'])       
        input_requested = request.form['phrase']
        result = sorting_tweet(input_requested, df)
        return redirect(url_for('index', result=result))

    result = request.args.getlist('result')
    if result is None:
        return render_template('index.html')
    return render_template('index.html', result=result)


if __name__ == '__main__':
    start_http_server(8010)
    app.run(debug=True,host='0.0.0.0')
