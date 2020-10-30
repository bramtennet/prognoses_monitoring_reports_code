import pandas as pd
import numpy as np
import glob


def update_dataset(path = '../data/raw/prognosis_monitoring_data/*2020*', csv_file_location = '../data/interim/all_data1.csv'):
    
    """This function creates the csv file from all seperate daily excel files
       
       Parameters:
       path(str) :               String which defines the path where the excel files are located
       csv_file_location(str):   String which defines the location and name of the excel files

       Returns:
       The function returns no variables
              
    """
    
    df = pd.DataFrame()
    for f in glob.glob(path):
        df1 = pd.read_excel(f)
        df = df.append(df1, ignore_index=True)
        print('Processing: ' +str(f))
    df.to_csv(csv_file_location)
        


def make_dataset(month, csv_file_location = '../data/interim/liander.csv'):
    
    """This function creates a preprocessed dataset from the raw csv file
       
       Parameters:
       month(int) :              An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)
       csv_file_location(str):   String which defines the location and name of the csv file

       Returns:
       The function returns a preprocessed dataframe which can be used for further analysis             
    """
        
    ## Open the relevant file with all raw data
    df = pd.read_csv(csv_file_location)
        
    # =============================================================================
    # Selecting the month
    # =============================================================================
         
    df['Business day'] = pd.to_datetime(df['Business day'], utc=False)
                                  
                           
    if month != None:
        df_month = df[df['Business day'].dt.month == month ]
    else:
        df_month = df
     
    # =============================================================================
    # Insert Fuel Type
    # =============================================================================
    
    # Load excel with asset information
# =============================================================================
#     df_asset = pd.read_excel('../data/raw/asset_data/MRD 2020-07-16_V_2020-08-03.xlsx')
#     df_asset = df_asset[['EANCODE_1', 'Fuel Type']]
#     df_asset.set_index(['EANCODE_1'], inplace = True)
#     
#     dict_asset = df_asset['Fuel Type'].to_dict()
#     df_month['Fuel Type'] = df['Connection point EAN'].apply(lambda x: dict_asset.get(x))
# =============================================================================

    
    # =============================================================================
    # Data preperation
    # =============================================================================
    
    #df_month = df_month.reset_index()
    # add the absolute error for each observation
    df_month['Error (DA)'] =  (df_month['Prognosis [MW] (DA)']) - (df_month['Realised [MW]']) 
    df_month['Error (ID)'] =  (df_month['Prognosis [MW] (ID)']) - (df_month['Realised [MW]'])
    
    # add the absolute error for each observation
    df_month['ABS Error (DA)'] = abs((df_month['Prognosis [MW] (DA)'])-(df_month['Realised [MW]']))
    df_month['ABS Error (ID)'] = abs((df_month['Prognosis [MW] (ID)'])-(df_month['Realised [MW]']))
    
    
    dfc = df.groupby('Connection point Name')['Realised [MW]']
    
    df_month = df_month.assign(min=dfc.transform(min), max=dfc.transform(max))
    
    # define the total range of the connection point
    df_month['Total range [MW]'] = df_month['max'] - df_month['min']
    
    df_month['relative ABS Error (DA)'] = (df_month['ABS Error (DA)']/(df_month['Total range [MW]']))*100
    df_month['relative ABS Error (ID)'] = (df_month['ABS Error (ID)']/(df_month['Total range [MW]']))*100
    
    
    df_month['relative ABS Error (DA)'].mask(df_month['Total range [MW]'] == 0, np.nan, inplace=True)
    df_month['relative ABS Error (ID)'].mask(df_month['Total range [MW]'] == 0, np.nan, inplace=True)
     
    
    return(df_month)
    