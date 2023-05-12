from flask import Flask, render_template, request
import os
import numpy as np
# from predict import predict_label

app = Flask(__name__, static_url_path='/static')

# routes
@app.route("/", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':

        img = request.files['file']

        img_path = img.filename
        print(request.files)
        img.save("static/images/" + img_path)

        # p = predict_label(img_path)
        p= 0.5
        return render_template("predcit.html", prediction = p, img_path = img_path)
    
    return render_template("predcit.html", img_path="Watermelon.jpg")

@app.route("/about")
def about_page():
    return "HI De7ko >:"



if __name__ =='__main__':
    #app.debug = True
    app.run()