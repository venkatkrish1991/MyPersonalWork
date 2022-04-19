import logging
import base64
import os
import logging

from flask import Flask, request


app = Flask(__name__)

logging.info("My First Test info cloud run")

if __name__=="__main__":
    app.run(debug=True )