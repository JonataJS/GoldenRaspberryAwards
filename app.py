from flask import Flask, request, Response
from model.model import Ormdb
from use_cases import WinnersUseCase
import json

app = Flask(__name__)
import jaydebeapi

connection  = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:5234/movies",
        ["SA", ""],
        "db/h2-2.1.214.jar")
cursor = connection.cursor()
orm = Ormdb()
orm.initialize()


@app.route("/")
def hello_world():
    return ""

@app.route("/getWinner")
def get_winner():
    response = json.dumps(WinnersUseCase().execute(orm))
    print(response)
    return Response(response, status=200, mimetype='application/json')