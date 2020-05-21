from flask import Flask
import numpy
#import cv2
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Cv2!"