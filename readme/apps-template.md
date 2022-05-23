## VisTool Apps

The following apps are available in the VisTool of the Complexity Science Hub Vienna and therefore accessible from python through the pyvistool package:

Name | App ID | Screenshot
----- | ----- | ----------
{% for app in apps %}
{{ app.title }}<br>[details](app-{{ app.id }}.md) | ```{{ app.id }}``` | <img src="https://vis.csh.ac.at/vistool/{{ app.previewImage }}" height="200">
{% endfor %}