# A2CPS: Extract data from RedCap and transform to HEAL CDE format

from dataforge.sources.redcap import REDCapProject
from dataforge.ids import replace_ids
from dataforge import tools
from pathlib import Path
from filter import filter_records_events, get_filter_list, reformat_to_cde
import csv
import pandas as pd
import os
from dotenv import load_dotenv

def extract_koos(data):
   # TODO Do we want to recompute the scale scores here, for replicability?
   codes = {'None':0,
         'Mild':1,
         'Moderate':2,
         'Severe':3,
         'Extreme':4}

   koos = reformat_to_cde(data, 
            drop_if_all_null = ['koospainfreqscl',
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
                           'koossummaryscore'],
            null_assignments = {"instance":None},
            rename_columns = {'pdqassessdate':'date_administered',
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
               'koossummaryscore':'KOOSsummaryScore'},
            replace_values = {'which_knee':{'Left Knee':'left',
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
                     'KOOSQOLkneeDifficultyScl':codes},
            output_columns = ['date_administered','instance','which_knee','dob','sex',
            'KOOSpainFreqScl','KOOSpainWalkFlatScl','KOOSpainStairsScl',
            'KOOSpainSitLyingScl','KOOSFuncDiffRiseSitScl','KOOSFuncDiffStandScl',
            'KOOSFuncDiffCarScl','KOOSFunctwistPivotScl','KOOSQOLKneeAwareScl',
            'KOOSQOLlifestyleModScl','KOOSQOLConfidenceScl',
            'KOOSQOLkneeDifficultyScl','KOOSpainScore','KOOSpainScoreT',
            'KOOSfunctionScore','KOOSfunctionScoreT','KOOSQOLScore',
            'KOOSQOLScoreT','KOOSsummaryScore']
            )
   # Write to delimited file
   Path('tmp/heal_cde').mkdir(exist_ok=True)
   koos.to_csv('tmp/heal_cde/koos-12.csv')
   return

def extract_promis(data):
   codes = {'Never':1,
            'Rarely':2,
            'Sometimes':3,
            'Usually':4,
            'Always':5}
   prsupport = reformat_to_cde(data,
                  drop_if_all_null=['essfsomeonelistenscl',
                                    'essfsomeoneconfidescl',
                                    'essffeelappreciatscl',
                                    'essftalkbaddayscl',
                                    'essfunderstandprobscl',
                                    'essftalkfeelingsscl',
                                    'essf6atotalscore'],
                  null_assignments = {"instance": None, "ESSF6aTScore": None},
                  rename_columns={'pdqassessdate':'date_administered',
                           'brthdtc':'dob',
                           'essfsomeonelistenscl':'ESSFSomeoneListenScl',
                           'essfsomeoneconfidescl':'ESSFSomeoneConfideScl',
                           'essffeelappreciatscl':'ESSFFeelAppreciatScl',
                           'essftalkbaddayscl':'ESSFTalkBadDayScl',
                           'essfunderstandprobscl':'ESSFUnderstandProbScl',
                           'essftalkfeelingsscl':'ESSFTalkFeelingsScl',
                           'essf6atotalscore':'ESSF6aTotalScore'},
                  replace_values={'ESSFSomeoneListenScl':codes,
                  'ESSFSomeoneConfideScl':codes,
                  'ESSFFeelAppreciatScl':codes,
                  'ESSFTalkBadDayScl':codes,
                  'ESSFUnderstandProbScl':codes,
                  'ESSFTalkFeelingsScl':codes},
                  output_columns=['date_administered','instance','dob','sex','ESSFSomeoneListenScl',
                  'ESSFSomeoneConfideScl','ESSFFeelAppreciatScl','ESSFTalkBadDayScl',
                  'ESSFUnderstandProbScl','ESSFTalkFeelingsScl','ESSF6aTotalScore',
                  'ESSF6aTScore']
                  )

   # Write to delimited file
   prsupport.to_csv('tmp/heal_cde/prsupport.csv')
   return

def extract_taps1(data):
   t1codes = {'Daily or Almost Daily': 0,
            'Less Than Monthly': 3,
            'Monthly': 2,
            'Never': 4,
            'Not Applicable': 9,
            'Weekly': 1}

   taps = reformat_to_cde(data,
            drop_if_all_null=['tapstobaccoproductscl',
               'tapstobaccoproductscl_yrs',
               'tapsalcoholusemalescl',
               'tapsalcoholusefemalescl',
               'tapsdrugusescl',
               'tapsprescriptionmedusescl'
               ],
            null_assignments = {"instance": None,"TAPSOverallYN": None},
            rename_columns={'pdqassessdate':'date_administered',
                     'brthdtc':'dob',
                     # TO DO request NDA add 'tapstobaccoproductscl_yrs'
                     'tapstobaccoproductscl': 'TAPSTobaccoProductScl',
                     'tapsalcoholusemalescl': 'TAPSAlcoholUseMaleScl',
                     'tapsalcoholusefemalescl': 'TAPSAlcoholUseFemaleScl',
                     'tapsdrugusescl': 'TAPSDrugUseScl',
                     # TO DO add caluclation for 'TAPSOverallYN',
                     'tapsprescriptionmedusescl': 'TAPSPrescriptionMedUseScl'},
            replace_values={'TAPSAlcoholUseFemaleScl':t1codes,
               'TAPSAlcoholUseMaleScl':t1codes,
               'TAPSDrugUseScl':t1codes,
               'TAPSPrescriptionMedUseScl':t1codes,
               'TAPSTobaccoProductScl':t1codes},
            output_columns=['date_administered','instance','dob','sex',
                              'TAPSTobaccoProductScl', 'TAPSAlcoholUseMaleScl', 
                              'TAPSAlcoholUseFemaleScl', 'TAPSDrugUseScl', 
                              'TAPSPrescriptionMedUseScl', 'TAPSOverallYN']
            )

   # Write to delimited file
   taps.to_csv('tmp/heal_cde/taps1.csv')
   return


def main():
   project = REDCapProject('A2CPSMainStudy')
   #project = REDCapProject('A2CPSMCC2TKA')
   data = project.data(['Postconsent Study Plan Crf V06',
                        'Patient Demographics Baseline v0.3 (Demographics I)',
                        'Pain Detect Questionnaire (PD-Q)',
                        'Knee Injury Osteoarthritis Outcome Score  (KOOS-12)',
                        'PROMIS SF v2.0 - Emotional Support 6a',
                        'TAPS-1',
                        'TAPS-2'
                        ])
   # get freeze ids 
   record_ids = get_filter_list('/Users/urrutia/Downloads/DataFreeze_2_022924.csv')
   # baseline only
   events = ['Baseline Visit']
   data = filter_records_events(data, record_ids, events)
   data.index.names = ['participant_id', 'event']


   # load set offset from env file
   load_dotenv()
   day_offset = int(os.getenv("DAY_OFFSET"))

   shift = tools.date_offset(data.index.get_level_values(0).\
                           to_series(name='participant_id'), 
                           offset_file='tmp/offsets.csv', 
                           min_days=day_offset , max_days=day_offset)
   data = data.dataforge.shift_dates(shift)
   data.dropna(axis=0, how='any', subset=['pdqassessdate','brthdtc'], inplace=True)

   extract_koos(data)
   extract_promis(data)
   extract_taps1(data)



if __name__ == '__main__':
    main()
