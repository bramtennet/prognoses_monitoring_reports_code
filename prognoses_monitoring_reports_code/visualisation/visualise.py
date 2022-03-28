"""
This module provides the code for visualisations.
"""
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import string


reports_output_folder = "../reports"


def barchart_marketparty_MAE(df_temp, reports_output_folder, mp=None):
    """Makes a barchart which compares the marketparties on MAE"""

    df_temp = df_temp.sort_values(by="ABS Error (DA)")

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    if mp != None:
        for x in range(len(list_index)):
            if list_index[x] == mp:
                pv_part_index = x

    # In order to mask the market party names generate a dictionary with corresponding letters
    else:
        keys_list = list(df_temp.sort_values(by="ABS Error (DA)").index)
        values_list = list(string.ascii_uppercase[0 : len(list_index)])
        zip_iterator = zip(keys_list, values_list)
        a_dictionary = dict(zip_iterator)

        list_index_1 = []
        for i in list_index:
            list_index_1.append(a_dictionary[i])

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 3.5])
    bar_width = 0.35
    opacity = 0.8

    if not df_temp["ABS Error (DA)"].isnull().values.all():
        rects1 = plt.bar(
            index,
            df_temp["ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp["ABS Error (ID)"].isnull().values.all():
        rects2 = plt.bar(
            index + bar_width,
            df_temp["ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("MAE per market party")
    plt.ylabel("MAE [MW]")
    plt.xlabel("Market Party")

    if mp != None:
        ax.set_xticks([pv_part_index])
        ax.set_xticklabels([list_index[pv_part_index]])

    else:
        ax.set_xticks(index)
        ax.set_xticklabels(list_index_1)

    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/barchart_marketparty_MAE.png")


def barchart_marketparty_rMAE(df_temp, reports_output_folder, mp=None):
    df_temp = df_temp.sort_values(by="relative ABS Error (DA)")

    index = np.arange(len(df_temp.index))

    list_index = list(df_temp.index)

    if mp != None:
        for x in range(len(list_index)):
            if list_index[x] == mp:
                pv_part_index = x

    # In order to mask the market party names generate a dictionary with corresponding letters
    else:
        keys_list = list(df_temp.sort_values(by="ABS Error (DA)").index)
        values_list = list(string.ascii_uppercase[0 : len(list_index)])
        zip_iterator = zip(keys_list, values_list)
        a_dictionary = dict(zip_iterator)

        list_index_1 = []
        for i in list_index:
            list_index_1.append(a_dictionary[i])

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 3.5])
    bar_width = 0.35
    opacity = 0.8

    if not df_temp["relative ABS Error (DA)"].isnull().values.all():
        rects1 = plt.bar(
            index,
            df_temp["relative ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp["relative ABS Error (ID)"].isnull().values.all():
        rects2 = plt.bar(
            index + bar_width,
            df_temp["relative ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("rMAE per market party")
    plt.ylabel("rMAE [%]")
    plt.xlabel("Market Party")

    if mp != None:
        ax.set_xticks([pv_part_index])
        ax.set_xticklabels([list_index[pv_part_index]])

    else:
        ax.set_xticks(index)
        ax.set_xticklabels(list_index_1)

    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/barchart_marketparty_rMAE.png")


def barchart_tennet_MAE(df_temp, reports_output_folder):
    """Makes a barchart which compares the marketparties on MAE"""

    df_temp = df_temp.sort_values(by="ABS Error (DA)")

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 3.5])
    bar_width = 0.35
    opacity = 0.8

    if not df_temp["ABS Error (DA)"].isnull().values.all():
        rects1 = plt.bar(
            index,
            df_temp["ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp["ABS Error (ID)"].isnull().values.all():
        rects2 = plt.bar(
            index + bar_width,
            df_temp["ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("MAE per market party")
    plt.ylabel("MAE [MW]")
    plt.xlabel("Market Party")

    ax.set_xticks(index)
    ax.set_xticklabels([x[:6] for x in list_index], rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/barchart_marketparty_MAE.png")


def barchart_tennet_rMAE(df_temp, reports_output_folder):
    """Makes a barchart which compares the marketparties on MAE"""

    df_temp = df_temp.sort_values(by="relative ABS Error (DA)")

    index = np.arange(len(df_temp.index))
    list_index = list(df_temp.index)

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 3.5])
    bar_width = 0.35
    opacity = 0.8
    if not df_temp["relative ABS Error (DA)"].isnull().values.all():
        rects1 = plt.bar(
            index,
            df_temp["relative ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp["relative ABS Error (ID)"].isnull().values.all():
        rects2 = plt.bar(
            index + bar_width,
            df_temp["relative ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("MAE per market party")
    plt.ylabel("rMAE [%]")
    plt.xlabel("Market Party")

    ax.set_xticks(index)
    ax.set_xticklabels([x[:6] for x in list_index], rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/barchart_marketparty_rMAE.png")


def completeness_plot_month(df_month, reports_output_folder):

    df_month["Connection point EAN"] = (
        df_month["Market Party Name"].astype(str)
        + "_"
        + df_month["Connection point EAN"].astype(str)
    )
    completeness = pd.DataFrame(
        df_month.groupby(by="Connection point EAN").count()["PTE (15min)"]
    ).rename(columns={"PTE (15min)": "recieved"})
    completeness["expected"] = len(
        pd.date_range(df_month.index.min(), df_month.index.max(), freq="15T")
    )

    x = np.arange(len(completeness.index))  # the label locations
    width = 0.35  # the width of the bars
    opacity = 0.8
    fig, ax = plt.subplots(figsize=[12.8, 6])
    rects1 = ax.bar(
        x - width / 2,
        completeness.recieved.to_list(),
        width,
        alpha=opacity,
        color="b",
        label="recieved",
    )
    rects2 = ax.bar(
        x + width / 2,
        completeness.expected.to_list(),
        width,
        alpha=opacity,
        color="g",
        label="expected",
    )

    # Add some text for labels, title and custom x-axis tick labels, etc.
    plt.title("Completeness per EAN")
    ax.set_ylabel("Number of PTU's")
    ax.set_xticks(x)
    ax.set_xticklabels(completeness.index.to_list())
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()

    autolabel(rects1)
    autolabel(rects2)
    ax.set_xticklabels(completeness.index.to_list(), rotation=40, ha="right")

    fig.tight_layout()
    plt.savefig(reports_output_folder + "/figures/completeness_month.png")


def completeness_time_month(df_month, EAN, mp, reports_output_folder):

    time_combined = (
        df_month[df_month["Connection point EAN"] == EAN]
        .groupby(pd.Grouper(freq="D"))
        .count()[["PTE (15min)"]]
        .rename(columns={"PTE (15min)": "recieved"})
    )
    time_combined["expected"] = 96  # Number of PTU's each day

    x = np.arange(len(time_combined.index))  # the label locations
    width = 0.35  # the width of the bars
    opacity = 0.8
    fig, ax = plt.subplots(figsize=[12.8, 5])
    rects1 = ax.bar(
        x - width / 2,
        time_combined.recieved.to_list(),
        width,
        alpha=opacity,
        color="b",
        label="recieved",
    )
    rects2 = ax.bar(
        x + width / 2,
        time_combined.expected.to_list(),
        width,
        alpha=opacity,
        color="g",
        label="expected",
    )

    # Add some text for labels, title and custom x-axis tick labels, etc.

    ax.set_xticks(x)
    ax.set_xticklabels(time_combined.index.to_list(), rotation=45, ha="right")
    ax.set_xlabel("Time")
    ax.set_ylabel("Numer of PTU's")
    plt.xticks(rotation=45)
    ax.legend()

    fig.tight_layout()
    plt.savefig(
        reports_output_folder
        + "/figures/completeness_time_month_{}_{}.png".format(EAN, mp)
    )


def predicted_realised_time_month(df_month, EAN, mp, reports_output_folder):
    time_combined = df_month[df_month["Connection point EAN"] == EAN][
        ["Realised [MW]", "Prognosis [MW] (DA)", "Prognosis [MW] (ID)"]
    ]

    fig = plt.figure(figsize=[12.8, 5])
    plt.plot(
        time_combined.index, time_combined["Realised [MW]"], color="r", label="Realised"
    )
    if not time_combined["Prognosis [MW] (DA)"].isnull().values.all():
        plt.plot(
            time_combined.index,
            time_combined["Prognosis [MW] (DA)"],
            color="b",
            label="DA Prognosis",
        )
    if not time_combined["Prognosis [MW] (ID)"].isnull().values.all():
        plt.plot(
            time_combined.index,
            time_combined["Prognosis [MW] (ID)"],
            color="g",
            label="ID Prognosis",
        )

    plt.xticks(rotation=45)

    plt.xlabel("Time")
    plt.ylabel("power [MW]")
    plt.legend()
    month = df_month.index.to_pydatetime()[0].month
    year = df_month.index.to_pydatetime()[0].year
    start = datetime(year, month, 1)
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = start.replace(day=28) + timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month
    end = next_month - timedelta(days=next_month.day)
    plt.xlim(start, end)
    fig.tight_layout()
    plt.savefig(
        reports_output_folder
        + "/figures/predicted_realized_time_month_{}_{}.png".format(EAN, mp)
    )


def dist_errors(df_month_party, reports_output_folder):
    fig = plt.figure(figsize=[12.8, 4])

    forecasts_to_plot = []
    color = []
    if not df_month_party["Error (DA)"].isnull().values.all():
        forecasts_to_plot.append(df_month_party["Error (DA)"].dropna())
        color.append("b")

    if not df_month_party["Error (ID)"].isnull().values.all():
        forecasts_to_plot.append(df_month_party["Error (ID)"].dropna())
        color.append("g")

    plt.hist(
        forecasts_to_plot,
        bins=20,
        color=color,
    )

    plt.title("Error distribution")
    plt.ylabel("Frequency")
    plt.xlabel("Error [MW]")
    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/dist_errors.png")


def five_conn_MAE(df_temp, reports_output_folder):

    df_temp_MAE = df_temp.sort_values(by="ABS Error (DA)", ascending=False)
    df_temp_MAE = df_temp_MAE[:5]

    # MAke a bar chart of the five connection points
    index = np.arange(len(df_temp_MAE.index))

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 4.8])
    bar_width = 0.35
    opacity = 0.8
    if not df_temp_MAE["ABS Error (DA)"].isnull().values.all():
        rects1 = plt.bar(
            index,
            df_temp_MAE["ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp_MAE["ABS Error (ID)"].isnull().values.all():
        rects2 = plt.bar(
            index + bar_width,
            df_temp_MAE["ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("Connection points with highest MAE")
    plt.ylabel("MAE [MW]")
    plt.xlabel("Connection point")
    plt.xticks(index + (0.5 * bar_width), (df_temp_MAE.index), rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/MAE_five_connectionpoints.png")
    plt.close("all")


def five_conn_rMAE(df_temp, reports_output_folder):

    df_temp_rMAE = df_temp.sort_values(by="relative ABS Error (DA)", ascending=False)
    df_temp_rMAE = df_temp_rMAE[:5]

    index = np.arange(len(df_temp_rMAE.index))

    # create plot
    fig, ax = plt.subplots(figsize=[6.4, 4.8])
    bar_width = 0.35
    opacity = 0.8

    if not df_temp_rMAE["relative ABS Error (DA)"].isnull().values.all():

        rects1 = plt.bar(
            index,
            df_temp_rMAE["relative ABS Error (DA)"],
            bar_width,
            alpha=opacity,
            color="b",
            label="DA",
        )
    if not df_temp_rMAE["relative ABS Error (ID)"].isnull().values.all():

        rects2 = plt.bar(
            index + bar_width,
            df_temp_rMAE["relative ABS Error (ID)"],
            bar_width,
            alpha=opacity,
            color="g",
            label="ID",
        )

    plt.title("Connection points with highest rMAE")
    plt.ylabel("rMAE [%]")
    plt.xlabel("Connection point")
    plt.xticks(index + (0.5 * bar_width), (df_temp_rMAE.index), rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/rMAE_five_connectionpoints.png")
    plt.close("all")


def MAE_marketparty_month(df_month_party, reports_output_folder):
    df_temp = df_month_party.groupby(df_month_party.index).mean()
    fig = plt.figure(figsize=[6.4, 4.2])
    ax1 = plt.axes()
    if not df_temp["ABS Error (DA)"].isnull().values.all():
        ax1.plot(df_temp["ABS Error (DA)"].dropna(), label="DA", marker=".", color="b")

    if not df_temp["ABS Error (ID)"].isnull().values.all():
        ax1.plot(df_temp["ABS Error (ID)"].dropna(), label="ID", marker=".", color="g")

    if len(df_temp["ABS Error (DA)"].dropna()) > 5:
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        ax1.xaxis.set_minor_locator(AutoMinorLocator(5))

        ax1.xaxis.grid(which="major", alpha=0.2)
        ax1.xaxis.grid(which="minor", alpha=0.2)

    plt.xticks(rotation=45)
    plt.title("MAE during month")
    plt.ylabel("MAE [MW]")
    plt.xlabel("Date")
    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/MAE_marketparty_month.png")
    plt.close("all")


def rMAE_marketparty_month(df_month_party, reports_output_folder):
    df_temp = df_month_party.groupby(df_month_party.index).mean()
    fig = plt.figure(figsize=[6.4, 4.2])
    ax1 = plt.axes()
    if not df_temp["relative ABS Error (DA)"].isnull().values.all():
        ax1.plot(
            df_temp["relative ABS Error (DA)"].dropna(),
            label="DA",
            marker=".",
            color="b",
        )
    if not df_temp["relative ABS Error (ID)"].isnull().values.all():
        ax1.plot(
            df_temp["relative ABS Error (ID)"].dropna(),
            label="ID",
            marker=".",
            color="g",
        )

    if len(df_temp["ABS Error (DA)"].dropna()) > 5:
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        ax1.xaxis.set_minor_locator(AutoMinorLocator(5))

        ax1.xaxis.grid(which="major", alpha=0.2)
        ax1.xaxis.grid(which="minor", alpha=0.2)

    plt.xticks(rotation=45)
    plt.title("rMAE during month")
    plt.ylabel("rMAE [%]")
    plt.xlabel("Date")
    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/rMAE_marketparty_month.png")
    plt.close("all")


def connectionpoint_plot(df_temp, i, reports_output_folder):
    df_temp_bd = df_temp.groupby(df_temp.index).mean()

    fig = plt.figure(figsize=[12.8, 5])

    # ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)

    total_range = df_temp["Total range [MW]"].max()

    # def GFG1(abs_error):
    #     return (abs_error / total_range) * 100

    # def GFG2(ax1):
    #     y1, y2 = ax1.get_ylim()
    #     ax_twin.set_ylim(GFG1(y1), GFG1(y2))
    #     ax_twin.figure.canvas.draw()

    # if len(df_temp_bd["ABS Error (DA)"].dropna()) > 5:
    #     ax_twin = ax1.twinx()
    #     ax1.callbacks.connect("ylim_changed", GFG2)
    #     ax_twin.set_ylabel("rMAE [%]")
    #
    # if df_temp_bd["ABS Error (DA)"].isnull().values.all():
    #     ax1.plot(
    #         df_temp_bd["ABS Error (DA)"].dropna(), label="DA", marker=".", color="b"
    #     )
    # if df_temp_bd["ABS Error (ID)"].isnull().values.all():
    #     ax1.plot(
    #         df_temp_bd["ABS Error (ID)"].dropna(), label="ID", marker=".", color="g"
    #     )
    #
    # ax1.title.set_text("MAE and rMAE during month")
    # ax1.set_ylabel("MAE [MW]")
    #
    # if len(df_temp_bd["ABS Error (DA)"].dropna()) > 5:
    #     ax1.xaxis.set_major_locator(MultipleLocator(5))
    #     ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    #
    #     ax1.xaxis.grid(which="major", alpha=0.2)
    #     ax1.xaxis.grid(which="minor", alpha=0.2)
    #
    # ax1.tick_params(axis="x", rotation=45)
    # ax1.legend()

    forecasts_to_plot = []
    color = []
    if not df_temp["Error (DA)"].isnull().values.all():
        forecasts_to_plot.append(df_temp["Error (DA)"].dropna())
        color.append("b")

    if not df_temp["Error (ID)"].isnull().values.all():
        forecasts_to_plot.append(df_temp["Error (ID)"].dropna())
        color.append("g")

    ax2.hist(
        forecasts_to_plot,
        label=["DA", "ID"],
        bins=20,
        color=color,
    )
    ax2.title.set_text("Error distribution")
    ax2.set_ylabel("Frequency")
    ax2.set_xlabel("Error [MW]")
    ax2.legend()

    plt.tight_layout()

    plt.savefig(reports_output_folder + "/figures/connectionpoint_" + str(i) + ".png")
    plt.close("all")


def plot_year(year, df, metric, reports_output_folder):

    if metric == "MAE":
        columnname_da = "ABS Error (DA)"
        columnname_id = "ABS Error (ID)"

    elif metric == "rMAE":
        columnname_da = "relative ABS Error (DA)"
        columnname_id = "relative ABS Error (ID)"

    # assign only the month to the column 'month'
    df["month"] = df.index.month

    # group the dataframe by month to get the mean of each month
    df_temp = df.groupby(["month"]).mean()

    # Use a list of all months which will be used for the ticks on the x-axis
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    months1 = []
    for i in df_temp.index:
        months1.append(months[i - 1])

    # Plot the figure
    fig = plt.figure()
    if not df_temp[columnname_da].isnull().values.all():
        plt.plot(df_temp[columnname_da].dropna(), label="DA", marker=".", color="b")
    if not df_temp[columnname_id].isnull().values.all():
        plt.plot(df_temp[columnname_id].dropna(), label="ID", marker=".", color="g")

    ax = plt.axes()
    # ax.xaxis.set_major_locator(MultipleLocator(5))
    # ax.xaxis.set_minor_locator(AutoMinorLocator(5))

    ax.xaxis.grid(which="major", alpha=0.2)
    # ax.xaxis.grid(which='minor', alpha=.2)

    plt.xticks(df_temp.index, (months1))
    plt.title(str(metric) + f" during {year}")

    if metric == "MAE":
        plt.ylabel("MAE [MW]")
    elif metric == "rMAE":
        plt.ylabel("rMAE [%]")

    plt.xlabel("Month")
    plt.legend()

    plt.tight_layout()
    plt.savefig(reports_output_folder + "/figures/plot_year_" + str(metric) + ".png")
    plt.close("all")
