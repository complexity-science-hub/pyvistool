## VisTool App: Map Arcs

<img src="https://vis.csh.ac.at/vistool/visualizations/map-arcs/maparcs.png" height="400">

### App ID

   ```
    map-arcs
   ```

### Description

Geospatial network visualization

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
```nodes``` | ```id;lat;lng;shapeId;Name;Field;...``` |  | <ul><li><b>id</b>: Node ID</li><li><b>lat</b>: Latitutde of the node</li><li><b>lng</b>: Longitude of the node</li><li><b>shapeId</b>: The ID of the shape in the shapefile this node corresponds to. If you do not upload a shape file, use the ISO3 country code.</li><li><b>Attributes</b>: add as many attributes as you want. They will be used as filters.</li></ul>
```edges``` | ```sourceId;targetId;weight;[time]``` |  | <ul><li><b>sourceId</b>: Source ID</li><li><b>targetId</b>: Target ID</li><li><b>weight</b>: Weight</li><li><b>time</b>: Time (optional)</li></ul>
```shapeFile``` |  |  | Shapefile in the geojson format. If you leave it blank, all countries of the world will be used.<br><br><ul></ul>

#### Settings

##### Settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```shapeFileIdAttribute``` | ```string``` |  | Attribute name of shapes used as the shapeId in the 'Nodes List' (default: 'ISO3')
```shapeFileNameAttribute``` | ```string``` |  | Attribute name of shapes used as the name
```showAllEdgesOnStart``` | ```boolean``` |  | Show all edges on start
##### Labels

Name | Type | Required | Description
---- | ---- | -------- | -----------
```pageTitle``` | ```string``` |  | Title of the page
```shapeLabel``` | ```string``` |  | Label for shape (e.g. 'Country')
```flowLabel``` | ```string``` |  | Label for flows (e.g. 'Product Flows')
##### Timeline

Name | Type | Required | Description
---- | ---- | -------- | -----------
```enableTimeline``` | ```boolean``` |  | Enable timeline
```timelineLabelX``` | ```string``` |  | Timeline Label X
```timelineLabelY``` | ```string``` |  | Timeline Label Y

<!--- #### Example

```py
config = {
    "datasets": {
        "nodes": {
            "data": {
                ...
            }
        },
        "edges": {
            "data": {
                ...
            }
        },
        "shapeFile": {
            "data": {
                ...
            }
        }
    },
    "settings": {
        "shapeFileIdAttribute": ...,
        "shapeFileNameAttribute": ...,
        "showAllEdgesOnStart": ...,
        "pageTitle": ...,
        "shapeLabel": ...,
        "flowLabel": ...,
        "enableTimeline": ...,
        "timelineLabelX": ...,
        "timelineLabelY": ...
    }
}

vt = Vistool("map-arcs", config)
vt.show()
``` -->