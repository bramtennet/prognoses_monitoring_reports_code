import pandas as pd
import numpy as np


def make_dataset(month, data_file_location):
    """This function creates a preprocessed dataset from the raw csv file

       Parameters:
       month(int) :              An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)
       csv_file_location(str):   String which defines the location and name of the csv file

       Returns:
       The function returns a preprocessed dataframe which can be used for further analysis             
    """

    # Open the relevant file with all raw data
    df = pd.read_csv(data_file_location)

    # =============================================================================
    # Selecting the month
    # =============================================================================

    df['Business day'] = pd.to_datetime(df['Business day'], utc=False)

    if month != None:
        df_month = df[df['Business day'].dt.month == month]
    else:
        df_month = df

    # =============================================================================
    # Data preperation
    # =============================================================================

    df_month['Error (DA)'] = (df_month['Prognosis [MW] (DA)']) - \
        (df_month['Realised [MW]'])
    df_month['Error (ID)'] = (df_month['Prognosis [MW] (ID)']) - \
        (df_month['Realised [MW]'])

    # add the absolute error for each observation
    df_month['ABS Error (DA)'] = abs(
        (df_month['Prognosis [MW] (DA)'])-(df_month['Realised [MW]']))
    df_month['ABS Error (ID)'] = abs(
        (df_month['Prognosis [MW] (ID)'])-(df_month['Realised [MW]']))

    # define the monthly minimum and maximum measured for each connection point
    dfc = df_month.groupby('Connection point Name')['Realised [MW]']
    df_month = df_month.assign(min=dfc.transform(min), max=dfc.transform(max))

    # define the total range of the connection point
    df_month['Total range [MW]'] = df_month['max'] - df_month['min']

    df_month['relative ABS Error (DA)'] = (
        df_month['ABS Error (DA)']/(df_month['Total range [MW]']))*100
    df_month['relative ABS Error (ID)'] = (
        df_month['ABS Error (ID)']/(df_month['Total range [MW]']))*100

    df_month['relative ABS Error (DA)'].mask(
        df_month['Total range [MW]'] == 0, np.nan, inplace=True)
    df_month['relative ABS Error (ID)'].mask(
        df_month['Total range [MW]'] == 0, np.nan, inplace=True)

    return(df_month)
