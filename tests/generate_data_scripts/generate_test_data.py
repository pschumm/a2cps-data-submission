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


def generate_rapa_test():
    cols = ['rapa_rarly', 'rapa_light', 'rapa_lightweekly', 'rapa_mod', 'rapa_vig', 'rapa_modweekly',
            'rapa_vigweekly', 'rapa_strength', 'rapa_flex', 'rapa_1Score', 'rapa_1Cat', 'rapa_2Score']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == 9:
            df[cols[i]] = [randint(1, 7) for p in range(0, 100)]
        elif i == 10:
            df[cols[i]] = [randint(1, 5) for p in range(0, 100)]
        elif i == 11:
            df[cols[i]] = [randint(0, 3) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 1) for p in range(0, 100)]

    return df


def generate_bfi_test():
    cols = ['BFI10reserveScl', 'BFI10trustScl', 'BFI10lazyScl', 'BFI10relaxScl', 'BFI10artisticScl', 'BFI10outgoingScl',
            'BFI10faultScl', 'BFI10thoroughScl', 'BFI10nervousScl', 'BFI10actImaginScl', 'BFI10extravertScr',
            'BFI10agreeableScr', 'BFI10conscientScr', 'BFI10neuroticScr', 'BFI10openExperScr']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i > 9:
            df[cols[i]] = [randint(2, 10) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(1, 5) for p in range(0, 100)]

    return df


def generate_taps2_test():
    cols = ['TAPS2tobaccoYN', 'TAPS2tobaccoGr10YN', 'TAPS2tobaccoWakingYN', 'TAPS2alcoholYN', 'TAPS2alcoholFem4YN',
            'TAPS2alcoholMale5YN', 'TAPS2alcoholFailYN', 'TAPS2alcoholConcernYN', 'TAPS2mjUseYN', 'TAPS2mjWeeklyYN',
            'TAPS2mjConcernYN', 'TAPS2stimulantYN', 'TAPS2stimulantWeeklyYN', 'TAPS2stimulntConcernYN', 'TAPS2heroinYN',
            'TAPS2heroinFailYN', 'TAPS2heroinConcernYN', 'TAPS2RxOpiateYN', 'TAPS2RxOpiateFailYN',
            'TAPS2RxOpiateConcernYN', 'TAPS2anxietySlpMedYN', 'TAPS2anxietySlpWeeklyYN', 'TAPS2anxietySlpConcYN',
            'TAPS2adhdMedYN', 'TAPS2adhdMedWeeklyYN', 'TAPS2adhdMedConcernYN', 'TAPS2otherDrugsYN',
            'TAPS2otherDrugsTxt', 'TAPS2commentsTxt', 'TAP2tobaccoScore', 'TAP2alcoholScore', 'TAP2cannabisScore',
            'TAP2stimulantScore', 'TAP2heroinScore', 'TAP2opioidScore', 'TAP2sedativeScore', 'TAP2RXstimScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == 27 | i == 28:
            df[cols[i]] = 'test'
        elif i == 29 | i > 30:
            df[cols[i]] = [randint(0, 3) for p in range(0, 100)]
        elif i ==30:
            df[cols[i]] = [randint(0, 4) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 1) for p in range(0, 100)]

    return df


def generate_comm01_test():
    cols = ['COMMTrbThkClrPast30DayScl', 'COMMCompTaskPast30DayScl', 'COMMOthPhyscMedPst30DyScl',
            'COMMTakMedDifPast30DayScl', 'COMMHurtSelfPast30DayScl', 'COMMOpiThkPast30DayScl', 'COMMArgOftPast30DayScl',
            'COMMAngConPast30DayScl', 'COMMSomElsMedPast30DayScl', 'COMMHanMedWorPast30DayScl',
            'COMMOthWorryPast30DayScl', 'COMMEmeCalAppPast30DayScl', 'COMMAngrOftnPast30DayScl',
            'COMMTakMorMedPast30DayScl', 'COMMBorMedPast30DayScl', 'COMMOthSymPast30DayScl', 'COMMEmergRmPast30DayScl',
            'COMMtotalScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == (len(cols)-1):
            df[cols[i]] = [randint(0, 68) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(0, 4) for p in range(0, 100)]

    return df


def generate_ace_test():
    cols = ['ACEAdInHmHFrOfF18YrInCode', 'ACEAdPhyAbsInFr18YrInCode', 'ACESxlAbsFr18YrInCode',
            'ACEFlLcEmSpOfFr18YrInCode', 'ACEFlNgDHPrOfFr18YrInCode', 'ACEPrEvSpDvFr18YrInCode',
            'ACEMtDmVlFr18YrInCode', 'ACEAlDrUsLvFr18YrInCode', 'ACEDpMnIScHsMbFr18YInCode', 'ACEHsMmPrFr18YrInCode',
            'ACEAdvChlExpQstTtlScore']

    guids = pd.read_csv("../../ids/guids.csv")

    df = pd.DataFrame()

    df['participant_id'] = list(guids['participant_id'])[0:100]
    df['date_administered'] = [date(2015, 6, 3)] * 100
    df['sex'] = ['Male', 'Female'] * 50
    df['dob'] = [date(1985, 4, 23)] * 100
    df['event'] = ['1'] * 100
    df['instance'] = ['1'] * 100

    for i in range(0, len(cols)):
        if i == (len(cols) - 1):
            df[cols[i]] = [randint(0, 10) for p in range(0, 100)]
        else:
            df[cols[i]] = [randint(1, 5) for p in range(0, 100)]

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


test_df = generate_rapa_test()
test_df.to_csv('../input_healcde_structure/rapa_test.csv', index=False)

test_df = generate_bfi_test()
test_df.to_csv('../input_healcde_structure/bfi_test.csv', index=False)

test_df = generate_taps2_test()
test_df.to_csv('../input_healcde_structure/taps2_test.csv', index=False)

test_df = generate_comm01_test()
test_df.to_csv('../input_healcde_structure/comm01_test.csv', index=False)

test_df = generate_ace_test()
test_df.to_csv('../input_healcde_structure/ace_test.csv', index=False)


print(test_df.head(10))
#print(np.min(test_df))
#print(np.max(test_df))
print(test_df.dtypes)








