## VisTool App: py Test

<img src="https://vis.csh.ac.at/vistool/visualizations/bipartite/bipa.png" height="400">

### App ID

   ```
    pytest
   ```

### Description

Just a small python test

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
```dataset```<br><br>(case: *settingA ==  a*) | ```Group 1;Group 2;optA;optA2``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional A</b>: depending on rule</li><li><b>Optional A2</b>: depending on rule</li></ul>
```dataset```<br><br>(case: *settingB ==  b*) | ```Group 1;Group 2;optB``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional B</b>: depending on rule</li></ul>
```dataset```<br><br>(case: *settingA ==  a; settingB ==  b*) | ```Group 1;Group 2;optA;optA2;optB;optC;optD``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional A</b>: depending on rule</li><li><b>Optional A2</b>: depending on rule</li><li><b>Optional B</b>: depending on rule</li><li><b>Optional C</b>: depending on rule</li><li><b>Optional D</b>: depending on rule</li></ul>
```dataset```<br><br>(case: *settingBool ==  True*) | ```Group 1;Group 2;optE``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional E</b>: depending on rule</li></ul>
```dataset```<br><br>(case: *settingBool ==  False*) | ```Group 1;Group 2;optF``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional F</b>: depending on rule</li></ul>
```dataset```<br><br>(case: *settingInt ==  3*) | ```Group 1;Group 2;optG``` | **Setting A**: ```settingA```, type: ```string```<br>**Setting B**: ```settingB```, type: ```string``` | <ul><li><b>First column</b>: group A</li><li><b>Second column</b>: group B</li><li><b>Optional G</b>: depending on rule</li></ul>

#### Settings

##### Settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```settingA``` | ```string``` |  | Setting A
```settingB``` | ```string``` |  | Setting B

<!--- #### Example

```py
config = {
    "datasets": {
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        },
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        },
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        },
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        },
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        },
        "dataset": {
            "options": {
                "settingA": ...,
                "settingB": ...
            },
            "data": {
                ...
            }
        }
    },
    "settings": {
        "settingA": ...,
        "settingB": ...
    }
}

vt = Vistool("pytest", config)
vt.show()
``` -->