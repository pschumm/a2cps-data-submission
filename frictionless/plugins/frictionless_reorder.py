
from frictionless import Plugin, Step, system, describe
from typing import Optional, List
import pandas as pd
import numpy as np
import petl as etl
import attrs


@attrs.define(kw_only=True)
class reorder(Step):

    type = 'reorder'
    cols: List[str]

    def transform_resource(self, resource):

        cols = self.cols

        df = resource.to_pandas()
        df = df[cols]

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)


    metadata_profile_patch = {
        'properties': {
            'cols': {'type': 'array'}
        }
    }

class REORDERPlugin(Plugin):

    def select_step_class(self, type):
        if type == 'reorder':
            return reorder


system.register('reorder', REORDERPlugin())