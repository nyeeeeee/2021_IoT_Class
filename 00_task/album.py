from flask import Flask, render_template

app=Flask(__name__)

@app.route("/album")
def home():
    return render_template('photo_album.html', image1="1.png", image2="2.png",image="3.png", image4="4.png",image5="5.png")

if __name__ == "__main__" :
    app.run("0.0.0.0")
