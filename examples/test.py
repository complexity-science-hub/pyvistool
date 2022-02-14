from pyvistool import Vistool

tableData = [
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a3", "b3", "c3"],
        ]

jsonData = {
    "a": "A",
    "b": {
        "b1": "B1",
        "b2": "B2"
    },
    "c": "C"
}

stringData = '{"a": "A","b": {"b1": "B1","b2": "B2"},"c": "C"}'

config = {
    "datasets": {
        "dataset": {
            "data": tableData
        }
    },
    "settings": {
        "settingA": "a setting",
        "boolSetting": False
    }
}

vt = Vistool("pytest", config)
vt.show()