# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:15:46 2020

@author: 104091
"""

from fpdf import FPDF
from slugify import slugify
import calendar

reports_output_folder = '../reports'

def create_pdf(month, mp, list_conn, conn_dict, reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report: " + str(mp), 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_marketparty_month.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_marketparty_month.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_five_connectionpoints.png',
              x=10, y=220, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_five_connectionpoints.png',
              x=105, y=220, w=90, h=0, type='', link='')

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Forecast performance on connection point level ", 0, 2)

    for i in range(len(list_conn)):
        pdf.set_font('arial', 'B', 8)
        pdf.cell(75, 10, str(list_conn[i]) + ' - EAN: ' +
                 str(conn_dict[list_conn[i]]), 0, 2)
        pdf.image(reports_output_folder + '/figures/connectionpoint_'+str(i) +
                  '.png', x=10, y=None, w=180, h=0, type='', link='')
        if (((i+1) % 3 == 0) and (i != range(len(list_conn))[-1])):
            pdf.add_page()

    pdf.output(reports_output_folder + '/prognosis_report_'+str(slugify(mp)) +
               '_2020_'+str('{:02}'.format(month))+'.pdf', 'F')


def create_pdf_general_month(month, reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report of all market parties during " +
             str(calendar.month_name[month]) + ' 2020', 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_marketparty_month.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_marketparty_month.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')

    pdf.output(reports_output_folder + '/general_prognosis_report_' +
               '_2020_'+str('{:02}'.format(month))+'.pdf', 'F')


def create_pdf_general_year(reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report of all market parties during 2020", 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance on market party level", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_MAE.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_rMAE.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')

    pdf.output(reports_output_folder + '/general_prognosis_report_2020.pdf', 'F')


def create_pdf_tennet_month(month, reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report of all market parties during " +
             str(calendar.month_name[month]) + ' 2020', 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_marketparty_month.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_marketparty_month.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')

    pdf.output(reports_output_folder + '/tennet_internal_prognosis_report_2020_' +
               str('{:02}'.format(month))+'.pdf', 'F')


def create_pdf_tennet_year(reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report of all market parties during 2020", 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_MAE.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_rMAE.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')

    pdf.output(reports_output_folder + '/tennet_internal_prognosis_report_2020.pdf', 'F')


def create_pdf_tennet_wind_year(reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report only including wind assets during 2020", 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_MAE.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/plot_year_rMAE.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')

    pdf.output(reports_output_folder + '/tennet_internal_wind_prognosis_report_2020.pdf', 'F')


def create_pdf_tennet_wind_month(month, list_conn, reports_output_folder):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Prognosis monitoring report only including wind assets during " +
             str(calendar.month_name[month]) + ' 2020', 0, 2)
    pdf.cell(30, 10, " ", 0, 2, 'C')
    pdf.set_font('arial', 'B', 12)
    pdf.cell(75, 10, "Forecasting performance over all market parties", 0, 2)

    pdf.image(reports_output_folder + '/figures/barchart_marketparty_MAE.png',
              x=10, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/barchart_marketparty_rMAE.png',
              x=105, y=40, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_marketparty_month.png',
              x=10, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_marketparty_month.png',
              x=105, y=102, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/dist_errors.png',
              x=10, y=160, w=180, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/MAE_five_connectionpoints.png',
              x=10, y=220, w=90, h=0, type='', link='')
    pdf.image(reports_output_folder + '/figures/rMAE_five_connectionpoints.png',
              x=105, y=220, w=90, h=0, type='', link='')

    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 16)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(10)
    pdf.cell(75, 10, "Forecast performance on connection point level ", 0, 2)

    for i in range(len(list_conn)):
        pdf.set_font('arial', 'B', 8)
        pdf.cell(75, 10, str(list_conn[i]), 0, 2)
        pdf.image(reports_output_folder + '/figures/connectionpoint_'+str(i) +
                  '.png', x=10, y=None, w=180, h=0, type='', link='')
        if (((i+1) % 3 == 0) and (i != range(len(list_conn))[-1])):
            pdf.add_page()

    pdf.output(reports_output_folder + '/tennet_internal_wind_prognosis_report_2020_' +
               str('{:02}'.format(month))+'.pdf', 'F')
