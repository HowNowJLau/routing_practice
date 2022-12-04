from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:times>/<string:word>')
def repeat_word(times, word):
    return render_template("repeat.html", times=times, word=word)

# snippet from: https://stackoverflow.com/questions/13678397/python-flask-default-route-possible
@app.errorhandler(404)
def handle_404(e):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)