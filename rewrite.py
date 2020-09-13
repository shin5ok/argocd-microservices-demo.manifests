#!/usr/bin/env python

import json
import glob
import yaml

# def getorg():
   

def main():
    for dep in glob.glob("*-dep.yaml"):
        try:
            with open(dep) as f:
                j = yaml.safe_load(f)
                j['spec']['selector'] = {"matchLabels":{"name":j["metadata"]["name"]}}
                with open(f"new-{dep}", "w") as fw:
                    fw.write(yaml.dump(j))
        except Exception as e:
            print(str(e))

main()
