import json
import yaml
import argparse


def generate_schema(vlmd_file_name, output_file):

    with open(f'vlmd/{vlmd_file_name}') as f:
        vlmd = json.load(f)
    with open('schemas/base-schema.yaml', 'r') as f:
        base_schema = yaml.load(f, Loader=yaml.SafeLoader)

    new_schema = dict()
    new_schema['fieldsMatch'] = base_schema['fieldsMatch']
    new_schema['missingValues'] = base_schema['missingValues']
    new_schema['uniqueKeys'] = base_schema['uniqueKeys']
    new_schema['fields'] = base_schema['fields'] + vlmd['fields']
    print(new_schema)


    with open(f'schemas/{output_file}.yaml', 'w') as outfile:
        yaml.dump(new_schema, outfile, default_flow_style=False, sort_keys=False, indent=2)


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-vlmd", dest="input_heal_vlmd", help="name of input HEAL VLMD file", required=True
    )
    parser.add_argument(
        "--output-file", dest="output_file", help="output file name)", required=True,
    )
    args = parser.parse_args()
    return args


def main():

    args = setup_args()
    vlmd_file_name = args.input_heal_vlmd
    output_file = args.output_file
    generate_schema(vlmd_file_name, output_file)

    return


if __name__ == "__main__":
    main()
