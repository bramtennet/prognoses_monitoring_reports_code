# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:36:32 2020

@author: 104091
"""

from prognoses_monitoring_reports_code.visualisation.visualise import barchart_marketparty_MAE, barchart_marketparty_rMAE, dist_errors, five_conn_MAE, five_conn_rMAE, MAE_marketparty_month, rMAE_marketparty_month, connectionpoint_plot, plot_year, barchart_tennet_MAE, barchart_tennet_rMAE
from prognoses_monitoring_reports_code.pdf.create_pdf import create_pdf, create_pdf_general_month, create_pdf_general_year, create_pdf_tennet_month, create_pdf_tennet_year, create_pdf_tennet_wind_month, create_pdf_tennet_wind_year


def generate_report_marketparty_month(df_month, market_party, month):
    """This function generates a report of an individual market party (if indicated) or reports for all market parties (if market_party = None) for a specific month

       Parameters:

       df_month(df)         Dataframe of the indicated month 
       month(int) :         An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)
       market_party(str):   String which defines the name of the market party you want to create the report for, Indicate None if you want to generate reports for all market parties

       Returns:
       The function returns no variables

    """

    if market_party == None:
        list_market_parties = df_month['Market Party Name'].unique()

    else:
        list_market_parties = [market_party]

    for mp in list_market_parties:
        print('Processing: ' + str(mp))

        # make a temporary dataframe grouped per market party calculating the mean
        # and sort it by ABS error (DA)
        df_temp = df_month.groupby(['Market Party Name']).mean()

        # =============================================================================
        # Plot a Comparison of the MAE and rMAE for all marketparties indicating performance of current mp
        # =============================================================================
        barchart_marketparty_MAE(df_temp, mp)
        barchart_marketparty_rMAE(df_temp, mp)

        # =============================================================================
        # Filter the dataframe for only the selected market party
        # =============================================================================
        df_month_party = df_month[df_month['Market Party Name'] == mp]

        # =============================================================================
        # Plot the distribution of errors
        # =============================================================================
        dist_errors(df_month_party)

        # =============================================================================
        # Plot the MAE and rMAE of the five connection points with the highest MAE and rMAE
        # =============================================================================

        # sort the dataframe by connection point to feed into the plotting functions
        df_temp = df_month_party.groupby(['Connection point Name']).mean()

        five_conn_MAE(df_temp)
        five_conn_rMAE(df_temp)

        # =============================================================================
        # PLOT the MAE and rMAE during the month for both the ID and DA
        # =============================================================================
        MAE_marketparty_month(df_month_party)
        rMAE_marketparty_month(df_month_party)

        # =============================================================================
        # PLOT the MAE and rMAE in one graph during the month for both the ID and DA for each connection point
        # And add the error distribution of this same connection point to the plot
        # =============================================================================
        list_conn = df_month_party['Connection point Name'].unique()

        for i in range(len(list_conn)):
            print('Processing: ' + str(mp) + ' : ' + str(list_conn[i]))

            # filter the dataframe based on the connection point to make a connectionpoint specific plot
            df_temp = df_month_party[df_month_party['Connection point Name']
                                     == list_conn[i]]

            # make a plot for the connection point
            connectionpoint_plot(df_temp, i)

       # =============================================================================
        # Generate the PDF report including all the plots
        # =============================================================================
        conn_dict = dict(
            zip(df_month_party['Connection point Name'], df_month_party['Connection point EAN']))

        create_pdf(month, mp, list_conn, conn_dict)


def generate_report_general_month(df_month, month):
    """This function generates a comparison report for all market parties for a specific month with anonymized names

       Parameters:

       df_month(df)         Dataframe of the indicated month 
       month(int) :         An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)

       Returns:
       The function returns no variables

    """

    # make a temporary dataframe grouped per market party calculating the mean
    # and sort it by ABS error (DA)
    df_temp = df_month.groupby(['Market Party Name']).mean()

    # =============================================================================
    # Plot a Comparison of the MAE and rMAE for all marketparties indicating performance of current mp
    # =============================================================================
    barchart_marketparty_MAE(df_temp)
    barchart_marketparty_rMAE(df_temp)

    # =============================================================================
    # Plot the distribution of errors
    # =============================================================================
    dist_errors(df_month)

    # =============================================================================
    # PLOT the MAE and rMAE during the month for both the ID and DA
    # =============================================================================
    MAE_marketparty_month(df_month)
    rMAE_marketparty_month(df_month)

    # =============================================================================
    # Generate the PDF report including all the plots
    # =============================================================================
    create_pdf_general_month(month)


def generate_report_general_year(df):
    """This function generates a comparison report for all market parties for a specific month with visible names(intended for internal use only)

       Parameters:

       df(df)         Dataframe of the indicated month 

       Returns:
       The function returns no variables

    """

    # make a temporary dataframe grouped per market party calculating the mean
    # and sort it by ABS error (DA)
    df_temp = df.groupby(['Market Party Name']).mean()

    # =============================================================================
    # Plot a Comparison of the MAE and rMAE for all marketparties indicating performance of current mp
    # =============================================================================
    barchart_marketparty_MAE(df_temp)
    barchart_marketparty_rMAE(df_temp)

    # =============================================================================
    # Plot the distribution of errors
    # =============================================================================
    dist_errors(df)

    # =============================================================================
    # PLOT the MAE and rMAE during the month for both the ID and DA
    # =============================================================================
    plot_year(df, 'MAE')
    plot_year(df, 'rMAE')

    # =============================================================================
    # Generate the PDF report including all the plots
    # =============================================================================
    create_pdf_general_year()


def generate_report_internal_month(df_month, month):
    """This function generates a comparison report for all market parties for a specific month with visible names(intended for internal use only)

       Parameters:

       df(df)         Dataframe of the indicated month 
       month(int) :         An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)

       Returns:
       The function returns no variables

    """

    # make a temporary dataframe grouped per market party calculating the mean
    # and sort it by ABS error (DA)
    df_temp = df_month.groupby(['Market Party Name']).mean()

    # =============================================================================
    # Plot a Comparison of the MAE and rMAE for all marketparties indicating performance of current mp
    # =============================================================================
    barchart_tennet_MAE(df_temp)
    barchart_tennet_rMAE(df_temp)

    # =============================================================================
    # Plot the distribution of errors
    # =============================================================================
    dist_errors(df_month)

    # =============================================================================
    # PLOT the MAE and rMAE during the month for both the ID and DA
    # =============================================================================
    MAE_marketparty_month(df_month)
    rMAE_marketparty_month(df_month)

    # =============================================================================
    # Generate the PDF report including all the plots
    # =============================================================================
    create_pdf_tennet_month(month)


def generate_report_internal_year(df):
    """This function generates a comparison report for all market parties for a specific month with visible names(intended for internal use only)

       Parameters:

       df(df)         Dataframe of the indicated month 
       month(int) :         An Integer which represent the month you would like to generate the report for (all months are now in 2020, januari = 1 etc.)

       Returns:
       The function returns no variables

    """

    # make a temporary dataframe grouped per market party calculating the mean
    # and sort it by ABS error (DA)
    df_temp = df.groupby(['Market Party Name']).mean()

    # =============================================================================
    # Plot a Comparison of the MAE and rMAE for all marketparties indicating performance of current mp
    # =============================================================================
    barchart_tennet_MAE(df_temp)
    barchart_tennet_rMAE(df_temp)

    # =============================================================================
    # Plot the distribution of errors
    # =============================================================================
    dist_errors(df)

    # =============================================================================
    # PLOT the MAE and rMAE during the month for both the ID and DA
    # =============================================================================
    plot_year(df, 'MAE')
    plot_year(df, 'rMAE')

    # =============================================================================
    # Generate the PDF report including all the plots
    # =============================================================================
    create_pdf_tennet_year()
