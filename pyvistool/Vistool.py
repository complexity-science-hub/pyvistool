import webbrowser, os
try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x

import jinja2
import time
import json

class Vistool():


    def __init__(self, visualization, config):
        self.visualization = visualization
        self.config = config
        self.config["visType"] = visualization

        for key in self.config["data"]:
            if isinstance(self.config["data"][key], dict):
                self.config["data"][key] = json.dumps(self.config["data"][key])
            elif isinstance(self.config["data"][key], list):
                csvdata = ""
                last_index = len(config["data"][key]) - 1
                for index, row in enumerate(config["data"][key]):
                    csvdata += ";".join(map(str, row))
                    if (index != last_index):
                        csvdata += "\\n"
                self.config["data"][key] = csvdata


    def show(self):
        TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        j2_loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
        j2_env = jinja2.Environment(loader=j2_loader, trim_blocks=True)

        js = j2_env.get_template("index.html")

        html_str = js.render(
            applicationId=self.visualization,
            vistoolconfig=self.config
        )

        tmpFilename = TEMPLATES_PATH + "index-py-tmp.html"

        with open(tmpFilename, "w+", encoding="utf-8") as f:
            f.write(html_str)

        self.display_html(tmpFilename)


    def display_html(self, filename):
        url = "file://{}".format(filename)
        # Hack to prevent blank page
        time.sleep(0.5)
        webbrowser.open(url)