# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:15:46 2020

@author: 104091
"""

from fpdf import FPDF
from slugify import slugify
import calendar

reports_output_folder = "../reports"


def create_pdf(
    year,
    month,
    mp,
    list_conn,
    conn_dict,
    reports_output_folder,
    missing_eans_per_pv=None,
    poor_quality_ean_per_pv=None,
):
    pdf = FPDF("P", "mm", "A4")

    if missing_eans_per_pv is not None:
        print(missing_eans_per_pv)
        print(mp)
        try:
            missing_eans_for_pv = missing_eans_per_pv[
                missing_eans_per_pv["PV_NAAM"] == mp
            ].copy(deep=True)
            print(len(missing_eans_for_pv))
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font("arial", "B", 16)
            pdf.cell(90, 10, " ", 0, 2, "C")
            pdf.cell(10)
            pdf.cell(
                75,
                10,
                "EANs for which no forecasts are recieved "
                + str(calendar.month_name[month])
                + f" {year}",
                0,
                2,
            )
            pdf.set_font("arial", "B", 10)

            page_width = pdf.w - 2 * pdf.l_margin
            col_width = page_width / 5

            pdf.ln(1)
            th = pdf.font_size
            pdf.cell(col_width, th, missing_eans_for_pv.columns[0], border=1)
            pdf.cell(col_width, th, missing_eans_for_pv.columns[1], border=1)
            pdf.cell(col_width, th, missing_eans_for_pv.columns[2], border=1)
            pdf.cell(col_width, th, missing_eans_for_pv.columns[3], border=1)
            pdf.cell(col_width, th, missing_eans_for_pv.columns[4], border=1)
            pdf.ln(th)
            pdf.set_font("arial", "", 9)
            for row_index, row in missing_eans_for_pv.iterrows():
                pdf.cell(col_width, th, format(row["EANCODE"]), border=1)
                pdf.cell(1.7 * col_width, th, format(row["PV_NAAM"]), border=1)
                pdf.cell(0.3 * col_width, th, format(row["AANSLUITWAARDE"]), border=1)
                pdf.cell(col_width, th, format(row["WOONPLAATS"]), border=1)
                pdf.cell(col_width, th, format(row["STRAATNAAM"]), border=1)
                pdf.ln(th)
            pdf.ln(1)
        except KeyError:
            print(
                f"Marketparty: {mp} not in list of missing EAN's, skipping table of missing EAN's"
            )

    if poor_quality_ean_per_pv is not None:

        try:

            print(len(poor_quality_ean_per_pv))
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font("arial", "B", 16)
            pdf.cell(90, 10, " ", 0, 2, "C")
            pdf.cell(10)
            pdf.cell(
                75,
                10,
                "EANs for which forecast quality is insufficient "
                + str(calendar.month_name[month])
                + f" {year}",
                0,
                2,
            )
            pdf.set_font("arial", "B", 10)

            page_width = pdf.w - 2 * pdf.l_margin
            col_width = page_width / 5

            pdf.ln(1)
            th = pdf.font_size
            pdf.cell(col_width, th, poor_quality_ean_per_pv.columns[0], border=1)
            pdf.cell(col_width, th, poor_quality_ean_per_pv.columns[1], border=1)
            pdf.cell(col_width, th, poor_quality_ean_per_pv.columns[2], border=1)
            pdf.cell(col_width, th, poor_quality_ean_per_pv.columns[3], border=1)
            pdf.cell(col_width, th, poor_quality_ean_per_pv.columns[4], border=1)
            pdf.ln(th)
            pdf.set_font("arial", "", 9)
            for row_index, row in poor_quality_ean_per_pv.iterrows():
                pdf.cell(col_width, th, format(row["EANCODE"]), border=1)
                pdf.cell(1.7 * col_width, th, format(row["PV_NAAM"]), border=1)
                pdf.cell(0.3 * col_width, th, format(row["AANSLUITWAARDE"]), border=1)
                pdf.cell(col_width, th, format(row["WOONPLAATS"]), border=1)
                pdf.cell(col_width, th, format(row["STRAATNAAM"]), border=1)
                pdf.ln(th)
            pdf.ln(1)
        except KeyError:
            print(
                f"Marketparty: {mp} not in list of missing EAN's, skipping table of missing EAN's"
            )

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report: " + str(mp), 0, 2)
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_marketparty_month.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_marketparty_month.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_five_connectionpoints.png",
        x=10,
        y=220,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_five_connectionpoints.png",
        x=105,
        y=220,
        w=90,
        h=0,
        type="",
        link="",
    )

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(75, 10, "Forecast performance on connection point level ", 0, 2)

    for i in range(len(list_conn)):
        pdf.set_font("arial", "B", 8)
        pdf.cell(
            75, 10, str(list_conn[i]) + " - EAN: " + str(conn_dict[list_conn[i]]), 0, 2
        )
        pdf.image(
            reports_output_folder + "/figures/connectionpoint_" + str(i) + ".png",
            x=10,
            y=None,
            w=180,
            h=0,
            type="",
            link="",
        )
        pdf.image(
            reports_output_folder
            + f"/figures/completeness_time_month_{list_conn[i]}_{mp}.png",
            x=10,
            y=None,
            w=180,
            h=0,
            type="",
            link="",
        )
        pdf.image(
            reports_output_folder
            + f"/figures/predicted_realized_time_month_{list_conn[i]}_{mp}.png",
            x=10,
            y=None,
            w=180,
            h=0,
            type="",
            link="",
        )
        if poor_quality_ean_per_pv is not None:
            reason = poor_quality_ean_per_pv[
                poor_quality_ean_per_pv["EANCODE"] == str(list_conn[i])
            ]["REASON"]
            print(poor_quality_ean_per_pv)

            if len(reason) > 0:
                print("".join(reason))
                # Output justified text
                pdf.set_font("arial", "B", 8)
                pdf.cell(
                    75,
                    10,
                    " Forecast sanity check failed because of the following reason(s): ",
                    0,
                    2,
                )
                pdf.set_font("arial", "", 8)
                pdf.multi_cell(200, 5, "".join(reason))
            else:
                pdf.set_font("arial", "B", 8)
                pdf.cell(75, 10, " Forecast sanity check! ", 0, 2)

        pdf.add_page()

    pdf.output(
        reports_output_folder
        + "/prognosis_report_"
        + str(slugify(mp))
        + f"_{year}_"
        + str("{:02}".format(month))
        + ".pdf",
        "F",
    )


def create_pdf_general_month(year, month, reports_output_folder):
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75,
        10,
        "Prognosis monitoring report of all market parties during "
        + str(calendar.month_name[month])
        + f" {year}",
        0,
        2,
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_marketparty_month.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_marketparty_month.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )

    pdf.output(
        reports_output_folder
        + "/general_prognosis_report_"
        + f"_{year}_"
        + str("{:02}".format(month))
        + ".pdf",
        "F",
    )


def create_pdf_general_year(year, reports_output_folder):
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75, 10, f"Prognosis monitoring report of all market parties during {year}", 0, 2
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_MAE.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_rMAE.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )

    pdf.output(reports_output_folder + f"/general_prognosis_report_{year}.pdf", "F")


def create_pdf_tennet_month(
    year, month, reports_output_folder, missing_eans_per_pv=None
):
    pdf = FPDF("P", "mm", "A4")

    if missing_eans_per_pv is not None:
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font("arial", "B", 16)
        pdf.cell(90, 10, " ", 0, 2, "C")
        pdf.cell(10)
        pdf.cell(
            75,
            10,
            "EANs for which no forecasts are recieved"
            + str(calendar.month_name[month])
            + f" {year}",
            0,
            2,
        )
        pdf.set_font("arial", "B", 10)

        page_width = pdf.w - 2 * pdf.l_margin
        col_width = page_width / 5

        pdf.ln(1)
        th = pdf.font_size
        pdf.cell(col_width, th, missing_eans_per_pv.columns[0], border=1)
        pdf.cell(col_width, th, missing_eans_per_pv.columns[1], border=1)
        pdf.cell(col_width, th, missing_eans_per_pv.columns[2], border=1)
        pdf.cell(col_width, th, missing_eans_per_pv.columns[3], border=1)
        pdf.cell(col_width, th, missing_eans_per_pv.columns[4], border=1)
        pdf.ln(th)
        pdf.set_font("arial", "", 9)
        for row_index, row in missing_eans_per_pv.iterrows():
            pdf.cell(col_width, th, format(row["EANCODE"]), border=1)
            pdf.cell(1.7 * col_width, th, format(row["PV_NAAM"]), border=1)
            pdf.cell(0.3 * col_width, th, format(row["AANSLUITWAARDE"]), border=1)
            pdf.cell(col_width, th, format(row["WOONPLAATS"]), border=1)
            pdf.cell(col_width, th, format(row["STRAATNAAM"]), border=1)
            pdf.ln(th)
        pdf.ln(1)

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75,
        10,
        "Prognosis monitoring report of all market parties during "
        + str(calendar.month_name[month])
        + f" {year}",
        0,
        2,
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_marketparty_month.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_marketparty_month.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/completeness_month.png",
        x=10,
        y=220,
        w=180,
        h=0,
        type="",
        link="",
    )

    pdf.output(
        reports_output_folder
        + f"/tennet_internal_prognosis_report_{year}_"
        + str("{:02}".format(month))
        + ".pdf",
        "F",
    )


def create_pdf_tennet_year(year, reports_output_folder):
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75, 10, f"Prognosis monitoring report of all market parties during {year}", 0, 2
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_MAE.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_rMAE.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )

    pdf.output(
        reports_output_folder + f"/tennet_internal_prognosis_report_{year}.pdf", "F"
    )


def create_pdf_tennet_wind_year(year, reports_output_folder):
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75,
        10,
        "Prognosis monitoring report only including wind assets during 2020",
        0,
        2,
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_MAE.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/plot_year_rMAE.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )

    pdf.output(
        reports_output_folder + f"/tennet_internal_wind_prognosis_report_{year}.pdf",
        "F",
    )


def create_pdf_tennet_wind_month(year, month, list_conn, reports_output_folder):
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(
        75,
        10,
        "Prognosis monitoring report only including wind assets during "
        + str(calendar.month_name[month])
        + f" {year}",
        0,
        2,
    )
    pdf.cell(30, 10, " ", 0, 2, "C")
    pdf.set_font("arial", "B", 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_MAE.png",
        x=10,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/barchart_marketparty_rMAE.png",
        x=105,
        y=40,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_marketparty_month.png",
        x=10,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_marketparty_month.png",
        x=105,
        y=102,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/dist_errors.png",
        x=10,
        y=160,
        w=180,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/MAE_five_connectionpoints.png",
        x=10,
        y=220,
        w=90,
        h=0,
        type="",
        link="",
    )
    pdf.image(
        reports_output_folder + "/figures/rMAE_five_connectionpoints.png",
        x=105,
        y=220,
        w=90,
        h=0,
        type="",
        link="",
    )

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font("arial", "B", 16)
    pdf.cell(90, 10, " ", 0, 2, "C")
    pdf.cell(10)
    pdf.cell(75, 10, "Forecast performance on connection point level ", 0, 2)

    for i in range(len(list_conn)):
        pdf.set_font("arial", "B", 8)
        pdf.cell(75, 10, str(list_conn[i]), 0, 2)
        pdf.image(
            reports_output_folder + "/figures/connectionpoint_" + str(i) + ".png",
            x=10,
            y=None,
            w=180,
            h=0,
            type="",
            link="",
        )
        if ((i + 1) % 3 == 0) and (i != range(len(list_conn))[-1]):
            pdf.add_page()

    pdf.output(
        reports_output_folder
        + f"/tennet_internal_wind_prognosis_report_{year}_"
        + str("{:02}".format(month))
        + ".pdf",
        "F",
    )
