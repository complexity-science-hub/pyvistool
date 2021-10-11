## VisTool App: {{ app.title }}

<img src="https://vis.csh.ac.at/vistool/{{ app.preview_image }}" height="400">

### App ID

   ```
    {{ app.id }}
   ```

### Description

{{ app.description }}

### Configuration

#### Datasets

Datasets can be provided as 2-dimensional arrays (including the header).

Name | Format (Header) | Options | Description
---- | --------------- | ------- | -----------
{% for file in files %}
```{{ file.id }}```{% if file.rule is defined %}<br><br>(case: *{% for r in file.rule %}{{ r }} ==  {{ file.rule[r] }}{{ "; " if not loop.last else "" }}{% endfor %}*){% endif %} | ```{% for h in file.header %}{{ h.example }}{{ ";" if not loop.last else "" }}{% endfor %}``` | {% for option in file.options %}**{{ option.label }}**: ```{{ option.id }}```, type: ```{{ option.type }}```{{ "<br>" if not loop.last else "" }}{% endfor %} | {% if file.description|length %}{{ file.description }}<br><br>{% endif %}<ul>{% for h in file.header %}<li><b>{{ h.title }}</b>: {{ h.description }}</li>{% endfor %}</ul>
{% endfor %}

#### Settings

{% for setting in settings %}
##### {{ setting.title }}

Name | Type | Required | Description
---- | ---- | -------- | -----------
{% for attribute in setting.attributes %}
```{{ attribute.id }}``` | {% if attribute.type == "select" %}```string```{% else %}```{{ attribute.type }}```{% endif %} | {% if attribute.required is sameas true %}yes{% endif %} | {{ attribute.label }}{% if attribute.type == "select" %}<br><br><b>Options:</b>{% if attribute.options == "fileColumns" %}<br>column name of dataset ```{{ attribute.file }}```{% else %}<ul>{% for option in attribute.options %}<li>{{ option.label }}: ```'{{ option.value }}'```</li>{% endfor %}</ul>{% endif %}{% endif %}

{% endfor %}
{% endfor %}

#### Example