from flask import Flask, render_template, jsonify, request, redirect
import json
app = Flask(__name__)
name_inp = ""


@app.route('/main', methods=['GET'])
def loadStart():
    return render_template("main.html")


@app.route('/get', methods=["POST"])
def loadMain():
    returnedVar = request.get_json()
    print(returnedVar['finame'], returnedVar['laname'], returnedVar['inpage'])
    global name_inp
    name_inp = returnedVar['finame']

    return returnedVar


@app.route('/select', methods=['GET', 'POST'])
def loadSelect():
    if request.method == 'GET':
        return render_template("select.html")
    if request.method == 'POST':
        returnedArr = request.get_json()
        print(returnedArr['selection1'],
              returnedArr['selection2'], returnedArr['selection3'])
        return returnedArr


@app.route('/dispList', methods=['GET'])
def loadDispList():
    # arrToPass = ['ele1', 'ele2', 'ele3', 'ele4', 'ele5']
    return render_template("sCourse.html")


@app.route('/selList', methods=['GET'])
def loadselList():

    arrToPass = ["ele1", "ele2", "ele3", "ele4"]
    print(arrToPass)
    data = {
        "arrPassed": arrToPass,
        "name": name_inp,

    }
    return json.dumps(data)
