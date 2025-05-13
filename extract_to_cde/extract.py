# A2CPS: Extract data from RedCap and transform to HEAL CDE format

import argparse
import os
from pathlib import Path

import numpy as np
from dataforge import tools
from dataforge.sources.redcap import REDCapProject
from dotenv import load_dotenv
from filter import filter_records_events, get_filter_list, reformat_to_cde

def extract_taps2(data):
    t2codes = {"No": 0, "Yes": 1}

    taps = reformat_to_cde(
        data,
        drop_if_all_null=[
            "taps2tobaccoyn",
            "taps2tobaccogr10yn",
            "taps2tobaccogr10ycnt",
            "taps2tobaccowakingyn",
            "taps2alcoholyn",
            "taps2alcoholfem4yn",
            "taps2alcoholmale5yn",
            "taps2alcoholfailyn",
            "taps2alcoholconcernyn",
            "taps2mjuseyn",
            "taps2mjweeklyyn",
            "taps2mjconcernyn",
            "taps2stimulantyn",
            "taps2stimulantweeklyyn",
            "taps2stimulntconcernyn",
            "taps2heroinyn",
            "taps2heroinfailyn",
            "taps2heroinconcernyn",
            "taps2rxopiateyn",
            "taps2rxopiatefailyn",
            "taps2rxopiateconcernyn",
            "taps2anxietyslpmedyn",
            "taps2anxietyslpweeklyyn",
            "taps2anxietyslpconcyn",
            "taps2adhdmedyn",
            "taps2adhdmedweeklyyn",
            "taps2adhdmedconcernyn",
            "taps2otherdrugsyn",
            "taps2otherdrugstxt",
            "tap2tobaccoscore",
            "tap2alcoholscore",
            "tap2cannabisscore",
            "tap2stimulantscore",
            "tap2heroinscore",
            "tap2opioidscore",
            "tap2sedativescore",
            "tap2rxstimscore",
        ],
        null_assignments={"instance": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "taps2tobaccoyn": "TAPS2tobaccoYN",
            "taps2tobaccogr10yn": "TAPS2tobaccoGr10YN",
            "taps2tobaccowakingyn": "TAPS2tobaccoWakingYN",
            "taps2alcoholyn": "TAPS2alcoholYN",
            "taps2alcoholfem4yn": "TAPS2alcoholFem4YN",
            "taps2alcoholmale5yn": "TAPS2alcoholMale5YN",
            "taps2alcoholfailyn": "TAPS2alcoholFailYN",
            "taps2alcoholconcernyn": "TAPS2alcoholConcernYN",
            "taps2mjuseyn": "TAPS2mjUseYN",
            "taps2mjweeklyyn": "TAPS2mjWeeklyYN",
            "taps2mjconcernyn": "TAPS2mjConcernYN",
            "taps2stimulantyn": "TAPS2stimulantYN",
            "taps2stimulantweeklyyn": "TAPS2stimulantWeeklyYN",
            "taps2stimulntconcernyn": "TAPS2stimulntConcernYN",
            "taps2heroinyn": "TAPS2heroinYN",
            "taps2heroinfailyn": "TAPS2heroinFailYN",
            "taps2heroinconcernyn": "TAPS2heroinConcernYN",
            "taps2rxopiateyn": "TAPS2RxOpiateYN",
            "taps2rxopiatefailyn": "TAPS2RxOpiateFailYN",
            "taps2rxopiateconcernyn": "TAPS2RxOpiateConcernYN",
            "taps2anxietyslpmedyn": "TAPS2anxietySlpMedYN",
            "taps2anxietyslpweeklyyn": "TAPS2anxietySlpWeeklyYN",
            "taps2anxietyslpconcyn": "TAPS2anxietySlpConcYN",
            "taps2adhdmedyn": "TAPS2adhdMedYN",
            "taps2adhdmedweeklyyn": "TAPS2adhdMedWeeklyYN",
            "taps2adhdmedconcernyn": "TAPS2adhdMedConcernYN",
            "taps2otherdrugsyn": "TAPS2otherDrugsYN",
            "taps2otherdrugstxt": "TAPS2otherDrugsTxt",
            "tap2tobaccoscore": "TAP2tobaccoScore",
            "tap2alcoholscore": "TAP2alcoholScore",
            "tap2cannabisscore": "TAP2cannabisScore",
            "tap2stimulantscore": "TAP2stimulantScore",
            "tap2heroinscore": "TAP2heroinScore",
            "tap2opioidscore": "TAP2opioidScore",
            "tap2sedativescore": "TAP2sedativeScore",
            "tap2rxstimscore": "TAP2RXstimScore",
        },
        replace_values={
            "sex": {np.NaN: "Unknown", None: "Unknown"},
            "TAPS2anxietySlpWeeklyYN": t2codes,
            "TAPS2heroinFailYN": t2codes,
            "TAPS2alcoholFailYN": t2codes,
            "TAPS2adhdMedWeeklyYN": t2codes,
            "TAPS2mjConcernYN": t2codes,
            "TAPS2mjWeeklyYN": t2codes,
            "TAPS2alcoholMale5YN": t2codes,
            "TAPS2alcoholYN": t2codes,
            "TAPS2alcoholFem4YN": t2codes,
            "TAPS2adhdMedYN": t2codes,
            "TAPS2tobaccoYN": t2codes,
            "TAPS2stimulntConcernYN": t2codes,
            "TAPS2stimulantYN": t2codes,
            "TAPS2RxOpiateConcernYN": t2codes,
            "TAPS2tobaccoWakingYN": t2codes,
            "TAPS2otherDrugsTxt": t2codes,
            "TAPS2heroinConcernYN": t2codes,
            "TAPS2alcoholConcernYN": t2codes,
            "TAPS2heroinYN": t2codes,
            "TAPS2anxietySlpMedYN": t2codes,
            "TAPS2mjUseYN": t2codes,
            "TAPS2anxietySlpConcYN": t2codes,
            "TAPS2adhdMedConcernYN": t2codes,
            "TAPS2otherDrugsYN": t2codes,
            "TAPS2RxOpiateYN": t2codes,
            "TAPS2stimulantWeeklyYN": t2codes,
            "TAPS2tobaccoGr10YN": t2codes,
            "TAPS2RxOpiateFailYN": t2codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "TAPS2tobaccoYN",
            "TAPS2tobaccoGr10YN",
            "TAPS2tobaccoWakingYN",
            "TAPS2alcoholYN",
            "TAPS2alcoholFem4YN",
            "TAPS2alcoholMale5YN",
            "TAPS2alcoholFailYN",
            "TAPS2alcoholConcernYN",
            "TAPS2mjUseYN",
            "TAPS2mjWeeklyYN",
            "TAPS2mjConcernYN",
            "TAPS2stimulantYN",
            "TAPS2stimulantWeeklyYN",
            "TAPS2stimulntConcernYN",
            "TAPS2heroinYN",
            "TAPS2heroinFailYN",
            "TAPS2heroinConcernYN",
            "TAPS2RxOpiateYN",
            "TAPS2RxOpiateFailYN",
            "TAPS2RxOpiateConcernYN",
            "TAPS2anxietySlpMedYN",
            "TAPS2anxietySlpWeeklyYN",
            "TAPS2anxietySlpConcYN",
            "TAPS2adhdMedYN",
            "TAPS2adhdMedWeeklyYN",
            "TAPS2adhdMedConcernYN",
            "TAPS2otherDrugsYN",
            "TAPS2otherDrugsTxt",
            # "TAPS2commentsTxt",
            "TAP2tobaccoScore",
            "TAP2alcoholScore",
            "TAP2cannabisScore",
            "TAP2stimulantScore",
            "TAP2heroinScore",
            "TAP2opioidScore",
            "TAP2sedativeScore",
            "TAP2RXstimScore",
        ],
    )

    # Write to delimited file
    taps.to_csv("tmp/heal_cde/taps2.csv")
    return

