from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/concept')
def concept():
    return render_template('concept.html')

@app.route('/structure')
def structure():
    return render_template('structure.html')

@app.route('/functions')
def functions():
    return render_template('functions.html')

@app.route('/trends')
def trends():
    return render_template('trends.html')

@app.route('/problems')
def problems():
    return render_template('problems.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)