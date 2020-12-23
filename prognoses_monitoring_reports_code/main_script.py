"""
Make sure you have installed the package FPDF which can be installed by 'pip install fpdf' (disconnected from TenneT vpn).

Make sure you have installed the slugify package which can be installed via the conda prompt : 'conda install -c conda-forge slugify'

"""


from prognoses_monitoring_reports_code.data.make_dataset import make_dataset
from prognoses_monitoring_reports_code.generate_reports.generate_reports import generate_report_marketparty_month, generate_report_general_month, generate_report_general_year, generate_report_internal_month, generate_report_internal_year



def main(month=8, market_party=None, report_type= 'marketparty_month', data_file_location= '../data/dummy_data.csv'):
    
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
       data_file_location:  Indicates the location of the datafile which is used for making the reports. By default a dummy data file is in place which can be used to run the script (dummy_data.csv).
                            The dummy file can be used as a template to put your own prognosis and measuring data.
       
       Returns:
       The function returns no variables
              
    """

    #### If no month is specified generate the dataset for all months
    if month == None:
        df = make_dataset(month, data_file_location)
    
    #### Preproces the data for the given month
    else:
        df_month = make_dataset(month, data_file_location)
    
    
    ## generate a report based on report type
    if report_type == 'marketparty_month':
        if month in range(1,13):
            generate_report_marketparty_month(df_month, market_party, month)
        else:
            raise Exception("Indicate a month with a number between 1 and 12")
            
    
    ## generate general reports supervising the entire market but which are anonymized
    elif report_type == 'general_month':
        if (month in range(1,13)) & (market_party == None):
            generate_report_general_month(df_month, month)
        else:
            raise Exception("Indicate a month with a number between 1 and 12 and make sure market_party=None")
    
    elif report_type == 'general_year':
        if (month == None) & (market_party == None):
            generate_report_general_year(df)
        else:
            raise Exception("Set month=None and market_party=None as you want to generate a report for the whole year for all market parties")

    ## generate general reports supervising the entire market but which are for internal usage only as they do not disclose market party names
    elif report_type == 'internal_month':
        if  (month in range(1,13)) & (market_party == None):
            generate_report_internal_month(df_month, month)
        else:
            raise Exception("Indicate a month with a number between 1 and 12 and make sure market_party=None")
     
    elif report_type == 'internal_year':
        if (month == None) & (market_party == None):
            generate_report_internal_year(df)
        else:
            raise Exception("Set month=None and market_party=None as you want to generate a report for the whole year for all market parties")
        
        
        
        

    
if __name__ == "__main__":
    main()
    