def extract_promis_fatigue(data):
    codes = {
        "Never": 1,
        "Rarely": 2,
        "Sometimes": 3,
        "Often": 4,
        "Always": 5,
        "": None,
    }

    # TODO: add scores (raw and t)
    # TODO: add fat_se and fat_theta (needed in NDA)
    cde = reformat_to_cde(
        data,
        drop_if_all_null=[
            "fat7atiredscl",
            "fat7aexhaustionscl",
            "fat7anoenergytscl",
            "fat7aworklimitscl",
            "fat7athinkclearscl",
            "fat7abathscl",
            "fat7aexercisescl",
        ],
        null_assignments={"instance": None},
        rename_columns={
            "brthdtc": "dob",
            "pdqassessdate": "date_administered",
            "fat7atiredscl": "FAT7AtiredScl",
            "fat7aexhaustionscl": "FAT7AExhaustionScl",
            "fat7anoenergytscl": "FAT7AnoEnergytScl",
            "fat7aworklimitscl": "FAT7AworkLimitScl",
            "fat7athinkclearscl": "FAT7AthinkClearScl",
            "fat7abathscl": "FAT7AbathScl",
            "fat7aexercisescl": "FAT7AexerciseScl",
        },
        replace_values={
            "sex": {np.NaN: "Unknown", None: "Unknown"},
            "FAT7AExhaustionScl": codes,
            "FAT7AexerciseScl": codes,
            "FAT7AworkLimitScl": codes,
            "FAT7aTotalScore": codes,
            "FAT7aTScore": codes,
            "FAT7AnoEnergytScl": codes,
            "FAT7AtiredScl": codes,
            "FAT7AthinkClearScl": codes,
            "FAT7AbathScl": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "FAT7AtiredScl",
            "FAT7AExhaustionScl",
            "FAT7AnoEnergytScl",
            "FAT7AworkLimitScl",
            "FAT7AthinkClearScl",
            "FAT7AbathScl",
            "FAT7AexerciseScl",
        ],
    )
    # Write to delimited file
    Path("tmp/heal_cde").mkdir(exist_ok=True)
    cde.to_csv("tmp/heal_cde/promis_fatigue.csv")
    return


