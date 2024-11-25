# Transform data for KOOS-12 from HEAL CDE to NDA structure

from frictionless import Pipeline, Resource
import os
import csv
import argparse

def output_nda(filepath, header, descriptor, heal_cde):
    print(filepath)
    with open(filepath, 'w') as f:
        f.write(header)
        pipeline = Pipeline.from_descriptor( descriptor)
        Resource(heal_cde).transform(pipeline).\
            to_pandas().to_csv(f, index=False)
    return

def output_koos(filepath='tmp/uploads/oai_koos_womac01.csv', 
                header='oai_koos_womac,01\n',
                descriptor='generate_uploads/koos-12.json',
                heal_cde='tmp/heal_cde/koos-12.csv'):
    output_nda(filepath, header,  descriptor, heal_cde)
    return

def output_prsupport(filepath='tmp/uploads/prsupport.csv', 
                header='prsupport,01\n',
                descriptor='generate_uploads/prsupport.json',
                heal_cde='tmp/heal_cde/prsupport.csv'):
    output_nda(filepath, header, descriptor, heal_cde)
    return

def output_taps(filepath='tmp/uploads/taps.csv', 
                header='taps,01\n',
                descriptor='generate_uploads/taps.json',
                heal_cde='tmp/heal_cde/taps1.csv'):
    output_nda(filepath, header, descriptor, heal_cde)
    return


def main(arg_vals):
    output_methods = {'koos': output_koos,
                      'prsupport': output_prsupport,
                      'taps': output_taps}
    
    if arg_vals["nda_outputs"] == 'all':
        print('outputing all')
        for k,v in output_methods.items():
            v()
    else: 
        for output in arg_vals["nda_outputs"]:
            print("outputing", output)
            output_methods[output]()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nda_outputs", 
                        nargs="*",
                        choices=['all', 'prsupport', 'koos', 'taps'],
                        default='all',
                        help="List of NDA structure to output, defaults to all, \
                        but can pass multiple as well, ex: python generate_uploads/create_nda.py koos prsupport taps")
    args = parser.parse_args()
    main(vars(args))
