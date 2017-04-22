# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

waynecramp = ChatBot("Wayne Cramp")
waynecramp.set_trainer(ChatterBotCorpusTrainer)
waynecramp.train("chatterbot.corpus.english")

@app.route("/WayneCramp")
def home1():
    return ('Hello Wayne Here!')

@app.route("/WayneCramp/<string:query>")
def get_raw_response1(query):
    return str(waynecramp.get_response(query))


luciencramp = ChatBot("Lucien Cramp")
luciencramp.set_trainer(ChatterBotCorpusTrainer)
luciencramp.train("chatterbot.corpus.english")

@app.route("/LucienCramp")
def home2():
    return ('Hello Lucien Here!')

@app.route("/LucienCramp/<string:query>")
def get_raw_response2(query):
    return str(luciencramp.get_response(query))


tonyparsens = ChatBot("Tony Parsens")
tonyparsens.set_trainer(ChatterBotCorpusTrainer)
tonyparsens.train("chatterbot.corpus.english")

@app.route("/TonyParsens")
def home3():
    return ('Hello Tony Here!')

@app.route("/TonyParsens/<string:query>")
def get_raw_response3(query):
    return str(tonyparsens.get_response(query))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
