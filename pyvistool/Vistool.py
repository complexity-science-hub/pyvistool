import webbrowser, os
try:
    from urllib import pathname2url         # Python 2.x
except:
    from urllib.request import pathname2url # Python 3.x

import jinja2
import time
import json

class Vistool():


    def __init__(self, visualization, config, browser=None):
        self.visualization = visualization
        self.config = config
        self.config["visType"] = visualization
        self.browser = browser

        for key in self.config["datasets"]:
            if isinstance(self.config["datasets"][key]["data"], dict):
                self.config["datasets"][key]["data"] = json.dumps(self.config["datasets"][key]["data"])
            elif isinstance(self.config["datasets"][key]["data"], list):
                csvdata = ""
                last_index = len(config["datasets"][key]["data"]) - 1
                for index, row in enumerate(config["datasets"][key]["data"]):
                    csvdata += ";".join(map(str, row))
                    if (index != last_index):
                        csvdata += "\\n"
                self.config["datasets"][key]["data"] = csvdata


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
        webbrowser.get(using=self.browser).open(url)