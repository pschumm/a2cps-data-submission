# Transform data for ESSF from HEAL CDE to NDA structure

from frictionless import Pipeline, Resource
import os
import csv

pipeline = Pipeline.from_descriptor({
    "steps": [{"type": "field-update",
               "name": "ESSFSomeoneListenScl",
               "descriptor": {"name": "prsupport13"}},
              {"type": "field-update",
               "name": "ESSFSomeoneConfideScl",
               "descriptor": {"name": "prsupport28"}},
              {"type": "field-update",
               "name": "ESSFFeelAppreciatScl",
               "descriptor": {"name": "prsupport20"}},
              {"type": "field-update",
               "name": "ESSFTalkBadDayScl",
               "descriptor": {"name": "prsupport24"}},
              {"type": "field-update",
               "name": "ESSFUnderstandProbScl",
               "descriptor": {"name": "prsupport16"}},
              {"type": "field-update",
               "name": "ESSFTalkFeelingsScl",
               "descriptor": {"name": "prsupport21"}},
              {"type": "field-update",
               "name": "ESSF6aTotalScore",
               "descriptor": {"name": "prsupport40"}},
              {"type": "field-update",
               "name": "ESSF6aTScore",
               "descriptor": {"name": "prsupport41"}},
              {"type": "nda-required-fields",
               "guids": "ids/guids.csv",
               "nda_cols": ["subjectkey",
                            "src_subject_id",
                            "interview_date",
                            "interview_age",
                            "sex",
                            "version_form"],
               "version": "healcde6181_1.0"}]
})

os.makedirs('tmp/uploads', exist_ok=True)
with open('tmp/uploads/prsupport.csv', 'w') as f:
    f.write('prsupport,01\n')
    Resource('tmp/heal_cde/prsupport.csv').transform(pipeline).\
        to_pandas().to_csv(f, index=False)
