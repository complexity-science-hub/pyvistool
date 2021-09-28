from pyvistool import Vistool
import json

jsonData = {
    'a': 'a1',
    'b': {
        'ab': 'ab1',
        'bb': 'ab2'
    }
}

tableData = [
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a3", "b3", "c3"],
        ]

config = {
    "data": {
        "dataset": tableData
    },
    "settings": {
        "settingA": "seawas"
    }
}

vt = Vistool("pytest", config)
vt.show()