def extract_ace(data):
    codes = {"No": 0, "Yes": 1, np.NaN: -9, None: -9}

    ace = reformat_to_cde(
        data,
        drop_if_all_null=[
            "aceadinhmhfroff18yrincode",
            "aceadphyabsinfr18yrincode",
            "acesxlabsfr18yrincode",
            "acefllcemspoffr18yrincode",
            "aceflngdhproffr18yrincode",
            "aceprevspdvfr18yrincode",
            "acemtdmvlfr18yrincode",
            "acealdruslvfr18yrincode",
            "acedpmnischsmbfr18yincode",
            "acehsmmprfr18yrincode",
            "aceadvchlexpqstttlscore",
        ],
        null_assignments={"instance": None},
        rename_columns={
            "brthdtc": "dob",
            "pdqassessdate": "date_administered",
            "aceadinhmhfroff18yrincode": "ACEAdInHmHFrOfF18YrInCode",
            "aceadphyabsinfr18yrincode": "ACEAdPhyAbsInFr18YrInCode",
            "acesxlabsfr18yrincode": "ACESxlAbsFr18YrInCode",
            "acefllcemspoffr18yrincode": "ACEFlLcEmSpOfFr18YrInCode",
            "aceflngdhproffr18yrincode": "ACEFlNgDHPrOfFr18YrInCode",
            "aceprevspdvfr18yrincode": "ACEPrEvSpDvFr18YrInCode",
            "acemtdmvlfr18yrincode": "ACEMtDmVlFr18YrInCode",
            "acealdruslvfr18yrincode": "ACEAlDrUsLvFr18YrInCode",
            "acedpmnischsmbfr18yincode": "ACEDpMnIScHsMbFr18YInCode",
            "acehsmmprfr18yrincode": "ACEHsMmPrFr18YrInCode",
            "aceadvchlexpqstttlscore": "ACEAdvChlExpQstTtlScore",
        },
        replace_values={
            "sex": {np.NaN: "Unknown", None: "Unknown"},
            "ACESxlAbsFr18YrInCode": codes,
            "ACEAlDrUsLvFr18YrInCode": codes,
            "ACEFlNgDHPrOfFr18YrInCode": codes,
            "ACEDpMnIScHsMbFr18YInCode": codes,
            "ACEHsMmPrFr18YrInCode": codes,
            "ACEAdPhyAbsInFr18YrInCode": codes,
            "ACEFlLcEmSpOfFr18YrInCode": codes,
            "ACEMtDmVlFr18YrInCode": codes,
            "ACEAdInHmHFrOfF18YrInCode": codes,
            "ACEAdvChlExpQstTtlScore": {np.NaN: -9, None: -9},
            "ACEPrEvSpDvFr18YrInCode": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "ACEAdInHmHFrOfF18YrInCode",
            "ACEAdPhyAbsInFr18YrInCode",
            "ACESxlAbsFr18YrInCode",
            "ACEFlLcEmSpOfFr18YrInCode",
            "ACEFlNgDHPrOfFr18YrInCode",
            "ACEPrEvSpDvFr18YrInCode",
            "ACEMtDmVlFr18YrInCode",
            "ACEAlDrUsLvFr18YrInCode",
            "ACEDpMnIScHsMbFr18YInCode",
            "ACEHsMmPrFr18YrInCode",
            "ACEAdvChlExpQstTtlScore",
        ],
    )
    # Write to delimited file
    Path("tmp/heal_cde").mkdir(exist_ok=True)
    ace.to_csv("tmp/heal_cde/ace.csv")
    return


