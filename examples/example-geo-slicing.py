from pyvistool import Vistool
import json

dataFile = [
    ["axisAttribute_A", "axisAttribute_B", "attribute_1", "attribute_2", "attribute_3", "lon", "lat"],
    [2, 9, 1.1, 30.3, 3.2, 12.78335128, 46.59090451],
    [5, 12, 2.2, 20.2, 3.1, 8.792641132, 48.58855926],
    [3, 15, 3.3, 10.1, 3.3, 9.789176363, 47.58621405]
]

config = {
    "datasets": {
        "dataFile": {
            "data": dataFile
        }
    },
    "settings": {
        "axisAttributes": ["axisAttribute_A", "axisAttribute_B"],
        "attributes": ["attribute_1", "attribute_2", "attribute_3"],
        "startAttributes": ["attribute_1", "attribute_2"],
        "aggregation": 'MEAN',
        "useGlobalNormalization": "true"
    }

}

#vt = Vistool("geo-slicing", config, "chrome")
vt = Vistool("geo-slicing", config)
vt.show()