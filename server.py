from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1 style="text-align: center">Learning Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)

