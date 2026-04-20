
import pandas as pdd
from pathlib import Path
import json

try:
    reportsdir = Path('reports')
    for report in reportsdir.iterdir():
        if report.suffix.lower() == '.csv':
            print(report.name)
except FileNotFoundError:
    Path('smartparser/reports').mkdir(parents=True, exist_ok=True)
