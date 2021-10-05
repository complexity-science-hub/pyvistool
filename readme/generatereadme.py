import urllib.request
import json
import jinja2
import os

baseUrl = "https://vis.csh.ac.at/vistool/"

def createAppDoc(vis):
    appj = j2_env.get_template("app-template.md")

    with urllib.request.urlopen(baseUrl + vis["config"]) as url:
        appConfig = json.load(url)

    print(appConfig)

    app_str = appj.render(
        app=vis,
        files=appConfig["files"]
    )

    tmpFilename = TEMPLATES_PATH + "/app-" + vis["id"] + ".md"

    with open(tmpFilename, "w+", encoding="utf-8") as f:
        f.write(app_str)


mainConfigUrl = baseUrl + "config.json"
with urllib.request.urlopen(mainConfigUrl) as url:
    mainConfig = json.load(url)

print(mainConfig)

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))
j2_loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
j2_env = jinja2.Environment(loader=j2_loader, trim_blocks=True)

mainj = j2_env.get_template("apps-template.md")

apps = []

for vis in mainConfig["visualizations"]:
    apps.append(vis)
    createAppDoc(vis)

main_str = mainj.render(
    apps=apps,
)

tmpFilename = TEMPLATES_PATH + "/apps.md"

with open(tmpFilename, "w+", encoding="utf-8") as f:
    f.write(main_str)