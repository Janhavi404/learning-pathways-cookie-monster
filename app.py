from flask import Flask, render_template, jsonify, request, redirect, url_for
from code import career, skillset
import json
app = Flask(__name__)
name_inp = ""
carRet = []
skiRet = []


@app.route('/index', methods=['GET'])
def loadStart():
    return render_template("/index.html")


@app.route('/get', methods=["POST"])
def loadMain():
    returnedVar = request.get_json()
    print(returnedVar['finame'], returnedVar['laname'], returnedVar['inpage'])
    global name_inp
    name_inp = returnedVar['finame']

    return redirect('/select', code=302)


@app.route('/select', methods=['GET', 'POST'])
def loadSelect():
    if request.method == 'GET':
        return render_template("select.html")
    if request.method == 'POST':
        dic = {"op1": "Algorithm", "op2": "Scheduling", "op3": "Social Media Management", "op4": "Research", "op5": "C",
               "op6": "HTML", "op7": "CSS", "op8": "Kubernetes and Docker", "op9": "Java", "op10": "Reinforcement Learning"}

        returnedArr = request.get_json()
        print(returnedArr['selection1'],
              returnedArr['selection2'], returnedArr['selection3'])
        a = dic[returnedArr['selection1']]
        b = dic[returnedArr['selection2']]
        c = dic[returnedArr['selection3']]
        # print(a, b, c)
        global carRet
        carRet = career(a, b, c)
        # print(carRet)

        return redirect('/dispList', code=302)


@app.route('/dispList', methods=['GET'])
def loadDispList():
    # arrToPass = ['ele1', 'ele2', 'ele3', 'ele4', 'ele5']
    return render_template("sCourse.html")


@app.route('/selList', methods=['GET'])
def loadselList():

    arrToPass = carRet
    # print(arrToPass)
    # print(name_inp)
    data = {
        "arrPassed": arrToPass,
        "name": name_inp,

    }
    return json.dumps(data)


@app.route('/dispTime', methods=['POST'])
def loadDispTime():
    valPassed = request.get_json()
    # print(valPassed['valuePassed'])
    global skiRet
    skiRet = skillset(valPassed['valuePassed'])
    # print(skiRet)
    # function call arg pass name of the course
    return redirect('/dispSkill', code=302)  # skillset


@app.route('/allCourse', methods=['GET'])
def loadAllCourse():
    return render_template("allCourse.html")


# @app.route('/coursesView', methods=['GET'])
# def loadCourseView():
#     courseArr = ["Big Data Analysis",
#                  "Project Management",
#                  " Social Media Management and Digital Marketing"
#                  "Technical Writing"
#                  "Back End Coding Developer"
#                  "Front End Coding Developers"
#                  "Full Stack Developer"
#                  "Cloud Architect"
#                  "DevOps Engineer"
#                  "AI Engineer"]
#     print(courseArr)
#     dataCourse = {
#         "arra": courseArr,
#     }
#     return json.dumps(dataCourse)

@app.route('/dispSkill', methods=['GET'])
def loadDispSkill():
    arrPassed = skiRet
    data = {
        "arra": arrPassed,

    }
    return render_template('skilDisp.html', li=skiRet)