def extract_koos(data):
    # TODO Do we want to recompute the scale scores here, for replicability?
    codes = {"None": 0, "Mild": 1, "Moderate": 2, "Severe": 3, "Extreme": 4}

    koos = reformat_to_cde(
        data,
        drop_if_all_null=[
            "koospainfreqscl",
            "koospainwalkflatscl",
            "koospainstairsscl",
            "koospainsitlyingscl",
            "koosfuncdiffrisesitscl",
            "koosfuncdiffstandscl",
            "koosfuncdiffcarscl",
            "koosfunctwistpivotscl",
            "koosqolkneeawarescl",
            "koosqollifestylemodscl",
            "koosqolconfidencescl",
            "koosqolkneedifficultyscl",
            "koospainscore",
            "koospainscoret",
            "koosfunctionscore",
            "koosfunctionscoret",
            "koosqolscore",
            "koosqolscoret",
            "koossummaryscore",
        ],
        null_assignments={"instance": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "sp_surgsite": "which_knee",
            "brthdtc": "dob",
            "koospainfreqscl": "KOOSpainFreqScl",
            "koospainwalkflatscl": "KOOSpainWalkFlatScl",
            "koospainstairsscl": "KOOSpainStairsScl",
            "koospainsitlyingscl": "KOOSpainSitLyingScl",
            "koosfuncdiffrisesitscl": "KOOSFuncDiffRiseSitScl",
            "koosfuncdiffstandscl": "KOOSFuncDiffStandScl",
            "koosfuncdiffcarscl": "KOOSFuncDiffCarScl",
            "koosfunctwistpivotscl": "KOOSFunctwistPivotScl",
            "koosqolkneeawarescl": "KOOSQOLKneeAwareScl",
            "koosqollifestylemodscl": "KOOSQOLlifestyleModScl",
            "koosqolconfidencescl": "KOOSQOLConfidenceScl",
            "koosqolkneedifficultyscl": "KOOSQOLkneeDifficultyScl",
            "koospainscore": "KOOSpainScore",
            "koospainscoret": "KOOSpainScoreT",
            "koosfunctionscore": "KOOSfunctionScore",
            "koosfunctionscoret": "KOOSfunctionScoreT",
            "koosqolscore": "KOOSQOLScore",
            "koosqolscoret": "KOOSQOLScoreT",
            "koossummaryscore": "KOOSsummaryScore",
        },
        replace_values={
            "which_knee": {"Left Knee": "left", "Right Knee": "right"},
            "KOOSpainFreqScl": {
                "Never": 0,
                "Monthly": 1,
                "Weekly": 2,
                "Daily": 3,
                "Always": 4,
            },
            "KOOSpainWalkFlatScl": codes,
            "KOOSpainStairsScl": codes,
            "KOOSpainSitLyingScl": codes,
            "KOOSFuncDiffRiseSitScl": codes,
            "KOOSFuncDiffStandScl": codes,
            "KOOSFuncDiffCarScl": codes,
            "KOOSFunctwistPivotScl": codes,
            "KOOSQOLKneeAwareScl": {
                "Never": 0,
                "Monthly": 1,
                "Weekly": 2,
                "Daily": 3,
                "Constantly": 4,
            },
            "KOOSQOLlifestyleModScl": {
                "Not at all": 0,
                "Mildly": 1,
                "Moderately": 2,
                "Severely": 3,
                # TODO Should be 'Totally' according to HEAL CDE and NDA structure
                "Extremely": 4,
            },
            "KOOSQOLConfidenceScl": {
                "Not at all": 0,
                "Mildly": 1,
                "Moderately": 2,
                "Severely": 3,
                "Extremely": 4,
            },
            "KOOSQOLkneeDifficultyScl": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "which_knee",
            "dob",
            "sex",
            "KOOSpainFreqScl",
            "KOOSpainWalkFlatScl",
            "KOOSpainStairsScl",
            "KOOSpainSitLyingScl",
            "KOOSFuncDiffRiseSitScl",
            "KOOSFuncDiffStandScl",
            "KOOSFuncDiffCarScl",
            "KOOSFunctwistPivotScl",
            "KOOSQOLKneeAwareScl",
            "KOOSQOLlifestyleModScl",
            "KOOSQOLConfidenceScl",
            "KOOSQOLkneeDifficultyScl",
            "KOOSpainScore",
            "KOOSpainScoreT",
            "KOOSfunctionScore",
            "KOOSfunctionScoreT",
            "KOOSQOLScore",
            "KOOSQOLScoreT",
            "KOOSsummaryScore",
        ],
    )
    # Write to delimited file
    Path("tmp/heal_cde").mkdir(exist_ok=True)
    koos.to_csv("tmp/heal_cde/koos-12.csv")
    return


