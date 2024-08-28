"""Transform to NDA submission format (i.e., wide format).

Assumes that event and date_administered together unique determine a single
administration of the instrument for a given participant.
"""

from frictionless import Plugin, Step, system, describe
import pandas as pd
import petl as etl

class koos(Step):
    type = 'koos'

    def transform_resource(self, resource):
        df = resource.to_pandas().set_index(['participant_id','event',
                                             'date_administered','instance',
                                             'which_knee','dob','sex'])
        columns = df.columns.tolist()
        idx = pd.MultiIndex.from_product(
                 [['right','left'],df.columns.tolist()],
                 names=['which_knee',None]).reorder_levels(order=[1,0])
        df = df.unstack(level=-3).reindex(idx, axis=1).reset_index()
        df.columns = df.columns.to_flat_index()
        df = (df
              .rename(columns={('participant_id',''): 'participant_id',
                               ('event',''): 'event',
                               ('date_administered',''): 'date_administered',
                               ('instance',''): 'instance',
                               ('dob',''): 'dob',
                               ('sex',''): 'sex',
                               ('KOOSpainFreqScl','right'): 'pain_rkfr',
                               ('KOOSpainWalkFlatScl','right'): 'pain_rkn1',
                               ('KOOSpainStairsScl','right'): 'pain_rkn2',
                               ('KOOSpainSitLyingScl','right'): 'pain_rkn4',
                               ('KOOSFuncDiffRiseSitScl','right'): 'diff_rkn10',
                               ('KOOSFuncDiffStandScl','right'): 'diff_rkn4',
                               ('KOOSFuncDiffCarScl','right'): 'diff_rkn7',
                               ('KOOSpainScoreT','right'): 'koos_rkpain',
                               ('KOOSpainFreqScl','left'): 'pain_lkfr',
                               ('KOOSpainWalkFlatScl','left'): 'pain_lkn1',
                               ('KOOSpainStairsScl','left'): 'pain_lkn2',
                               ('KOOSpainSitLyingScl','left'): 'pain_lkn4',
                               ('KOOSFuncDiffRiseSitScl','left'): 'diff_lkn10',
                               ('KOOSFuncDiffStandScl','left'): 'diff_lkn4',
                               ('KOOSFuncDiffCarScl','left'): 'diff_lkn7',
                               ('KOOSpainScoreT','left'): 'koos_lkpain'})
              # Recover proper types
              .assign(pain_rkfr=lambda x: x.pain_rkfr.astype('Int64'),
                      pain_rkn1=lambda x: x.pain_rkn1.astype('Int64'),
                      pain_rkn2=lambda x: x.pain_rkn2.astype('Int64'),
                      pain_rkn4=lambda x: x.pain_rkn4.astype('Int64'),
                      diff_rkn3=lambda x: x.diff_rkn3.astype('Int64'),
                      diff_rkn4=lambda x: x.diff_rkn4.astype('Int64'),
                      diff_rkn7=lambda x: x.diff_rkn7.astype('Int64'),
                      pain_lkfr=lambda x: x.pain_lkfr.astype('Int64'),
                      pain_lkn1=lambda x: x.pain_lkn1.astype('Int64'),
                      pain_lkn2=lambda x: x.pain_lkn2.astype('Int64'),
                      pain_lkn4=lambda x: x.pain_lkn4.astype('Int64'),
                      diff_lkn3=lambda x: x.diff_lkn3.astype('Int64'),
                      diff_lkn4=lambda x: x.diff_lkn4.astype('Int64'),
                      diff_lkn7=lambda x: x.diff_lkn7.astype('Int64'))
              # TODO NDA structure collapses these items over both knees
              .assign(qol_kn1=df[[('KOOSQOLKneeAwareScl','right'),
                                  ('KOOSQOLKneeAwareScl','left')]
                                ].mean(axis=1).round().astype('Int64'),
                      qol_kn2=df[[('KOOSQOLlifestyleModScl','right'),
                                  ('KOOSQOLlifestyleModScl','left')]
                                ].mean(axis=1).round().astype('Int64'),
                      qol_kn3=df[[('KOOSQOLConfidenceScl','right'),
                                  ('KOOSQOLConfidenceScl','left')]
                                ].mean(axis=1).round().astype('Int64'),
                      qol_kn4=df[[('KOOSQOLkneeDifficultyScl','right'),
                                  ('KOOSQOLkneeDifficultyScl','left')]
                                ].mean(axis=1).round().astype('Int64'),
                      diff_kn4=df[[('KOOSFunctwistPivotScl','right'),
                                   ('KOOSFunctwistPivotScl','left')]
                                 ].mean(axis=1).round().astype('Int64'),
                      koos_qol=df[[('KOOSQOLScoreT','right'),
                                   ('KOOSQOLScoreT','left')]
                                 ].mean(axis=1),
                      koos_sports=df[[('KOOSfunctionScoreT','right'),
                                      ('KOOSfunctionScoreT','left')]
                                    ].mean(axis=1))
              .drop(columns=[('KOOSQOLKneeAwareScl','right'),
                             ('KOOSQOLKneeAwareScl','left'),
                             ('KOOSQOLlifestyleModScl','right'),
                             ('KOOSQOLlifestyleModScl','left'),
                             ('KOOSQOLConfidenceScl','right'),
                             ('KOOSQOLConfidenceScl','left'),
                             ('KOOSQOLkneeDifficultyScl','right'),
                             ('KOOSQOLkneeDifficultyScl','left'),
                             ('KOOSFunctwistPivotScl','right'),
                             ('KOOSFunctwistPivotScl','left'),
                             ('KOOSfunctionScoreT','right'),
                             ('KOOSfunctionScoreT','left'),
                             ('KOOSQOLScoreT','right'),
                             ('KOOSQOLScoreT','left')], errors='ignore')
              # TODO NDA structure does not include these items
              .drop(columns=[('KOOSpainScore','right'),
                             ('KOOSpainScore','left'),
                             ('KOOSfunctionScore','right'),
                             ('KOOSfunctionScore','left'),
                             ('KOOSQOLScore','right'),
                             ('KOOSQOLScore','left'),
                             ('KOOSsummaryScore','right'),
                             ('KOOSsummaryScore','left')], errors='ignore')
              .convert_dtypes()
             )

        resource.schema = describe(df, type='schema')
        resource.data = etl.fromdataframe(df)

class KOOSPlugin(Plugin):
    def select_step_class(self, type):
        if type == 'koos':
            return koos

system.register('koos', KOOSPlugin())
