from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Render the quiz page
    return render_template('quiz.html')

@app.route('/check_answer', methods=['POST'])
def check_answer():
    # Get the user's answer
    user_answer = request.form['user_answer']

    # Check if the answer is correct
    if user_answer == '2':
        result = 'Correct!'
        score = 1
    else:
        result = 'Incorrect'
        score = 0

    # Render the result page
    return render_template('result.html', result=result, score=score)

if __name__ == '__main__':
    app.run(port=8080)