def extract_prsupport(data):
    codes = {
        "Never": 1,
        "Rarely": 2,
        "Sometimes": 3,
        "Usually": 4,
        "Always": 5,
    }
    prsupport = reformat_to_cde(
        data,
        drop_if_all_null=[
            "essfsomeonelistenscl",
            "essfsomeoneconfidescl",
            "essffeelappreciatscl",
            "essftalkbaddayscl",
            "essfunderstandprobscl",
            "essftalkfeelingsscl",
            "essf6atotalscore",
        ],
        null_assignments={"instance": None, "ESSF6aTScore": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "essfsomeonelistenscl": "ESSFSomeoneListenScl",
            "essfsomeoneconfidescl": "ESSFSomeoneConfideScl",
            "essffeelappreciatscl": "ESSFFeelAppreciatScl",
            "essftalkbaddayscl": "ESSFTalkBadDayScl",
            "essfunderstandprobscl": "ESSFUnderstandProbScl",
            "essftalkfeelingsscl": "ESSFTalkFeelingsScl",
            "essf6atotalscore": "ESSF6aTotalScore",
        },
        replace_values={
            "ESSFSomeoneListenScl": codes,
            "ESSFSomeoneConfideScl": codes,
            "ESSFFeelAppreciatScl": codes,
            "ESSFTalkBadDayScl": codes,
            "ESSFUnderstandProbScl": codes,
            "ESSFTalkFeelingsScl": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "ESSFSomeoneListenScl",
            "ESSFSomeoneConfideScl",
            "ESSFFeelAppreciatScl",
            "ESSFTalkBadDayScl",
            "ESSFUnderstandProbScl",
            "ESSFTalkFeelingsScl",
            "ESSF6aTotalScore",
            "ESSF6aTScore",
        ],
    )

    # Write to delimited file
    prsupport.to_csv("tmp/heal_cde/prsupport.csv")
    return


def extract_taps1(data):
    t1codes = {
        "Daily or Almost Daily": 0,
        "Less Than Monthly": 3,
        "Monthly": 2,
        "Never": 4,
        "Not Applicable": 9,
        "Weekly": 1,
    }

    taps = reformat_to_cde(
        data,
        drop_if_all_null=[
            "tapstobaccoproductscl",
            "tapstobaccoproductscl_yrs",
            "tapsalcoholusemalescl",
            "tapsalcoholusefemalescl",
            "tapsdrugusescl",
            "tapsprescriptionmedusescl",
        ],
        null_assignments={"instance": None, "TAPSOverallYN": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            # TO DO request NDA add 'tapstobaccoproductscl_yrs'
            "tapstobaccoproductscl": "TAPSTobaccoProductScl",
            "tapsalcoholusemalescl": "TAPSAlcoholUseMaleScl",
            "tapsalcoholusefemalescl": "TAPSAlcoholUseFemaleScl",
            "tapsdrugusescl": "TAPSDrugUseScl",
            # TO DO add caluclation for 'TAPSOverallYN',
            "tapsprescriptionmedusescl": "TAPSPrescriptionMedUseScl",
        },
        replace_values={
            "TAPSAlcoholUseFemaleScl": t1codes,
            "TAPSAlcoholUseMaleScl": t1codes,
            "TAPSDrugUseScl": t1codes,
            "TAPSPrescriptionMedUseScl": t1codes,
            "TAPSTobaccoProductScl": t1codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "TAPSTobaccoProductScl",
            "TAPSAlcoholUseMaleScl",
            "TAPSAlcoholUseFemaleScl",
            "TAPSDrugUseScl",
            "TAPSPrescriptionMedUseScl",
            "TAPSOverallYN",
        ],
    )

    # Write to delimited file
    taps.to_csv("tmp/heal_cde/taps1.csv")
    return


