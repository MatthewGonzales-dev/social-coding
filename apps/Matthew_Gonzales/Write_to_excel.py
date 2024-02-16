import xlsxwriter

#create an excel file and add a work sheet.
workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()

#widen the first colum
worksheet.set_column('A:A' , 100)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold':True})

#write some simple text
worksheet.write ('A1','Hello?')

#text with formatting.

worksheet.write('A2','World' , bold)
#this above will take the foramting from bold which i defined

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()


#link to module information
#https://pypi.org/project/XlsxWriter/#:~:text=XlsxWriter%20is%20a%20Python%20module,100%25%20compatible%20Excel%20XLSX%20files.
