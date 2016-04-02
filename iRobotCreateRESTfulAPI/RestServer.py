#! /usr/bin/env python

from flask import Flask, render_template
from flask.ext.bower import Bower
import sys
sys.path.insert(0,"../../")
from PyCharmRemote.iRobotCreateLib.OpenInterfaceLibrary import IRobotCreate

app = Flask(__name__)
Bower(app)

@app.route('/')
def hello_world():
    return 'Hello iRobot Create Commander in Chief!'

@app.route('/control/')
def control():
    return render_template("ControlUI.html")

@app.route("/move/<speedRight>/<speedLeft>/")
def move(speedRight, speedLeft):
    print("Values are : ", str(speedRight), " :: ", str(speedLeft))
    myRobot.drive(int(speedRight),int(speedLeft))
    return "Success"

@app.route("/stop/")
def stop():
    result = myRobot.stop()
    return "Stopped"

if __name__ == '__main__':
    try:
        myRobot = IRobotCreate()
        myRobot.start()
        myRobot.fullMode()
        # myRobot.drive(30, 30)

        app.run(host="0.0.0.0", port=5002, debug=True)
    except Exception as ex:
        print(str(ex))
