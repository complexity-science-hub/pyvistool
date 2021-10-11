from pyvistool import Vistool

tableData = [
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a3", "b3", "c3"],
        ]

config = {
    "datasets": {
        "dataset": {
            "data": tableData
        }
    },
    "settings": {
        "settingA": "a setting"
    }
}

vt = Vistool("pytest", config)
vt.show()