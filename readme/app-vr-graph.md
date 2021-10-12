## VisTool App: VR Graph

<img src="https://vis.csh.ac.at/vistool/visualizations/vr-graph/vrnets.png" height="400">

### App ID

   ```
    vr-graph
   ```

### Description

Virtual reality graph visualization

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
```nodeList``` | ```id;weight;desc;...``` |  | <ul><li><b>id</b>: the id of the node</li><li><b>Attributes</b>: add as many attributes as you want</li></ul>
```dataFile``` | ```source;target;weight;desc;...``` |  | <ul><li><b>Source</b>: id of the source node</li><li><b>Target</b>: id of the target node</li><li><b>Attributes</b>: add as many attributes as you want</li></ul>

#### Settings

##### Node settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```node-label``` | ```string``` | yes | Node label column<br><br><b>Options:</b><br>column name of dataset ```nodeList```
```node-desc``` | ```string``` |  | Node description column<br><br><b>Options:</b><br>column name of dataset ```nodeList```
```node-auto-color-by``` | ```string``` |  | Node color by column<br><br><b>Options:</b><br>column name of dataset ```nodeList```
```node-val``` | ```string``` |  | Node value column<br><br><b>Options:</b><br>column name of dataset ```nodeList```
```node-color``` | ```string``` |  | Node color column<br><br><b>Options:</b><br>column name of dataset ```nodeList```
```node-label-billboard``` | ```boolean``` |  | Display node labels as billboards
##### Edge settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```link-label``` | ```string``` |  | Edge label column<br><br><b>Options:</b><br>column name of dataset ```dataFile```
```link-width``` | ```string``` |  | Edge width column<br><br><b>Options:</b><br>column name of dataset ```dataFile```
```link-color``` | ```string``` |  | Edge color column<br><br><b>Options:</b><br>column name of dataset ```dataFile```
##### Additional settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```detailLayout``` | ```string``` |  | Detail layout mode<br><br><b>Options:</b><ul><li>Baseline: ```'baseline'```</li><li>Ego-Highlight: ```'egohighlight'```</li><li>Ego-Bubble: ```'egobubble'```</li></ul>
```showLandmarks``` | ```boolean``` |  | skybox
```permanentSelection``` | ```boolean``` |  | permanent selection
```distanceEncoding``` | ```boolean``` |  | distance encoding
```nodeDegreeInfo``` | ```boolean``` |  | node degree info attached to the controller
```freeFlying``` | ```boolean``` |  | allow free flying (has effect on 'Jump-Through' and 'Fish-Eye' conditions only)
```overviewDetailTransition``` | ```boolean``` |  | smooth transition between overview and detail perspective
```createLayout``` | ```boolean``` |  | Generate static layout (generates a download which can be used to create a new visualization with precomputed layout)

<!--- #### Example

```py
config = {
    "datasets": {
        "nodeList": {
            "data": {
                ...
            }
        },
        "dataFile": {
            "data": {
                ...
            }
        }
    },
    "settings": {
        "node-label": ...,
        "node-desc": ...,
        "node-auto-color-by": ...,
        "node-val": ...,
        "node-color": ...,
        "node-label-billboard": ...,
        "link-label": ...,
        "link-width": ...,
        "link-color": ...,
        "detailLayout": ...,
        "showLandmarks": ...,
        "permanentSelection": ...,
        "distanceEncoding": ...,
        "nodeDegreeInfo": ...,
        "freeFlying": ...,
        "overviewDetailTransition": ...,
        "createLayout": ...
    }
}

vt = Vistool("vr-graph", config)
vt.show()
``` -->