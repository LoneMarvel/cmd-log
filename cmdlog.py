import subprocess
import os
from datetime import datetime, timedelta

def DoRunCommand():
    try:
        tstVar = subprocess.run(['ls','-l', '/home/tinos'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f'And the result -> {tstVar.stdout}')
    except FileExistsError as e:
        print(f'And Return Code {e}')
    except FileNotFoundError as e:
        print(f'And Return Code {e}')

logFileName = 'cmdLogFile'+datetime.now().strftime("%d%m%Y%H%M%S")
logFile = open(logFileName, 'a+')
logFile.write('#'*200)

pastDay = datetime(2020, 3, 16)
dayDiff = datetime.now() - pastDay
print(f'Difference -> {dayDiff}')