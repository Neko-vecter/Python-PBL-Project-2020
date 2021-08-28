# Powered By Neko.vecter
# The excel output for Python Programming class

import xlsxwriter

class excel_exchange():

    def __init__(self) -> None:
        super().__init__()

    # Def of making excel table
    def show_table(self, age, score_avg, times):
        age_p = age
        score_avg_p = score_avg
        times_p = times

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('export.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 8)
        worksheet.set_column('B:B', 18)
        worksheet.set_column('C:C', 18)
    
        # Set chart column
        chart = workbook.add_chart({'type': 'pie'})

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        # Creat 
        worksheet.write('A1', 'Age' , bold)
        worksheet.write('B1', 'Average Score', bold)
        worksheet.write('C1', 'Times Appear' , bold)

        # Write some numbers, with row/column notation.
        worksheet.write_column('A2', age_p)
        worksheet.write_column('B2', score_avg_p)
        worksheet.write_column('C2', times_p)

        datalen = len(age_p)

        len_age_need = str('=Sheet1!$A$2:$A$'+ str(datalen+1))
        len_times_need = str('=Sheet1!$C$2:$C$'+ str(datalen+1))

        chart.add_series({'categories': len_age_need,
                          'values': len_times_need,
                          'name' : 'Times appare'
                          })

        worksheet.insert_chart('E2', chart)

        workbook.close()
        print("finish ex excel")
        pass