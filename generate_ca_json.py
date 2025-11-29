#!/bin/env python3

import os
import json
import xml.etree.ElementTree as ET

TEMPLATES_DIR = "templates"
OUTPUT_JSON = "community.applications.json"

apps = []

for filename in os.listdir(TEMPLATES_DIR):
    if not filename.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(TEMPLATES_DIR, filename))
    root = tree.getroot()

    name = root.findtext("Name")
    description = root.findtext("Description")
    overview = root.findtext("Overview")
    repo = root.findtext("Repository")
    registry = root.findtext("Registry")
    icon = root.findtext("Icon")
    project = root.findtext("Project")

    app = {
        "name": name,
        "description": description or overview,
        "note": "Hosted by me",
        "repo": repo,
        "registry": registry,
        "icon": icon,
        "documentation": project
    }

    apps.append(app)

with open(OUTPUT_JSON, "w") as f:
    json.dump({"Apps": apps}, f, indent=2)

print(f"Generated {OUTPUT_JSON} with {len(apps)} apps.")

