from flask import Flask, render_template

app=Flask(__name__)

@app.route('/test')
def home():
    return render_template('test.html', test="image/cat.jpg")

if __name__ == "__main__" :
    app.run(host="0.0.0.0")