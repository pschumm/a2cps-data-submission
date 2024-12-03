import pandas as pd
import csv

def filter_records_events(data: pd.DataFrame,
                  record_ids: list,
                  events: list
                  ) -> pd.DataFrame:
    # filter for record ids in list
    data = data.iloc[data.index.isin(record_ids, level=0)]
    # filter for events in list
    data = data.iloc[data.index.isin(events, level=1)]
    return data


def get_filter_list(filter_csv):
    filter_list = []
    with open(filter_csv, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            filter_list.append(lines[0])
    return filter_list

def reformat_to_cde(data, 
                    drop_if_all_null: list = [],
                    null_assignments: dict = {},
                    rename_columns: dict = {},
                    replace_values: dict = {},
                    output_columns: list = []
                    ):
    """ 
    Filters and reshapes RedCap data object from Dataforge's project.data to 
    match the expected format of the Heal CDE
    drop_if_all null is a list of RedCap field names, any rows with no values 
        for that list will be dropped
    null_assignments is a dictionary with field:None for any fields that should 
        be converted to None, by default some null fields with be more esoteric
        version of null like np.NaN or pd.NaT, converting them to None is more 
        generalizable and will work for int or string values
    rename_columns is a dictionary with RedCap_Field:CDE_Field to handle any 
        discrepancies between the RedCap field names and the names in the CDE
    replace_values is a nested dictionary with the structure
        {CDE_Field1:{'String1':int1,'String2':int2}, CDE_Field2:{'S1':int1...etc}}
        it replaces the string values from RedCap with the integer values we expect
        in the CDE
    output columns is an ordered list of the columns we want in the output CDE
    """
    cde = (data
       .dropna(how='all', subset=drop_if_all_null)
       .assign(**null_assignments)
       .rename(columns=rename_columns)
       .replace(replace_values)
      )[output_columns]
    return cde

