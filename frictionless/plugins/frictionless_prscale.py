
from frictionless import Plugin, Step, system, describe
import pandas as pd
import numpy as np
import petl as etl

class pain_resilience_scale(Step):

        type = 'pain_resilience_scale'

        def transform_resource(self, resource):

                df = resource.to_pandas()

                cols = ['PRSbackOutScl', 'PRSworkGoalsScl', 'PRSpushThroughScl', 'PRScontWorkScl', 'PRSStayActiveScl',
                        'PRSfocusPositiveScl', 'PRSposAttitudeScl', 'PRSnotAffectHappyScl', 'PRSfindJoyScl',
                        'PRShopefulScl', 'PRSNotGetDownScl', 'PRSNotUpsetScl', 'PRSavoidNegativeScl', 'PRSStayRelaxScl',
                        'PRSscore', 'PRSBehPersScore', 'PRSCognitiveScore']

                df[cols] = df[cols].astype(int)
                resource.schema = describe(df, type='schema')
                resource.data = etl.fromdataframe(df)


class PRScalePlugin(Plugin):

        def select_step_class(self, type):
                if type == 'pain_resilience_scale':
                        return pain_resilience_scale


system.register('pain_resilience_scale', PRScalePlugin())


