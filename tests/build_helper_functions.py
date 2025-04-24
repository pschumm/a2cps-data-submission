import os
import pprint

import yaml


def print_forms(project):
    pprint.pprint(project.forms)
    return


def return_form_fields(project, form):
    fields = [i.name for i in project.forms[form].items]
    pprint.pprint(fields)
    return fields


def print_redcap_mappings(project, form):
    pprint.pprint({i.name: i.categories for i in project.forms[form].items})
    return


def return_schema(schema_path):
    if not os.path.exists(schema_path):
        print("No Data Freeze file found in ", schema_path)
        exit(1)
    with open(schema_path, "r") as stream:
        schema = yaml.safe_load(stream)
    return schema


def return_schema_fields(schema):
    schema_fields = [i["name"] for i in schema["fields"]]
    pprint.pprint(schema_fields)
    return schema_fields


def print_schema_mappings(schema):
    pprint.pprint(
        {
            i["name"]: {v: int(k) for k, v in i["enumLabels"].items()}
            for i in schema["fields"]
            if i.get("enumLabels") is not None
        }
    )
    return
