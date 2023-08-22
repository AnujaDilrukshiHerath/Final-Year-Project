import flask
import requests
from flask import Flask, request, jsonify, render_template
import sys
import json
from flask_cors import CORS

# adding Folder_2 to the system path
sys.path.insert(0, 'E:\FYYYP')
import TanglishTagger
import BreakData2
t = BreakData2.Trie()
t.formTrie(BreakData2.keys)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/tanglish/test", methods=["POST"])
def tanglish_process():
    if request.method == "POST":
        data = request.get_json()
        if data is not None and 'text' in data:
            text = data['text']
            result = TanglishTagger.triGramTranslate(text)
            response = {'result': result}
            return flask.jsonify(response)
        else:
            response = {'error': 'Invalid request data'}
            return flask.jsonify(response)
    else:
        response = {'error': 'Invalid request method'}
        return flask.jsonify(response)

@app.route("/suggestions", methods=["POST"])
def suggest_prosses():
        if request.method == "POST":
            data = request.json
            txt = data["text"]
            if len(txt) >= 4:
                para = 1
            else:
                para = 2
            t.printAutoSuggestions(txt, para)
            suggestions = list(set(BreakData2.lstword))
            BreakData2.lstword.clear()
            return jsonify({"suggestions": suggestions})


if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
