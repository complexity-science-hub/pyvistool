from pyvistool import Vistool
import json

node_data = [
["id","weight","layer","label","R","G","B","x","y","z","desc"],
[0,1,0,"label1",10,100,10,100,0,0],
[1,15,0,"label2",100,100,10,100,110,100],
[2,1,1,"label3",10,100,100,0,0,100],
[3,4,1,"label4",100,100,10,0,110,100],
[4,1,0,"label5",10,100,100,100,110,0],
[5,7,2,"label6",100,100,10,200,50,100],
[6,1,2,"label7",10,100,100,100,50,200],

]

link_data = [
    ["Source","Target","weight"],
    [1,2,0.5],
    [3,2,0.5],
    [4,2,0.5],
    [1,5,0.5],
    [1,6,0.5],
    [6,3,1],
    [2,3,0.7]
]

config = {
    "datasets": {
        "node_path": {
            "data": node_data
        },
        "link_path": {
            "data": link_data
        }
    },
    "settings": {
         "node_delimiter" : ";",
         "link_delimiter" : ";",
         "node_has_header" : "true",
         "link_has_header" : "true",
         "showLayerLabels": 'false',
         "calcForceLayout": "false",
         "overwriteNodePos": "true",
         "randomNodePos": "true",
         "encodeNodeSize": "false",
         "encodeLinkWeights": "true",
         "numForces": 3,
    }
}

vt = Vistool("3d-nets", config, "chrome")
#vt = Vistool("3d-nets", config)
vt.show()