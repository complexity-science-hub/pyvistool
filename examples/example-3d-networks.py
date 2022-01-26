from pyvistool import Vistool
import json

node_data = [
["Label","ID","DESC","Level","Age_Range","Num_pat","Size","Class","r","g","b","alpha","x","y","z"],
["A00__0-9",1,"Cholera",1,"0-9",3,3,"A",26,242,57,1,196.385595627344,426.899375312316,0],
["A01__0-9",2,"Typhus abdominalis und Paratyphus",1,"0-9",5,6.63499562090289e-05,"A",26,242,57,1,195.497108653403,463.841109842348,0],
["A02__0-9",3,"Sonstige Salmonelleninfektionen",1,"0-9",345,0.00457814697842299,"A",26,242,57,1,158.23346,424.83405,0]
]

link_data = [
    ["Source","Target","weight"],
    [1,2,0.5],
    [1,3,1],
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
         "node_delimiter": ";",
         "link_delimiter": ";",
         "node_has_header": "true",
         "link_has_header": "true"
    }
}

vt = Vistool("3d-nets", config, "chrome")
vt.show()