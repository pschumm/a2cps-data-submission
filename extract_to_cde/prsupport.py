# A2CPS: Extract data for PROMIS Emotional Support Short Form 6a

# TODO Calculate ESSF6aTScore and possibly recalculate ESSF6aTotalScore

from dataforge.sources.redcap import REDCapProject
from dataforge.ids import replace_ids
from pathlib import Path

project = REDCapProject('A2CPSMainStudy')
data = project.data(['Patient Demographics Baseline v0.3 (Demographics I)',
                     'Pain Detect Questionnaire (PD-Q)',
                     'PROMIS SF v2.0 - Emotional Support 6a'])

# Replace REDCap record IDs
data = replace_ids(data, 'ids/ids.csv', 'ids/id_map.csv')

# TODO Shift dates (dataforge package includes functionality for this)

codes = {'Never':1,
         'Rarely':2,
         'Sometimes':3,
         'Usually':4,
         'Always':5}
cde = (data
       .dropna(how='all', subset=['essfsomeonelistenscl',
                                  'essfsomeoneconfidescl',
                                  'essffeelappreciatscl',
                                  'essftalkbaddayscl',
                                  'essfunderstandprobscl',
                                  'essftalkfeelingsscl',
                                  'essf6atotalscore'])
       .rename_axis(index={'record_id':'participant_id'})
       .assign(instance=None,
               ESSF6aTScore=None)
       .rename(columns={'pdqassessdate':'date_administered',
                        'brthdtc':'dob',
                        'essfsomeonelistenscl':'ESSFSomeoneListenScl',
                        'essfsomeoneconfidescl':'ESSFSomeoneConfideScl',
                        'essffeelappreciatscl':'ESSFFeelAppreciatScl',
                        'essftalkbaddayscl':'ESSFTalkBadDayScl',
                        'essfunderstandprobscl':'ESSFUnderstandProbScl',
                        'essftalkfeelingsscl':'ESSFTalkFeelingsScl',
                        'essf6atotalscore':'ESSF6aTotalScore'})
       .replace({'ESSFSomeoneListenScl':codes,
                 'ESSFSomeoneConfideScl':codes,
                 'ESSFFeelAppreciatScl':codes,
                 'ESSFTalkBadDayScl':codes,
                 'ESSFUnderstandProbScl':codes,
                 'ESSFTalkFeelingsScl':codes})
      )[['date_administered','instance','dob','sex','ESSFSomeoneListenScl',
         'ESSFSomeoneConfideScl','ESSFFeelAppreciatScl','ESSFTalkBadDayScl',
         'ESSFUnderstandProbScl','ESSFTalkFeelingsScl','ESSF6aTotalScore',
         'ESSF6aTScore']]

# Write to delimited file
Path('tmp/heal_cde').mkdir(parents=True, exist_ok=True)
cde.to_csv('tmp/heal_cde/prsupport.csv')
