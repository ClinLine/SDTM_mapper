import jsonata
import json
import openpyxl

# Read JSON file
with open('ReCoPad.json', 'r') as file:
    data=json.load (file)
# expr= jsonata.Jsonata("$count(study.versions.studyDesigns.arms)")
# result=expr.evaluate(data)
# print(result)

wb = openpyxl.load_workbook('Maps/sdtm_mapping_paths.xlsx')

# Start with TS Summary domain
ts_sheet = wb['TS Parameters']

#print(str(ts_sheet['G2'].value))
#code_snip= ts_sheet['G5'].value
#expr= jsonata.Jsonata("$count(study.versions.studyDesigns.arms)")
#result=expr.evaluate(data)
#print(result)


with open('ReCoPad.json', 'r') as file:
    data=json.load (file)
    for row in range(2, 8):
        codeSnip= ts_sheet[f'G{row}'].value
        print(codeSnip)
        expr = jsonata.Jsonata(codeSnip)
        result=expr.evaluate(data)
        print(result)
    