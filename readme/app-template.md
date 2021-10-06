## VisTool App: {{ app.title }}

<img src="https://vis.csh.ac.at/vistool/{{ app.preview_image }}" height="400">

### App ID

   ```
    {{ app.id }}
   ```

### Description

{{ app.description }}

### Configuration

#### Data

Datasets can be provided either as json or as a 2-dimensional array (including the header).

Name | Format (Header) | Description
---- | ------ | -----------
{% for file in files %}
```{{ file.id }}```{% if file.variant is defined %}<br><br>{{ file.variant }}{% endif %} | ```{% for h in file.header %}{{ h.example }}{{ ";" if not loop.last else "" }}{% endfor %}``` | {% if file.description|length %}{{ file.description }}<br><br>{% endif %}<ul>{% for h in file.header %}<li><b>{{ h.title }}</b>: {{ h.description }}</li>{% endfor %}</ul>
{% endfor %}

#### Settings

{% for setting in settings %}
##### {{ setting.title }}

Name | Type / Options | Required | Description
---- | ---- | -------- | -----------
{% for attribute in setting.attributes %}
```{{ attribute.id }}``` | {% if attribute.type == "select" %}{% if attribute.options == "fileColumns" %}column name of dataset ```{{ attribute.file }}```{% else %}{% for option in attribute.options %}```'{{ option.value }}'```{{ " &#124; " if not loop.last else "" }}{% endfor %}{% endif %}{% else %}```{{ attribute.type }}```{% endif %} | {% if attribute.required is sameas true %}yes{% endif %} | {{ attribute.label }}
{% endfor %}
{% endfor %}

#### Example