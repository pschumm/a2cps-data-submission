# A2CPS: Extract data for KOOS-12 and transform to HEAL CDE format

# TODO Do we want to recompute the scale scores here, for replicability?

from dataforge.sources.redcap import REDCapProject
from dataforge.ids import replace_ids
from dataforge import tools
from pathlib import Path

project = REDCapProject('A2CPSMainStudy')
data = project.data(['Postconsent Study Plan Crf V06',
                     'Patient Demographics Baseline v0.3 (Demographics I)',
                     'Pain Detect Questionnaire (PD-Q)',
                     'Knee Injury Osteoarthritis Outcome Score  (KOOS-12)'])

# Replace REDCap record IDs
Path('tmp').mkdir(exist_ok=True)
data = replace_ids(data, 'ids/ids.csv', 'tmp/id_map.csv')

# Shift dates
shift = tools.date_offset(data.index.get_level_values(0).\
                          to_series(name='participant_id'),
                          offset_file='tmp/offsets.csv', seed=5398038)
data = data.dataforge.shift_dates(shift)

codes = {'None':0,
        'Mild':1,
        'Moderate':2,
        'Severe':3,
        'Extreme':4}
cde = (data
       .dropna(how='all', subset=['koospainfreqscl',
                                  'koospainwalkflatscl',
                                  'koospainstairsscl',
                                  'koospainsitlyingscl',
                                  'koosfuncdiffrisesitscl',
                                  'koosfuncdiffstandscl',
                                  'koosfuncdiffcarscl',
                                  'koosfunctwistpivotscl',
                                  'koosqolkneeawarescl',
                                  'koosqollifestylemodscl',
                                  'koosqolconfidencescl',
                                  'koosqolkneedifficultyscl',
                                  'koospainscore',
                                  'koospainscoret',
                                  'koosfunctionscore',
                                  'koosfunctionscoret',
                                  'koosqolscore',
                                  'koosqolscoret',
                                  'koossummaryscore'])
       .assign(instance=None)
       .rename(columns={'pdqassessdate':'date_administered',
                        'sp_surgsite':'which_knee',
                        'brthdtc':'dob',
                        'koospainfreqscl':'KOOSpainFreqScl',
                        'koospainwalkflatscl':'KOOSpainWalkFlatScl',
                        'koospainstairsscl':'KOOSpainStairsScl',
                        'koospainsitlyingscl':'KOOSpainSitLyingScl',
                        'koosfuncdiffrisesitscl':'KOOSFuncDiffRiseSitScl',
                        'koosfuncdiffstandscl':'KOOSFuncDiffStandScl',
                        'koosfuncdiffcarscl':'KOOSFuncDiffCarScl',
                        'koosfunctwistpivotscl':'KOOSFunctwistPivotScl',
                        'koosqolkneeawarescl':'KOOSQOLKneeAwareScl',
                        'koosqollifestylemodscl':'KOOSQOLlifestyleModScl',
                        'koosqolconfidencescl':'KOOSQOLConfidenceScl',
                        'koosqolkneedifficultyscl':'KOOSQOLkneeDifficultyScl',
                        'koospainscore':'KOOSpainScore',
                        'koospainscoret':'KOOSpainScoreT',
                        'koosfunctionscore':'KOOSfunctionScore',
                        'koosfunctionscoret':'KOOSfunctionScoreT',
                        'koosqolscore':'KOOSQOLScore',
                        'koosqolscoret':'KOOSQOLScoreT',
                        'koossummaryscore':'KOOSsummaryScore'})
       .replace({'which_knee':{'Left Knee':'left',
                               'Right Knee':'right'},
                 'KOOSpainFreqScl':{'Never':0,
                                    'Monthly':1,
                                    'Weekly':2,
                                    'Daily':3,
                                    'Always':4},
                 'KOOSpainWalkFlatScl':codes,
                 'KOOSpainStairsScl':codes,
                 'KOOSpainSitLyingScl':codes,
                 'KOOSFuncDiffRiseSitScl':codes,
                 'KOOSFuncDiffStandScl':codes,
                 'KOOSFuncDiffCarScl':codes,
                 'KOOSFunctwistPivotScl':codes,
                 'KOOSQOLKneeAwareScl':{'Never':0,
                                        'Monthly':1,
                                        'Weekly':2,
                                        'Daily':3,
                                        'Constantly':4},
                 'KOOSQOLlifestyleModScl':{'Not at all':0,
                                           'Mildly':1,
                                           'Moderately':2,
                                           'Severely':3,
                 # TODO Should be 'Totally' according to HEAL CDE and NDA structure
                                           'Extremely':4},
                 'KOOSQOLConfidenceScl':{'Not at all':0,
                                         'Mildly':1,
                                         'Moderately':2,
                                         'Severely':3,
                                         'Extremely':4},
                 'KOOSQOLkneeDifficultyScl':codes})
      )[['date_administered','instance','which_knee','dob','sex',
         'KOOSpainFreqScl','KOOSpainWalkFlatScl','KOOSpainStairsScl',
         'KOOSpainSitLyingScl','KOOSFuncDiffRiseSitScl','KOOSFuncDiffStandScl',
         'KOOSFuncDiffCarScl','KOOSFunctwistPivotScl','KOOSQOLKneeAwareScl',
         'KOOSQOLlifestyleModScl','KOOSQOLConfidenceScl',
         'KOOSQOLkneeDifficultyScl','KOOSpainScore','KOOSpainScoreT',
         'KOOSfunctionScore','KOOSfunctionScoreT','KOOSQOLScore',
         'KOOSQOLScoreT','KOOSsummaryScore']]

# Write to delimited file
Path('tmp/heal_cde').mkdir(exist_ok=True)
cde.to_csv('tmp/heal_cde/koos-12.csv')
