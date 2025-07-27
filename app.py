from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page using the index.html template."""
    return render_template('index.html', title='My Flask App', message='Welcome to a basic Flask app with templates!')

if __name__ == '__main__':
    app.run(debug=True)