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


def generate_psd_test():
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


test_df = generate_gad7_test()
test_df.to_csv('../input_healcde_structure/gad7_test.csv', index=False)

test_df = generate_phq9_test()
test_df.to_csv('../input_healcde_structure/phq9_test.csv', index=False)

test_df = generate_psd_test()
test_df.to_csv('../input_healcde_structure/psd_test.csv', index=False)

test_df = generate_pcs_test()
test_df.to_csv('../input_healcde_structure/pcs6_test.csv', index=False)

test_df = generate_taps_test()
test_df.to_csv('../input_healcde_structure/taps_test.csv', index=False)

print(test_df.head(10))
#print(np.min(test_df))
#print(np.max(test_df))
print(test_df.dtypes)









