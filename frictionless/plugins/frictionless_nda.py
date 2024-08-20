"""Add NDA required and/or common fields."""

from frictionless import Plugin, Step, system, describe
from typing import Optional, List
import attrs
import numpy as np
import pandas as pd
import petl as etl

@attrs.define(kw_only=True)
class nda_required_fields(Step):
    type = 'nda-required-fields'

    guids: str
    nda_cols: List[str]
    version: str
    pid: Optional[str] = 'participant_id'
    event: Optional[str] = 'event'
    date_admin: Optional[str] = 'date_administered'
    instance: Optional[str] = 'instance'
    dob: Optional[str] = 'dob'
    sex: Optional[str] = 'sex'

    def transform_resource(self, resource):

        guids = self.guids
        nda_cols = self.nda_cols
        version = self.version
        pid = self.pid
        event = self.event
        date_admin = self.date_admin
        instance = self.instance
        dob = self.dob
        sex = self.sex

        df = resource.to_pandas()
        extra_flds = [pid, event, date_admin, instance, dob, sex]
        for col in extra_flds:
            assert col in df
        flds = [c for c in df.columns if c not in extra_flds]

        gdf = pd.read_csv(guids)
        gdf.columns = gdf.columns.str.lower()
        df = df.merge(gdf[[pid,'guid']], how='left', left_on=pid,
                      right_on=pid, indicator=True, validate='many_to_one')
        if (df._merge != 'both').any():
            print(df.loc[df._merge != 'both', pid].to_list())
            raise Exception(f'Values of {pid} listed above are not mapped ' +
                            f'to GUIDs in {guids}.')

        df = (df
              .rename(columns={'guid':'subjectkey',
                               pid:'src_subject_id',
                               sex:'sex',
                               event:'visit'})
              .replace({'sex':{'Female':'F',
                               'Intersex':'O',
                               'Male':'M',
                               np.nan:'NR'}})
              .assign(interview_date=df[date_admin].dt.strftime('%m/%d/%Y'),
                      interview_age=(df[date_admin].dt.year*12
                                     + df[date_admin].dt.month
                                     - (df[dob].dt.year*12 + df[dob].dt.month)
                                    ),
                      ageyears=df.apply(
                          lambda x: x[date_admin].year - x[dob].year -
                                    ((x[date_admin].month, x[date_admin].day)
                                     < (x[dob].month, x[dob].day)),
                          axis=1
                      ),
                      version=version,
                      version_form=version)
              .drop(columns=['_merge',date_admin,dob])
              .convert_dtypes()
             )[nda_cols + flds]

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)

    metadata_profile_patch = {
        'properties': {
            'guids': {'type': 'string'},
            'nda_cols': {'type': 'array'},
            'version': {'type': 'string'},
            'pid': {'type': 'string'},
            'event': {'type': 'string'},
            'date_admin': {'type': 'string'},
            'instance': {'type': 'string'},
            'dob': {'type': 'string'},
            'sex': {'type': 'string'}
        }
    }

class NDAPlugin(Plugin):
    def select_step_class(self, type):
        if type == 'nda-required-fields':
            return nda_required_fields

system.register('nda-required-fields', NDAPlugin())
