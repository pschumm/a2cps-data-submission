# Transform data for KOOS-12 from HEAL CDE to NDA structure

from frictionless import Pipeline, Resource
import os
import csv

os.makedirs('tmp/uploads', exist_ok=True)
with open('tmp/uploads/oai_koos_womac01.csv', 'w') as f:
    f.write('oai_koos_womac,01\n')
    pipeline = Pipeline.from_descriptor('generate_uploads/koos-12.json')
    Resource('tmp/heal_cde/koos-12.csv').transform(pipeline).\
        to_pandas().to_csv(f, index=False)
