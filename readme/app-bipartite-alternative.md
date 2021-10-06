## VisTool App: Bipartite

<img src="https://vis.csh.ac.at/vistool/visualizations/bipartite/bipa.png" height="400">

### App ID

   ```
    bipartite
   ```

### Configuration

#### Data

Datasets can be provides either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
```dataset```<br><br>(variant: *settings.custom_clustering=false*) | ```Group 1;Filter 1;Filter 2;Filter 3;Group 2;Value``` | <br><br><ul><li><b>First column</b>: group A</li><li><b>As many columns as you want</b>: filters</li><li><b>Second last column</b>: group B</li><li><b>Last column</b>: value</li></ul>
```dataset```<br><br>(variant: *settings.custom_clustering=true*) | ```Group 1;Filter 1;Filter 2;Filter 3;Group 2;Value;Cluster``` | <br><br><ul><li><b>First column</b>: group A</li><li><b>As many columns as you want</b>: filters</li><li><b>Third last column</b>: group B</li><li><b>Second last column</b>: value</li><li><b>Last column</b>: cluster</li></ul>

#### Settings

#### Example