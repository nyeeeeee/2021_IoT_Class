from flask import Flask

app = Flask(__name__) #파일명 얻어오기

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/first">Go First</a>
        <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first():
    return '''
        <p>First Page</p>
        <a href="/">Go Home</a>
    '''

@app.route("/second")
def second():
    return '''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

#터미널에서 직접실행한 경우
if __name__ == "__main__" :
    app.run(host="0.0.0.0") #port = 5000 - default
