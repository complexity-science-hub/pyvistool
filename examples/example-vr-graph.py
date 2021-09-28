from pyvistool import Vistool
import json

nodeList = [
    ["id", "weight2", "weight1", "desc"],
    ["A", 24.2561357984647, 3, "Description for A"],
    ["B", 7.81111471510434, 3, "Description for B"],
    ["C", 7.50297329441021, 3, "Description for C"],
    ["D", 6.8380365444913, 3, "Description for D"]
]

dataFile = [
            ["source","target","weight2"],
            ["A","B","53.4504939738474"],
            ["A","C","45.5491951727553"],
            ["A","D","103.856748129292"]
        ]

config = {
    "data": {
        "nodeList": nodeList,
        "dataFile": dataFile
    },
    "settings": {
        "showLandmarks": "true"
    }
}

#vt = Vistool("vr-graph", config, "chrome")
vt = Vistool("vr-graph", config)
vt.show()