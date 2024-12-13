import pandas as pd
import numpy as np
from random import randint
from datetime import date


def generate_gad7_test():
    cols = ['GAD2FeelNervScl',
            'GAD2NotStopWryScl',
            'GAD7WryTooMchScl',
            'GAD7TroubRelxScl',
            'GAD7RstlessScl',
            'GAD7EasyAnnoyedScl',
            'GAD7FeelAfrdScl',
            'GAD7TotScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100
    df['language'] = ['English', 'Spanish'] * 50

    for i in range(0, len(cols)):
        df[cols[i]] = [randint(0, 3) for p in range(0, 100)]

    return df


def generate_phq9_test():
    cols = ['PHQLitIntrstScore',
            'PHQDeprssnScore',
            'PHQSleepImpairScore',
            'PHQTirdLittleEnrgyScore',
            'PHQAbnrmlDietScore',
            'PHQFlngFailrScore',
            'PHQConcntrtnImprmntScore',
            'PHQMovmntSpchImprmntScore',
            'PHQBttrDdThghtScore',
            'PHQTotalScore',
            'PHQDiffcltyPerfScl']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100
    df['language'] = ['English', 'Spanish'] * 50
    for i in range(0, len(cols)):
        if i == 10:
            df[cols[i]] = [randint(0, 4) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 3) for p in range(0, 100)]


    return df


# For PROMIS Sleep Disturbance
def generate_promis_sleep_test():
    cols = ['PROMISSleepQualityScl',
            'PROMISSleepWasRefreshScl',
            'PROMISProblemWithSlpScl',
            'PROMISDifficltFallAslpScl',
            'PROMISSlpWasRestlessScl',
            'PROMISTryHardGetToSlpScl',
            'PROMISSlpDist6TotalScore',
            'PROMISSlpDist6TScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == 7:
            df[cols[i]] = [randint(1, 5)/10 for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(1, 5) for p in range(0, 100)]

    return df


def generate_promis_physical_func_test():
    cols = ['PFADoChoresScl',
            'PFAstairsScl',
            'PFAWalkScl',
            'PFARunErrandsScl',
            'PFAPhysLaborLimitScl',
            'PFAModWrkLimitScl',
            'PFAGrocLiftLimitScl',
            'PFAHeavyWorkLimitScl',
            'PFATotalScore',
            'PFATScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == 8:
            df[cols[i]] = [randint(8, 40) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(1, 5) for p in range(0, 100)]

    return df


def generate_pcs_test():
    cols = ['PCQPainAwfulOvrwhlmScl',
            'PCQFeelCantWithstandScl',
            'PCQAfraidPainWorseScl',
            'PCQHurtScl',
            'PCQPainStopScl',
            'PCQSeriousScl',
            'PCQTotalScoreVal']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()


    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)]*100
    df['sex'] = ['Male', 'Female']*50
    df['dob'] = [date(1985, 4, 23)]*100
    df['event'] = ['1']*100
    df['instance'] = ['1']*100

    for i in range(0, len(cols)):
        if i == 6:
            df[cols[i]] = [randint(0, 24) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 4) for p in range(0, 100)]

    return df


def generate_taps_test():
    cols = ['TAPSTobaccoProductScl',
            'TAPSAlcoholUseMaleScl',
            'TAPSAlcoholUseFemaleScl',
            'TAPSDrugUseScl',
            'TAPSPrescriptionMedUseScl',
            'TAPSOverallYN']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()


    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)]*100
    df['sex'] = ['Male', 'Female']*50
    df['dob'] = [date(1985, 4, 23)]*100
    df['event'] = ['1']*100
    df['instance'] = ['1']*100

    for i in range(0, len(cols)):
        if i == 1:
            df[cols[i]] = [1, 9]*50
        elif i == 2:
            df[cols[i]] = [9, 2] * 50
        elif i == 5:
            df[cols[i]] = [randint(0, 1) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 4) for p in range(0, 100)]
    return df


def generate_prscale_test():

    cols1 = ['PRSbackOutScl', 'PRSworkGoalsScl', 'PRSpushThroughScl', 'PRScontWorkScl', 'PRSStayActiveScl',
             'PRSfocusPositiveScl', 'PRSposAttitudeScl', 'PRSnotAffectHappyScl', 'PRSfindJoyScl',
             'PRShopefulScl', 'PRSNotGetDownScl', 'PRSNotUpsetScl', 'PRSavoidNegativeScl', 'PRSStayRelaxScl']

    cols2 = ['PRSscore', 'PRSBehPersScore', 'PRSCognitiveScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols1)):
        df[cols1[i]] = [randint(0, 4) for p in range(0, 100)]


    df[cols2[0]] = [randint(0, 56) for p in range(0, 100)]
    df[cols2[1]] = [randint(0, 20) for p in range(0, 100)]
    df[cols2[2]] = [randint(0, 36) for p in range(0, 100)]

    return df




#test_df = generate_gad7_test()
#test_df.to_csv('../input_healcde_structure/gad7_test.csv', index=False)

#test_df = generate_phq9_test()
#test_df.to_csv('../input_healcde_structure/phq9_test.csv', index=False)

#test_df = generate_promis_sleep_test()
#test_df.to_csv('../input_healcde_structure/promis_sleep_disturbance_test.csv', index=False)

test_df = generate_promis_physical_func_test()
test_df.to_csv('../input_healcde_structure/promis_physical_func_test.csv', index=False)

#test_df = generate_pcs_test()
#test_df.to_csv('../input_healcde_structure/pcs6_test.csv', index=False)

#test_df = generate_taps_test()
#test_df.to_csv('../input_healcde_structure/taps_test.csv', index=False)

#test_df = generate_prscale_test()
#test_df.to_csv('../input_healcde_structure/prscale_test.csv', index=False)

print(test_df.head(10))
#print(np.min(test_df))
#print(np.max(test_df))
print(test_df.dtypes)








