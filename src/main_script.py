"""
Make sure you have installed the package FPDF which can be installed by 'pip install fpdf' (disconnected from TenneT vpn).

Make sure you have installed the slugify package which can be installed via the conda prompt : 'conda install -c conda-forge slugify'

"""


from data.make_dataset import make_dataset, update_dataset
from generate_reports.generate_reports import generate_report_marketparty_month, generate_report_general_month, generate_report_general_year, generate_report_tennet_month, generate_report_tennet_year, generate_report_tennet_wind_year,generate_report_tennet_wind_month



def main(month=9, market_party=None, update_data=False, report_type= 'marketparty_month'):
    
    """With this main function you are able to generate prognosis monitoring reports for individual or all market parties for a specific month
       
       Parameters:
       month(int) :         An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)
       market_party(str):   String which defines the name of the market party you want to create the report for, Indicate None if you want to generate reports for all market parties
       update_data(bool):   Boolean which defines if the data needs to be updated, if True all excel files will be merged together in one csv file, if False the last update csv file will be used
                            Note that updating from the excel files will take some time 
       report_type:         Indicate the type of report you would like to produce
                            'marketparty_month': generates reports for each market party per month   
                            'general_month': generates a report which overviews all market parties during the indicated month (market party names are anonymized)
                            'general_year': generates a report which overviews all market parties during the entire year (market party names are annonymized)
                            'tennet_month': generates a report which overviews all market parties during the indicated month (market party names are visible), this document is intended for internal purposes
                            'tennet_year': generates a report which overviews all market parties during the entire year (market party names are visible), this document is intended for internal purpose only
                            'tennet_wind_month':generates a report which overviews all wind assets during the indicated month (market party names are visible), this document is intended for internal purposes
                            'tennet_wind_year':generates a report which overviews all wind assets during the entire year (market party names are visible), this document is intended for internal purpose only
       Returns:
       The function returns no variables
              
    """

    #### Update the CSV file from all the individual excel files
    if update_data == True:
        update_dataset()
    
    
    #### If no month is specified generate the dataset for all months
    if month == None:
        df = make_dataset(month)
    
    #### Preproces the data for the given month
    else:
        df_month = make_dataset(month)
    
    
    ## generate a report based on report type
    if report_type == 'marketparty_month':
        generate_report_marketparty_month(df_month, market_party, month)
         
    
    ## generate general reports supervising the entire market but which are anonymized
    elif report_type == 'general_month':
        generate_report_general_month(df_month, month)

    
    elif report_type == 'general_year':
        generate_report_general_year(df)

    ## generate general reports supervising the entire market but which are for TenneT usage only
    elif report_type == 'tennet_month':
        generate_report_tennet_month(df_month, month)

    
    elif report_type == 'tennet_year':
        generate_report_tennet_year(df)
        
    
    elif report_type == 'tennet_wind_month':
        generate_report_tennet_wind_month(df_month,month)
    
    elif report_type == 'tennet_wind_year':
        generate_report_tennet_wind_year(df)
    
   
if __name__ == "__main__":
    main()
    
