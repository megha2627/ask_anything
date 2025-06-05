from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face model (text generation)
generator = pipeline("text-generation", model="gpt2")

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        question = request.form['question']
        result = generator(question, max_length=100, num_return_sequences=1)
        answer = result[0]['generated_text']
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
