## VisTool App: VR Graph

<img src="https://vis.csh.ac.at/vistool/visualizations/vr-graph/vrnets.png" height="400">

### App ID

   ```
    vr-graph
   ```

### Configuration

#### Data

Datasets can be provides either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
```nodeList``` | ```id;weight;desc;...``` | <br><br><ul><li><b>id</b>: the id of the node<li><b>Attributes</b>: add as many attributes as you want</li></ul>
```dataFile``` | ```source;target;weight;desc;...``` | <br><br><ul><li><b>Source</b>: id of the source node<li><b>Target</b>: id of the target node<li><b>Attributes</b>: add as many attributes as you want</li></ul>

#### Settings

#### Example