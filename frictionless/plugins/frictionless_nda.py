"""Transform to NDA submission format."""

from frictionless import Plugin, Step, system, describe
from typing import Optional
import attrs
import numpy as np
import pandas as pd
import petl as etl


@attrs.define(kw_only=True)
class nda_required_fields(Step):
    type = 'nda-required-fields'

    guids: str
    pid: Optional[str] = 'participant_id'
    event: Optional[str] = 'event'
    date_admin: Optional[str] = 'date_administered'
    dob: Optional[str] = 'dob'
    sex: Optional[str] = 'sex'

    def transform_resource(self, resource):

        guids = self.guids
        pid = self.pid
        event = self.event
        date_admin = self.date_admin
        dob = self.dob
        sex = self.sex

        df = resource.to_pandas()
        for col in [pid,event,date_admin,dob,sex]:
            assert col in df

        gdf = pd.read_csv(guids)
        gdf.columns = gdf.columns.str.lower()
        df = df.merge(gdf[['record_id','guid']], how='left', left_on=pid,
                      right_on='record_id', indicator=True, validate='many_to_one')
        assert (df._merge == 'both').all()

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
                      version='heal_cde_1.0')
              .drop(columns=['record_id','_merge',date_admin,dob])
              .convert_dtypes()
             )

        req_cols = ['subjectkey','src_subject_id','interview_date',
                    'interview_age','sex','ageyears','visit','version']
        df = df[req_cols + [c for c in df.columns if c not in req_cols]]

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)

    metadata_profile_patch = {
        'properties': {
            'guids': {'type': 'string'},
            'pid': {'type': 'string'},
            'event': {'type': 'string'},
            'date_admin': {'type': 'string'},
            'dob': {'type': 'string'},
            'sex': {'type': 'string'}
        }
    }

class NDAPlugin(Plugin):
    def select_step_class(self, type):
        if type == 'nda-required-fields':
            return nda_required_fields

system.register('nda-required-fields', NDAPlugin())
