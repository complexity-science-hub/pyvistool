## VisTool App: VR Graph

<img src="https://vis.csh.ac.at/vistool/visualizations/vr-graph/vrnets.png" height="400">

### App ID

   ```
    vr-graph
   ```

### Description

Virtual reality graph visualization

### Configuration

#### Data

Datasets can be provided either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
```nodeList``` | ```id;weight;desc;...``` | <ul><li><b>id</b>: the id of the node</li><li><b>Attributes</b>: add as many attributes as you want</li></ul>
```dataFile``` | ```source;target;weight;desc;...``` | <ul><li><b>Source</b>: id of the source node</li><li><b>Target</b>: id of the target node</li><li><b>Attributes</b>: add as many attributes as you want</li></ul>

#### Settings

##### Node settings

Name | Type / Options | Required | Description
---- | ---- | -------- | -----------
```node-label``` | column name of dataset ```nodeList``` | yes | Node label column
```node-desc``` | column name of dataset ```nodeList``` |  | Node description column
```node-auto-color-by``` | column name of dataset ```nodeList``` |  | Node color by column
```node-val``` | column name of dataset ```nodeList``` |  | Node value column
```node-color``` | column name of dataset ```nodeList``` |  | Node color column
```node-label-billboard``` | ```boolean``` |  | Display node labels as billboards
##### Edge settings

Name | Type / Options | Required | Description
---- | ---- | -------- | -----------
```link-label``` | column name of dataset ```dataFile``` |  | Edge label column
```link-width``` | column name of dataset ```dataFile``` |  | Edge width column
```link-color``` | column name of dataset ```dataFile``` |  | Edge color column
##### Additional settings

Name | Type / Options | Required | Description
---- | ---- | -------- | -----------
```detailLayout``` | ```'normal'``` &#124; ```'normalNoDirectLinks'``` &#124; ```'sphereFishEye'``` &#124; ```'rings'``` |  | Detail layout mode
```showLandmarks``` | ```boolean``` |  | skybox
```permanentSelection``` | ```boolean``` |  | permanent selection
```distanceEncoding``` | ```boolean``` |  | distance encoding
```nodeDegreeInfo``` | ```boolean``` |  | node degree info attached to the controller
```freeFlying``` | ```boolean``` |  | allow free flying (has effect on 'Jump-Through' and 'Fish-Eye' conditions only)
```overviewDetailTransition``` | ```boolean``` |  | smooth transition between overview and detail perspective
```createLayout``` | ```boolean``` |  | Generate static layout (generates a download which can be used to create a new visualization with precomputed layout)

#### Example