
from frictionless import Plugin, Step, system, describe
import pandas as pd
import numpy as np
import petl as etl

# Merge 'TAPSAlcoholUseMaleScl' & 'TAPSAlcoholUseFemaleScl' HEAL CDE fields to 'TAPSAlcoholUseScl' based on field 'sex'.
# Field 'TAPSAlcoholUseScl' will later be renamed 'past12mo_malefemale_alc' to match the NDA schema structure

class taps(Step):

    type = 'taps'

    def transform_resource(self, resource):
        df = resource.to_pandas()
        df['TAPSAlcoholUseScl'] = np.where(df['sex'] == 'Male',
                                           df['TAPSAlcoholUseMaleScl'],
                                           df['TAPSAlcoholUseFemaleScl'])

        df.drop(['TAPSAlcoholUseMaleScl', 'TAPSAlcoholUseFemaleScl'], axis=1, inplace=True)

        cols = ['TAPSTobaccoProductScl',
                'TAPSAlcoholUseScl',
                'TAPSDrugUseScl',
                'TAPSPrescriptionMedUseScl']

        # Map HEAL CDE 9=(not applicable) to NDA Structure 5=(prefer not to say)
        # All values (0,1,...,5) in the above cols are later shifted to (1,2,...,6) to fit the NDA Structure encoding
        for column in cols:
            df.loc[df[column] == 9, column] = 5

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)


class TAPSPlugin(Plugin):

    def select_step_class(self, type):
        if type == 'taps':
            return taps


system.register('taps', TAPSPlugin())
