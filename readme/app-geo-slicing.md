## VisTool App: Geospatial Correlations

<img src="https://vis.csh.ac.at/vistool/visualizations/geo-slicing/geoslice.png" height="400">

### App ID

   ```
    geo-slicing
   ```

### Description

Geospatial distribution of data attributes

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
```dataFile``` | ```lat;lon;householdSize;female;male;...``` |  | <ul><li><b>lat</b>: Latitude of the node</li><li><b>lon</b>: Longitude of the node</li><li><b>Attributes</b>: add as many attributes as you want. You can select them below as attributes for the x/y axis or as the attributes to visualize</li></ul>

#### Settings

##### Settings

Name | Type | Required | Description
---- | ---- | -------- | -----------
```axisAttributes``` | ```multiselect``` |  | Attributes selectable as x/y axis
```attributes``` | ```multiselect``` | yes | Attributes selectable to visualize
```startAttributes``` | ```multiselect``` |  | Attributes selected on start
```aggregation``` | ```string``` |  | Aggregation mode - how should values within a cell be aggregated?<br><br><b>Options:</b><ul><li>sum: ```'SUM'```</li><li>mean: ```'MEAN'```</li></ul>
```useGlobalNormalization``` | ```boolean``` |  | Use global normalization - normalizes all attributes with the global maximum of all attributes (makes different attributes comparable)

<!--- #### Example

```py
config = {
    "datasets": {
        "dataFile": {
            "data": {
                ...
            }
        }
    },
    "settings": {
        "axisAttributes": ...,
        "attributes": ...,
        "startAttributes": ...,
        "aggregation": ...,
        "useGlobalNormalization": ...
    }
}

vt = Vistool("geo-slicing", config)
vt.show()
``` -->