def extract_gad7(data):
    g7codes = {
        "Over half the days": 2,
        "Nearly every day": 3,
        "Not at all": 0,
        "Several days": 1,
        np.NaN: -9,
    }

    gad7 = reformat_to_cde(
        data,
        drop_if_all_null=[
            "gad2feelnervscl",
            "gad2notstopwryscl",
            "gad7wrytoomchscl",
            "gad7troubrelxscl",
            "gad7rstlessscl",
            "gad7easyannoyedscl",
            "gad7feelafrdscl",
            # 'gad7_tot_not_sure',
            # 'gad7_tot_several',
            # 'gad7_tot_over_half',
            # 'gad7_tot_every_day',
            # 'gad7totscore',
            # 'gad7difficulttowork'
        ],
        null_assignments={"instance": None},  # , "GAD7TotScore": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "contact_language": "language",
            "gad2feelnervscl": "GAD2FeelNervScl",
            "gad2notstopwryscl": "GAD2NotStopWryScl",
            "gad7easyannoyedscl": "GAD7EasyAnnoyedScl",
            "gad7feelafrdscl": "GAD7FeelAfrdScl",
            "gad7rstlessscl": "GAD7RstlessScl",
            "gad7troubrelxscl": "GAD7TroubRelxScl",
            "gad7wrytoomchscl": "GAD7WryTooMchScl",
        },
        replace_values={
            "GAD7EasyAnnoyedScl": g7codes,
            "GAD7RstlessScl": g7codes,
            "GAD7TroubRelxScl": g7codes,
            "GAD2NotStopWryScl": g7codes,
            "GAD2FeelNervScl": g7codes,
            "GAD7FeelAfrdScl": g7codes,
            "GAD7WryTooMchScl": g7codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "language",
            "GAD2FeelNervScl",
            "GAD2NotStopWryScl",
            "GAD7WryTooMchScl",
            "GAD7TroubRelxScl",
            "GAD7RstlessScl",
            "GAD7EasyAnnoyedScl",
            "GAD7FeelAfrdScl",  #'GAD7TotScore'
        ],
    )

    # Write to delimited file
    gad7.to_csv("tmp/heal_cde/gad7.csv")
    return


def extract_pcs6(data):
    codes = {
        "All the time": 4,
        "Not at all": 0,
        "To a great degree": 3,
        "To a moderate degree": 2,
        "To a slight degree": 1,
    }

    pcs6 = reformat_to_cde(
        data,
        drop_if_all_null=[
            #'pcs_dt_1',
            "pcqpainawfulovrwhlmscl",
            "pcqfeelcantwithstandscl",
            "pcqafraidpainworsescl",
            "pcqhurtscl",
            "pcqpainstopscl",
            "pcqseriousscl",
            "pcqtotalscoreval",
            #'pain_catastrophizing_questionnaire_pcs6_complete'
        ],
        null_assignments={"instance": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "pcqafraidpainworsescl": "PCQAfraidPainWorseScl",
            "pcqfeelcantwithstandscl": "PCQFeelCantWithstandScl",
            "pcqhurtscl": "PCQHurtScl",
            "pcqpainawfulovrwhlmscl": "PCQPainAwfulOvrwhlmScl",
            "pcqpainstopscl": "PCQPainStopScl",
            "pcqseriousscl": "PCQSeriousScl",
            "pcqtotalscoreval": "PCQTotalScoreVal",
        },
        replace_values={
            "PCQPainAwfulOvrwhlmScl": codes,
            "PCQSeriousScl": codes,
            "PCQPainStopScl": codes,
            "PCQHurtScl": codes,
            "PCQFeelCantWithstandScl": codes,
            "PCQAfraidPainWorseScl": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "PCQPainAwfulOvrwhlmScl",
            "PCQFeelCantWithstandScl",
            "PCQAfraidPainWorseScl",
            "PCQHurtScl",
            "PCQPainStopScl",
            "PCQSeriousScl",
            "PCQTotalScoreVal",
        ],
    )

    # Write to delimited file
    pcs6.to_csv("tmp/heal_cde/pcs6.csv")
    return


