## VisTool App: Bipartite

<img src="https://vis.csh.ac.at/vistool/visualizations/bipartite/bipa.png" height="400">

### App ID

   ```
    bipartite
   ```

### Description

Bipartite network visualization

### Configuration

#### Data

Datasets can be provided either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
```dataset``` | ```Group 1;Filter 1;Filter 2;Filter 3;Group 2;Group 2;Value;Value;Cluster``` | <ul><li><b>First column</b>: group A</li><li><b>As many columns as you want</b>: filters</li><li><b>Second last column</b>: group B</li><li><b>Third last column</b>: group B</li><li><b>Last column</b>: value</li><li><b>Second last column</b>: value</li><li><b>Last column</b>: cluster</li></ul>

#### Settings

##### Value formatting

Name | Type | Required | Description
---- | ---- | -------- | -----------
```unit``` | ```string``` |  | Unit
```decimals``` | ```number``` |  | Value decimals
```unit_space``` | ```boolean``` |  | Space between value and unit
```unit_position``` | ```string``` |  | Unit positioning<br><br><b>Options:</b><ul><li>Left of value: ```'left'```</li><li>Right of value: ```'right'```</li></ul>

#### Example