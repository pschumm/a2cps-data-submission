import numpy as np
import pandas as pd
import json
import argparse


def generate_template(vlmd_file_name, output_file):

    ### Read VLMD json file ###
    with open(f'vlmd/{vlmd_file_name}') as f:
        d = json.load(f)
    vlmd_df = pd.json_normalize(d['fields'])

    ### Create NDA template for study VLMD ###
    df = pd.DataFrame()
    df['ElementName'] = vlmd_df['name']
    df['DataType'] = vlmd_df['type'].str.capitalize()
    df['Size'] = ''
    df['Required'] = 'Recommended'
    df['ElementDescription'] = vlmd_df['description']

    # needs to improve
    df['ValueRange'] = ["1::4" if vlmd_df['constraints.maximum'][i] == ""
                        else f"{vlmd_df['constraints.minimum'][i]}:{vlmd_df['constraints.maximum'][i]}"
                        for i in range(0, len(vlmd_df))]

    Notes = vlmd_df['constraints.enum'][0].copy()
    for i in range(0, len(vlmd_df['constraints.enum'][0])):
        Notes[i] = Notes[i] + "=" + vlmd_df[f'enumLabels.{Notes[i]}'][0] + ";"
    df['Notes'] = ' '.join(Notes)
    df['Aliases'] = ''

    ### Create required rows for NDA definition file ###
    ElementName = ['subjectkey', 'src_subject_id', 'interview_age', 'interview_date', 'sex']
    DataType = ['GUID', 'String', 'Integer', 'Date', 'String']
    Size = ['', '20', '', '', '20']
    Required = ['Required'] * 5
    ElementDescription = ["The NDAR Global Unique Identifier (GUID) for research subject",
                          "Subject ID how it's defined in lab/project",
                          "Age in months at the time of the interview/test/sampling/imaging.",
                          "Date on which the interview/genetic test/sampling/imaging/biospecimen was completed. MM/DD/YYYY",
                          "Sex of subject at birth"]
    ValueRange = ['NDAR*', '', '0::1440', '', 'M;F;O;NR']
    Notes = ['', '',
             """Age is rounded to chronological month. If the research participant is 15-days-old at time of interview,
              the appropriate value would be 0 months. If the participant is 16-days-old, the value would be 1 month.""",
             '', 'M = Male; F = Female; O=Other; NR = Not reported']
    Aliases = ['', '', '', '', '']

    definitions_df = pd.DataFrame({'ElementName': ElementName, 'DataType': DataType, 'Size': Size, 'Required': Required,
                                  'ElementDescription': ElementDescription, 'ValueRange': ValueRange, 'Notes': Notes,
                                  'Aliases': Aliases})

    ### Join and write NDA definitions file
    definitions_df = pd.concat([definitions_df, df], ignore_index=True)
    definitions_df.to_csv(f'background/nda/{output_file}01_defintions.csv', index=False)

    fields = list(definitions_df.ElementName)
    labels = [output_file, '01'] + ['']*(len(fields) - 2)
    template_df = pd.DataFrame(list(zip(labels, fields))).T
    template_df.to_csv(f'background/nda/{output_file}01_template.csv', index=False, header=False)


    return


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
    generate_template(vlmd_file_name, output_file)

    return


if __name__ == "__main__":
    main()