def extract_phq9(data):
    codes = {
        "More than<br>half<br>the days<br>2": 2,
        "Nearly<br>every day<br>3": 3,
        "Not<br>at all<br>0": 0,
        "Several<br>days<br>1": 1,
        np.NaN: -9,
        None: -9,
    }

    phq = reformat_to_cde(
        data,
        drop_if_all_null=[
            "phqlitintrstscore",
            "phqdeprssnscore",
            "phqsleepimpairscore",
            "phqtirdlittleenrgyscore",
            "phqabnrmldietscore",
            "phqflngfailrscore",
            "phqconcntrtnimprmntscore",
            "phqmovmntspchimprmntscore",
            #'phq8_score_inst_sc',
            "phqtotalscore",
            #'patient_health_questionnaire_depression_scale_phq_complete'
        ],
        null_assignments={"instance": None, "PHQBttrDdThghtScore": None},
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "contact_language": "language",
            "phqlitintrstscore": "PHQLitIntrstScore",
            "phqdeprssnscore": "PHQDeprssnScore",
            "phqsleepimpairscore": "PHQSleepImpairScore",
            "phqtirdlittleenrgyscore": "PHQTirdLittleEnrgyScore",
            "phqabnrmldietscore": "PHQAbnrmlDietScore",
            "phqflngfailrscore": "PHQFlngFailrScore",
            "phqconcntrtnimprmntscore": "PHQConcntrtnImprmntScore",
            "phqmovmntspchimprmntscore": "PHQMovmntSpchImprmntScore",
            # missing redcap q for 'PHQBttrDdThghtScore'
        },
        replace_values={
            "PHQTirdLittleEnrgyScore": codes,
            "PHQLitIntrstScore": codes,
            "PHQFlngFailrScore": codes,
            "PHQSleepImpairScore": codes,
            "PHQDeprssnScore": codes,
            "PHQBttrDdThghtScore": codes,
            "PHQAbnrmlDietScore": codes,
            "PHQConcntrtnImprmntScore": codes,
            "PHQMovmntSpchImprmntScore": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "language",
            "PHQLitIntrstScore",
            "PHQDeprssnScore",
            "PHQSleepImpairScore",
            "PHQTirdLittleEnrgyScore",
            "PHQAbnrmlDietScore",
            "PHQFlngFailrScore",
            "PHQConcntrtnImprmntScore",
            "PHQMovmntSpchImprmntScore",
            "PHQBttrDdThghtScore",
        ],
    )

    # Write to delimited file
    phq.to_csv("tmp/heal_cde/phq9.csv")
    return


def extract_prsleep(data):
    codes = {
        "A little bit": 2,
        "Not at all": 1,
        "Quite a bit": 4,
        "Somewhat": 3,
        "Very much": 5,
        "Fair": 3,
        "Good": 2,
        "Poor": 4,
        "Very good": 1,
        "Very poor": 5,
        np.NaN: -997,
    }
    prsleep = reformat_to_cde(
        data,
        drop_if_all_null=[
            "promissleepwasrefreshscl",
            "promisproblemwithslpscl",
            "promisdifficltfallaslpscl",
            "promisslpwasrestlessscl",
            "promistryhardgettoslpscl",
            "promissleepqualityscl",
            #'promis_sf_v10_sleep_disturbance_6a_sleep_i_complete'
        ],
        null_assignments={
            "instance": None,
            "PROMISSlpDist6TotalScore": None,
            "PROMISSlpDist6TScore": None,
        },
        rename_columns={
            "pdqassessdate": "date_administered",
            "brthdtc": "dob",
            "promissleepqualityscl": "PROMISSleepQualityScl",
            "promissleepwasrefreshscl": "PROMISSleepWasRefreshScl",
            "promisproblemwithslpscl": "PROMISProblemWithSlpScl",
            "promisdifficltfallaslpscl": "PROMISDifficltFallAslpScl",
            "promisslpwasrestlessscl": "PROMISSlpWasRestlessScl",
            "promistryhardgettoslpscl": "PROMISTryHardGetToSlpScl",
        },
        replace_values={
            "PROMISSleepWasRefreshScl": codes,
            "PROMISSleepQualityScl": codes,
            "PROMISTryHardGetToSlpScl": codes,
            "PROMISDifficltFallAslpScl": codes,
            "PROMISProblemWithSlpScl": codes,
            "PROMISSlpWasRestlessScl": codes,
        },
        output_columns=[
            "date_administered",
            "instance",
            "dob",
            "sex",
            "PROMISSleepQualityScl",
            "PROMISSleepWasRefreshScl",
            "PROMISProblemWithSlpScl",
            "PROMISDifficltFallAslpScl",
            "PROMISSlpWasRestlessScl",
            "PROMISTryHardGetToSlpScl",
            "PROMISSlpDist6TotalScore",
            "PROMISSlpDist6TScore",
        ],
    )

    # Write to delimited file
    prsleep.to_csv("tmp/heal_cde/prsleep.csv")
    return


