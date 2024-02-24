from flask import Flask, render_template, request
from core.support_function import get_synonyms,rephrase_sentence

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rephrase', methods=['POST'])
def rephrase():
    if request.method == 'POST':
        original_sentence = request.form['sentence']
        rephrased_style = request.form['style']
        rephrased_sentence = rephrase_sentence(original_sentence,rephrased_style)
        return render_template('index.html', original=original_sentence, rephrased=rephrased_sentence,style=rephrased_style)

if __name__ == '__main__':
    app.run(debug=True)
