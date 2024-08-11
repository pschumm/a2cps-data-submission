# Transform data for ESSF from HEAL CDE to NDA structure

from frictionless import Pipeline, Resource
import os
import csv

os.makedirs('tmp/uploads', exist_ok=True)
with open('tmp/uploads/prsupport.csv', 'w') as f:
    f.write('prsupport,01\n')
    pipeline = Pipeline.from_descriptor('generate_uploads/prsupport.json')
    Resource('tmp/heal_cde/prsupport.csv').transform(pipeline).\
        to_pandas().to_csv(f, index=False)
