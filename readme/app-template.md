## VisTool App: {{ app.title }}

<img src="https://vis.csh.ac.at/vistool/{{ app.preview_image }}" height="400">

### App ID

   ```
    {{ app.id }}
   ```

### Configuration

#### Data

Datasets can be provides either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
{% for file in files %}
    <pre>{{ file.id }}</pre> | <pre>{% for h in file.header %}{{ h.example }}{{ ";" if not loop.last else "" }}{% endfor %}</pre> | {{file.description }}<br><br><ul>{% for h in file.header %}<li><b>{{ h.title }}</b>: {{ h.description }}{% endfor %}</li></ul>
{% endfor %}

#### Settings

#### Example