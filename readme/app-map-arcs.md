## VisTool App: Geospatial Flows

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
```nodes``` | ```id;lat;lng;shapeId;Name;Field;...``` |  | <ul><li><b>id</b>: Node ID</li><li><b>lat</b>: Latitude of the node</li><li><b>lng</b>: Longitude of the node</li><li><b>shapeId</b>: The ID of the shape in the shapefile this node corresponds to. If you do not upload a shape file, use the ISO3 country code.</li><li><b>Attributes</b>: add as many attributes as you want. They will be used as filters.</li></ul>
```edges``` | ```sourceId;targetId;weight;[time];Category;...``` |  | <ul><li><b>sourceId</b>: Source ID</li><li><b>targetId</b>: Target ID</li><li><b>weight</b>: Weight</li><li><b>time</b>: Time (optional)</li><li><b>Attributes</b>: add as many attributes as you want. They will be used as filters.</li></ul>
```shapeFile``` |  |  | Shapefile in the geojson format. If you leave it blank, all countries of the world will be used.<br><br><ul></ul>

#### Settings

##### Settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```shapeFileIdAttribute``` | ```string``` |  | Attribute name of shapes used as the shapeId in the 'Nodes List' (default: 'ISO3')
```shapeFileNameAttribute``` | ```string``` |  | Attribute name of shapes used as the name
```arcMinWidth``` | ```number``` |  | Minimum width of arcs
```arcMaxWidth``` | ```number``` |  | Maximum width of arcs
##### Filters

Name | Type | Required | Description
---- | ---- | -------- | -----------
```showAllEdgesOnStart``` | ```boolean``` |  | Show all edges on start
```nodeFilterAttributes``` | ```multiselect``` |  | Node attributes used as filters
```edgeFilterAttributes``` | ```multiselect``` |  | Edge attributes used as filters
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
##### Hexagons

Name | Type | Required | Description
---- | ---- | -------- | -----------
```enableHexagons``` | ```boolean``` |  | Enable hexagons to visualize aggregated node attributes (numeric attributes only)
```hexagonAttributes``` | ```multiselect``` | yes | Node attributes used for hexagons
```defaultHexAggregation``` | ```string``` |  | Aggregation mode - how should values within a hexagon be aggregated?<br><br><b>Options:</b><ul><li>sum: ```'SUM'```</li><li>mean: ```'MEAN'```</li></ul>
```hexagonGridSize``` | ```number``` | yes | Initial grid size of hexagons in meteres
##### Histogram

Name | Type | Required | Description
---- | ---- | -------- | -----------
```enableDistribution``` | ```boolean``` |  | Enable distribution histogram
```nodeDistributionAttributes``` | ```multiselect``` |  | Node attributes used as filters
```edgeDistributionAttributes``` | ```multiselect``` |  | Edge attributes used as filters
```distributionBins``` | ```number``` | yes | How many bins should be used for the histogram?
##### Multiple Scenarios

Name | Type | Required | Description
---- | ---- | -------- | -----------
```enableMultipleScenarios``` | ```boolean``` |  | Enable multiple scenarios.
```scenarioAttribute``` | ```string``` |  | The edge attribute defining the scenario<br><br><b>Options:</b><br>column name of dataset ```edges```

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
        "arcMinWidth": ...,
        "arcMaxWidth": ...,
        "showAllEdgesOnStart": ...,
        "nodeFilterAttributes": ...,
        "edgeFilterAttributes": ...,
        "pageTitle": ...,
        "shapeLabel": ...,
        "flowLabel": ...,
        "enableTimeline": ...,
        "timelineLabelX": ...,
        "timelineLabelY": ...,
        "enableHexagons": ...,
        "hexagonAttributes": ...,
        "defaultHexAggregation": ...,
        "hexagonGridSize": ...,
        "enableDistribution": ...,
        "nodeDistributionAttributes": ...,
        "edgeDistributionAttributes": ...,
        "distributionBins": ...,
        "enableMultipleScenarios": ...,
        "scenarioAttribute": ...
    }
}

vt = Vistool("map-arcs", config)
vt.show()
``` -->