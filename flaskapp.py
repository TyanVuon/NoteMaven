import sys
sys.path.append('C:\\Users\\Tyan\\PycharmProjects\\NoteMaven')
from flask import Flask, render_template, request
from importinglib import process_input

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input']
        response = process_input(input_text)
        return render_template('index.html', input_text=input_text, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


