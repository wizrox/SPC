# '''
# ######################
# Courtesy: Special thanks codeBasic youtube channel for this knowledgeable DataScience Series
#
# Tutorial (youtube):https://www.youtube.com/playlist?list=PLeo1K3hjS3uvaRHZLl-jLovIjBP14QTXc
# Project-code(gitHub): https://github.com/codebasics/py/tree/master/DataScience/CelebrityFaceRecognition
#
# Disclaimer: I don't own the rights of this code/project. The code written is followed as shown
#            in the tutorial with reference to above.
#            P.S.: There are some changes in names of files and variables for personal reference
#            only, In case you are copy pasting this code , please look out for the syntax.
# ######################
#
# '''
from flask import Flask, request, jsonify
import util
# import util2

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "hi"


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":  # always look for the __main__ typo as it will run but with no output
    # if the lien above(24) will not run the statement below at line 26 will not print so this is the
    # key indicator that there is something wrong with line 24:

    print("Starting Python Flask Server For SPC-Image Classification")
    # util2.load_saved_artifacts()
    util.load_saved_artifacts()
    app.run(port=5000)
