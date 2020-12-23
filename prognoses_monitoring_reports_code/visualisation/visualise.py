"""
This module provides the code for visualisations.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import string


def barchart_marketparty_MAE(df_temp, mp=None):
    """ Makes a barchart which compares the marketparties on MAE """

    df_temp = df_temp.sort_values(by='ABS Error (DA)')

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    if mp != None:
        for x in range(len(list_index)):
            if list_index[x] == mp:
                pv_part_index = x

    # In order to mask the market party names generate a dictionary with corresponding letters
    else:
        keys_list = list(df_temp.sort_values(by='ABS Error (DA)').index)
        values_list = list(string.ascii_uppercase[0:len(list_index)])
        zip_iterator = zip(keys_list, values_list)
        a_dictionary = dict(zip_iterator)

        list_index_1 = []
        for i in list_index:
            list_index_1.append(a_dictionary[i])

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp['ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp['ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('MAE per market party')
    plt.ylabel('MAE [MW]')
    plt.xlabel('Market Party')

    if mp != None:
        ax.set_xticks([pv_part_index])
        ax.set_xticklabels([list_index[pv_part_index]])

    else:
        ax.set_xticks(index)
        ax.set_xticklabels(list_index_1)

    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/barchart_marketparty_MAE.png')


def barchart_marketparty_rMAE(df_temp, mp=None):
    df_temp = df_temp.sort_values(by='relative ABS Error (DA)')

    index = np.arange(len(df_temp.index))

    list_index = list(df_temp.index)

    if mp != None:
        for x in range(len(list_index)):
            if list_index[x] == mp:
                pv_part_index = x

    # In order to mask the market party names generate a dictionary with corresponding letters
    else:
        keys_list = list(df_temp.sort_values(by='ABS Error (DA)').index)
        values_list = list(string.ascii_uppercase[0:len(list_index)])
        zip_iterator = zip(keys_list, values_list)
        a_dictionary = dict(zip_iterator)

        list_index_1 = []
        for i in list_index:
            list_index_1.append(a_dictionary[i])

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp['relative ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp['relative ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('rMAE per market party')
    plt.ylabel('rMAE [%]')
    plt.xlabel('Market Party')

    if mp != None:
        ax.set_xticks([pv_part_index])
        ax.set_xticklabels([list_index[pv_part_index]])

    else:
        ax.set_xticks(index)
        ax.set_xticklabels(list_index_1)

    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/barchart_marketparty_rMAE.png')


def barchart_tennet_MAE(df_temp):
    """ Makes a barchart which compares the marketparties on MAE """

    df_temp = df_temp.sort_values(by='ABS Error (DA)')

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp['ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp['ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('MAE per market party')
    plt.ylabel('MAE [MW]')
    plt.xlabel('Market Party')

    ax.set_xticks(index)
    ax.set_xticklabels([x[:6] for x in list_index], rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.savefig('../reports/figures/barchart_marketparty_MAE.png')


def barchart_tennet_rMAE(df_temp):
    """ Makes a barchart which compares the marketparties on MAE """

    df_temp = df_temp.sort_values(by='relative ABS Error (DA)')

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp['relative ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp['relative ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('MAE per market party')
    plt.ylabel('rMAE [%]')
    plt.xlabel('Market Party')

    ax.set_xticks(index)
    ax.set_xticklabels([x[:6] for x in list_index], rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.savefig('../reports/figures/barchart_marketparty_rMAE.png')


def dist_errors(df_month_party):
    fig = plt.figure(figsize=[12.8, 4])

    plt.hist([df_month_party['Error (DA)'].dropna(),
              df_month_party['Error (ID)'].dropna()], bins=20, color=['b', 'g'])

    plt.title('Error distribution')
    plt.ylabel('Frequency')
    plt.xlabel('Error [MW]')
    plt.tight_layout()
    plt.savefig('../reports/figures/dist_errors.png')


def five_conn_MAE(df_temp):

    df_temp_MAE = df_temp.sort_values(by='ABS Error (DA)', ascending=False)
    df_temp_MAE = df_temp_MAE[:5]

    # MAke a bar chart of the five connection points
    index = np.arange(len(df_temp_MAE.index))

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp_MAE['ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp_MAE['ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('Connection points with highest MAE')
    plt.ylabel('MAE [MW]')
    plt.xlabel('Connection point')
    plt.xticks(index + (0.5*bar_width), (df_temp_MAE.index), rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/MAE_five_connectionpoints.png')
    plt.close('all')


def five_conn_rMAE(df_temp):

    df_temp_rMAE = df_temp.sort_values(by='relative ABS Error (DA)', ascending=False)
    df_temp_rMAE = df_temp_rMAE[:5]

    index = np.arange(len(df_temp_rMAE.index))

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, df_temp_rMAE['relative ABS Error (DA)'], bar_width,
                     alpha=opacity,
                     color='b',
                     label='DA')

    rects2 = plt.bar(index + bar_width, df_temp_rMAE['relative ABS Error (ID)'], bar_width,
                     alpha=opacity,
                     color='g',
                     label='ID')

    plt.title('Connection points with highest rMAE')
    plt.ylabel('rMAE [%]')
    plt.xlabel('Connection point')
    plt.xticks(index + (0.5*bar_width), (df_temp_rMAE.index), rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/rMAE_five_connectionpoints.png')
    plt.close('all')


def MAE_marketparty_month(df_month_party):
    df_temp = df_month_party.groupby(['Business day']).mean()
    fig = plt.figure()
    plt.plot(df_temp['ABS Error (DA)'].dropna(), label='DA', marker='o', color='b')
    plt.plot(df_temp['ABS Error (ID)'].dropna(), label='ID', marker='o', color='g')

    ax1 = plt.axes()
    if len(df_temp['ABS Error (DA)'].dropna()) > 5:
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        ax1.xaxis.set_minor_locator(AutoMinorLocator(5))

        ax1.xaxis.grid(which='major', alpha=.2)
        ax1.xaxis.grid(which='minor', alpha=.2)

    plt.xticks(rotation=45)
    plt.title('MAE during month')
    plt.ylabel('MAE [MW]')
    plt.xlabel('Date')
    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/MAE_marketparty_month.png')
    plt.close('all')


def rMAE_marketparty_month(df_month_party):
    df_temp = df_month_party.groupby(['Business day']).mean()
    fig = plt.figure()
    plt.plot(df_temp['relative ABS Error (DA)'].dropna(),
             label='DA', marker='o', color='b')
    plt.plot(df_temp['relative ABS Error (ID)'].dropna(),
             label='ID', marker='o', color='g')

    ax1 = plt.axes()
    if len(df_temp['ABS Error (DA)'].dropna()) > 5:
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        ax1.xaxis.set_minor_locator(AutoMinorLocator(5))

        ax1.xaxis.grid(which='major', alpha=.2)
        ax1.xaxis.grid(which='minor', alpha=.2)

    plt.xticks(rotation=45)
    plt.title('rMAE during month')
    plt.ylabel('rMAE [%]')
    plt.xlabel('Date')
    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/rMAE_marketparty_month.png')
    plt.close('all')


def connectionpoint_plot(df_temp, i):
    df_temp_bd = df_temp.groupby(['Business day']).mean()

    fig = plt.figure(figsize=[12.8, 4.8])

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    total_range = df_temp['Total range [MW]'].max()

    def GFG1(abs_error):
        return (abs_error / total_range) * 100

    def GFG2(ax1):
        y1, y2 = ax1.get_ylim()
        ax_twin .set_ylim(GFG1(y1), GFG1(y2))
        ax_twin .figure.canvas.draw()

    if len(df_temp_bd['ABS Error (DA)'].dropna()) > 5:
        ax_twin = ax1.twinx()
        ax1.callbacks.connect("ylim_changed", GFG2)
        ax_twin.set_ylabel('rMAE [%]')

    ax1.plot(df_temp_bd['ABS Error (DA)'].dropna(), label='DA', marker='o', color='b')
    ax1.plot(df_temp_bd['ABS Error (ID)'].dropna(), label='ID', marker='o', color='g')
    ax1.title.set_text('MAE and rMAE during month')
    ax1.set_ylabel('MAE [MW]')

    if len(df_temp_bd['ABS Error (DA)'].dropna()) > 5:
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        ax1.xaxis.set_minor_locator(AutoMinorLocator(5))

        ax1.xaxis.grid(which='major', alpha=.2)
        ax1.xaxis.grid(which='minor', alpha=.2)

    ax1.tick_params(axis='x', rotation=45)
    ax1.legend()

    ax2.hist([df_temp['Error (DA)'].dropna(), df_temp['Error (ID)'].dropna()],
             label=['DA', 'ID'], bins=20, color=['b', 'g'])
    ax2.title.set_text('Error distribution')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Error [MW]')
    ax2.legend()

    plt.tight_layout()

    plt.savefig('../reports/figures/connectionpoint_'+str(i)+'.png')
    plt.close('all')


def plot_year(df, metric):

    if metric == 'MAE':
        columnname_da = 'ABS Error (DA)'
        columnname_id = 'ABS Error (ID)'

    elif metric == 'rMAE':
        columnname_da = 'relative ABS Error (DA)'
        columnname_id = 'relative ABS Error (ID)'

    # assign only the month to the column 'month'
    df['month'] = df['Business day'].dt.month

    # group the dataframe by month to get the mean of each month
    df_temp = df.groupby(['month']).mean()

    # Use a list of all months which will be used for the ticks on the x-axis
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

    months1 = []
    for i in df_temp.index:
        months1.append(months[i-1])

    # Plot the figure
    fig = plt.figure()
    plt.plot(df_temp[columnname_da].dropna(), label='DA', marker='o', color='b')
    plt.plot(df_temp[columnname_id].dropna(), label='ID', marker='o', color='g')

    ax = plt.axes()
    # ax.xaxis.set_major_locator(MultipleLocator(5))
    # ax.xaxis.set_minor_locator(AutoMinorLocator(5))

    ax.xaxis.grid(which='major', alpha=.2)
    #ax.xaxis.grid(which='minor', alpha=.2)

    plt.xticks(df_temp.index, (months1))
    plt.title(str(metric) + ' during 2020')

    if metric == 'MAE':
        plt.ylabel('MAE [MW]')
    elif metric == 'rMAE':
        plt.ylabel('rMAE [%]')

    plt.xlabel('Month')
    plt.legend()

    plt.tight_layout()
    plt.savefig('../reports/figures/plot_year_' + str(metric) + '.png')
    plt.close('all')