def main(arg_vals):
    project = REDCapProject("A2CPS_Main_Study_MCC1")
    # project = REDCapProject('A2CPS_Main_Study_MCC2')
    # project = REDCapProject('A2CPS_TKA_MCC2')
    # project = REDCapProject('A2CPS_Thoracic_MCC1')

    # Defines all the forms we pull from the RedCap export,
    # there could potentially be mistmatches between the TKA/Thoracic projects
    # but so far they've matched up or are left out entirely (ex koos-12)
    data = project.data(
        [
            "Postconsent Study Plan Crf V06",
            "Patient Demographics Baseline v0.3 (Demographics I)",
            "Pain Detect Questionnaire (PD-Q)",
            "Knee Injury Osteoarthritis Outcome Score  (KOOS-12)",
            "PROMIS SF v2.0 - Emotional Support 6a",
            "TAPS-1",
            "TAPS-2",
            "Generalized Anxiety Disorder 7 Item (GAD7) Scale Score",
            # needed to get language
            "Consented Participant Information",
            "Pain Catastrophizing Questionnaire (PCS6)",
            "Patient Health Questionnaire Depression Scale (PHQ) Scored",
            "PROMIS SF v1.0 - Sleep Disturbance 6a (Sleep I)",
            "Adverse Childhood Experience Questionnaire (ACE)",
<<<<<<< HEAD
            "TAPS-2",
=======
            "The Big Five Inventory (BFI-2-S)",
            "PROMIS SF v1.0 - Fatigue 7a",
>>>>>>> e7cb447 (add promis-fatigue)
        ]
    )

    # Filter inputs by freeze ids
    record_ids = get_filter_list("ids/DataFreeze_1_022823.csv")
    # baseline only
    events = ["Baseline Visit"]
    data = filter_records_events(data, record_ids, events)
    data.index.names = ["participant_id", "event"]

    # load set offset from env file
    load_dotenv()
    offset = os.getenv("DAY_OFFSET")
    if offset is None:
        print("No DAY_OFFSET variable found in .env")
        exit(1)
    day_offset = int(offset)

    shift = tools.date_offset(
        data.index.get_level_values(0).to_series(name="participant_id"),
        offset_file="tmp/offsets.csv",
        min_days=day_offset,
        max_days=day_offset,
    )
    data = data.dataforge.shift_dates(shift)
    # Dates and ages are a required field, so we drop anyone who is missing those
    # as they will not validate against NDA
    # TODO: find and fix subjects with missing dates
    data.dropna(axis=0, how="any", subset=["pdqassessdate", "brthdtc"], inplace=True)

    # mapping of argument name to function name
    output_methods = {
        "koos": extract_koos,
        "prsupport": extract_prsupport,
        "taps": extract_taps1,
        "gad": extract_gad7,
        "pcs": extract_pcs6,
        "phq": extract_phq9,
        "prsleep": extract_prsleep,
        "ace": extract_ace,
<<<<<<< HEAD
        "taps2": extract_taps2,
=======
        "promis_fatigue": extract_promis_fatigue,
>>>>>>> e7cb447 (add promis-fatigue)
    }

    if arg_vals["extract_heal"] == "all":
        print("outputing all")
        for k, v in output_methods.items():
            v(data)
    else:
        for output in arg_vals["extract_heal"]:
            print("outputing", output)
            output_methods[output](data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "extract_heal",
        nargs="*",
        choices=[
            "all",
            "prsupport",
            "koos",
            "taps",
            "taps2",
            "gad",
            "pcs",
            "phq",
            "prsleep",
            "ace",
            "promis_fatigue",
        ],
        default="all",
        help="List of HEAL structures to extract, defaults to all, \
                     but can pass multiple as well, ex: python generate_uploads/create_nda.py koos prsupport taps",
    )
    args = parser.parse_args()
    main(vars(args))
