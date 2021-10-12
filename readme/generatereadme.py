import urllib.request
import json
import jinja2
import os, copy

baseUrl = "https://vis.csh.ac.at/vistool/"

includeHidden = False

def createAppDoc(vis):
    appj = j2_env.get_template("app-template.md")

    with urllib.request.urlopen(baseUrl + vis["config"]) as url:
        appConfig = json.load(url)

    #print(appConfig)
    appConfig["files"] = createFileVariants(appConfig["files"])



    app_str = appj.render(
        app=vis,
        files=appConfig["files"],
        settings=appConfig["settings"]
    )

    tmpFilename = TEMPLATES_PATH + "/app-" + vis["id"] + ".md"

    with open(tmpFilename, "w+", encoding="utf-8") as f:
        f.write(app_str)


def createFileVariants(files):
    resultFiles = []

    for file in files:
            rules = []
            eitherOrRulesAvailable = False

            if "header" in file:
                for h in file["header"]:
                    if 'rules' in h:
                        if not h["rules"] in rules:
                            print("new rule: ")
                            print(h["rules"])
                            if len(h["rules"]) == 1 and isinstance(list(h["rules"].values())[0], bool):
                                print("one rule is boolean")
                                for rule in rules:
                                    if len(h["rules"]) == 1 and isinstance(list(rule.values())[0], bool):
                                        if list(h["rules"].keys())[0] == list(rule.keys())[0] and list(h["rules"].values())[0] != list(rule.values())[0]:
                                            print("found eitherOrRules")
                                            eitherOrRulesAvailable = True

                            rules.append(h["rules"])

            print("rules for file:")
            print(rules)

            if len(rules) > 0:
                print("!!! we have variants")
                newFile = copy.deepcopy(file)
                newFile["header"] = []

                if not eitherOrRulesAvailable:
                    resultFiles.append(newFile)

                    for h in file["header"]:
                        if not 'rules' in h:
                            newFile["header"].append(h)

                for rule in rules:
                    newFile = copy.deepcopy(file)
                    newFile["header"] = []
                    newFile["rule"] = rule

                    for h in file["header"]:
                        if not 'rules' in h:
                            newFile["header"].append(h)
                        else:
                            ruleContainsHeaderRules = True
                            for r in h["rules"]:
                                if not r in rule:
                                    ruleContainsHeaderRules = False
                                elif h["rules"][r] != rule[r]:
                                    ruleContainsHeaderRules = False

                            if ruleContainsHeaderRules:
                                newFile["header"].append(h)

                    resultFiles.append(newFile)
            else:
                resultFiles.append(file)


    return resultFiles


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
    if 'hidden' in vis:
        if not includeHidden and vis["hidden"]:
            continue

    apps.append(vis)
    createAppDoc(vis)

main_str = mainj.render(
    apps=apps,
)

tmpFilename = TEMPLATES_PATH + "/apps.md"

with open(tmpFilename, "w+", encoding="utf-8") as f:
    f.write(main_str)