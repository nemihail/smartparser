
from pathlib import Path
import csv
from datetime import date

reports = []

try:
    reportsdir = Path('smartparser/reports')
    for report in reportsdir.iterdir():
        if report.suffix.lower() == '.csv':
            reports.append(report.name)
except FileNotFoundError:
    Path('smartparser/reports').mkdir(parents=True, exist_ok=True)

with open(f'smartparser/reports/{input('Report name: ')}.csv', mode='r', newline='', encoding='utf-8') as file:
    data = [
        ['Name', 'Price', 'Category', 'Date']
    ]
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
    

data.append([input('Book name: '),
             float(input('Book price, £: ')),
             input('Book category aka genre: '),
             date.today()])

with open(f'smartparser/reports/{input('Report name: ')}.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
