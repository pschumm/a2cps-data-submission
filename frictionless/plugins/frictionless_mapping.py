
from frictionless import Plugin, Step, system, describe
from typing import Optional, List
import pandas as pd
import numpy as np
import petl as etl
import attrs
import ast


@attrs.define(kw_only=True)
class mapping(Step):

    type = 'mapping'
    cols: List[str]
    mapping: str

    def transform_resource(self, resource):

        cols = self.cols
        mapping = self.mapping

        mapping = ast.literal_eval(mapping)

        df = resource.to_pandas()
        for col in cols:
            df[col] = df[col].map(mapping)

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)

    metadata_profile_patch = {
        'properties': {
            'cols': {'type': 'array'},
            'mapping': {'type': 'string'},
        }
    }

class MAPPINGPlugin(Plugin):

    def select_step_class(self, type):
        if type == 'mapping':
            return mapping


system.register('mapping', MAPPINGPlugin())