## VisTool App: 3D Networks

<img src="https://vis.csh.ac.at/vistool/visualizations/3d-nets/3dnets.png" height="400">

### App ID

   ```
    3d-nets
   ```

### Description

Network and path exploration in 3D

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
```node_path``` | ```id;weight;layer;label;R;G;B;x;y;z;desc``` |  | <ul><li><b>id</b>: Node ID</li><li><b>weight</b>: Node weight (numerical value)</li><li><b>layer</b>: Layer ID (for multilayer networks - numerical)</li><li><b>label</b>: A short text label describing the node.</li><li><b>R</b>: Red value of the node's RGB color [0,255]</li><li><b>G</b>: Green value of the node's RGB color [0,255]</li><li><b>B</b>: Blue value of the node's RGB color [0,255]</li><li><b>x</b>: Node's position on the x-axis.</li><li><b>y</b>: Node's position on the y-axis.</li><li><b>z</b>: Node's position on the z-axis.</li><li><b>desc</b>: Detailed node description (optional).</li></ul>
```link_path``` | ```s_id;t_id;l_weight;l_label``` |  | <ul><li><b>s_id</b>: Source node ID</li><li><b>t_id</b>: Target node ID</li><li><b>l_weight</b>: Link weight (numerical)</li><li><b>l_label</b>: Link label</li></ul>

#### Settings

##### Settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```node_delimiter``` | ```string``` |  | Delimiter of nodes CSV
```link_delimiter``` | ```string``` |  | Delimiter of links CSV
```node_has_header``` | ```boolean``` |  | Nodes CSV has header
```link_has_header``` | ```boolean``` |  | Links CSV has header
```showLayerLabels``` | ```boolean``` |  | Auto-generate labels for layers
```calcForceLayout``` | ```boolean``` |  | Calculate an [1,3]-dimensional force-based layout
```overwriteNodePos``` | ```boolean``` |  | Overwrite the original node positions for calculating the force layout
```randomNodePos``` | ```boolean``` |  | Use random node positions (true) or (0,0,0)
```encodeNodeSize``` | ```boolean``` |  | Scale the node size by the node's weight
```encodeLinkWeights``` | ```boolean``` |  | Change the link color by the link's weight
```filterAttribute``` | ```boolean``` |  | Option to filter nodes based on an attribute group (e.g., a cluster ID)
```numForces``` | ```string``` |  | Number of dimensions for force-simulation<br><br><b>Options:</b><ul><li>3: ```'3'```</li><li>2: ```'2'```</li><li>1: ```'1'```</li></ul>
```id``` | ```number``` |  | Node ID index in CSV
```weight``` | ```number``` |  | Node weight index in CSV
```layer``` | ```number``` |  | Node layer index in CSV
```label``` | ```number``` |  | Node label index in CSV
```r``` | ```number``` |  | r (RGB) index in CSV (default: 4)
```g``` | ```number``` |  | g (RGB) index in CSV (default: 5)
```b``` | ```number``` |  | b (RGB) index in CSV (default: 6)
```x``` | ```number``` |  | Node's x-position index in CSV (default: 7)
```y``` | ```number``` |  | Node's y-position index in CSV (default: 8)
```z``` | ```number``` |  | Node's z-position index in CSV (default: 9)
```desc``` | ```number``` |  | Node description index in CSV (default: 10)
```attrToFilter``` | ```number``` |  | Index of cluster/group filter attribute in CSV
```s_id``` | ```number``` |  | Link source ID index in CSV (default: 0)
```t_id``` | ```number``` |  | Link target ID index in CSV (default: 1)
```l_weight``` | ```number``` |  | Link weight index in CSV (default: 2)
```l_label``` | ```number``` |  | Link label index in CSV (default: 3)

<!--- #### Example

```py
config = {
    "datasets": {
        "node_path": {
            "data": {
                ...
            }
        },
        "link_path": {
            "data": {
                ...
            }
        }
    },
    "settings": {
        "node_delimiter": ...,
        "link_delimiter": ...,
        "node_has_header": ...,
        "link_has_header": ...,
        "showLayerLabels": ...,
        "calcForceLayout": ...,
        "overwriteNodePos": ...,
        "randomNodePos": ...,
        "encodeNodeSize": ...,
        "encodeLinkWeights": ...,
        "filterAttribute": ...,
        "numForces": ...,
        "id": ...,
        "weight": ...,
        "layer": ...,
        "label": ...,
        "r": ...,
        "g": ...,
        "b": ...,
        "x": ...,
        "y": ...,
        "z": ...,
        "desc": ...,
        "attrToFilter": ...,
        "s_id": ...,
        "t_id": ...,
        "l_weight": ...,
        "l_label": ...
    }
}

vt = Vistool("3d-nets", config)
vt.show()
``` -->