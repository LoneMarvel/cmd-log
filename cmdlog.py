import subprocess
import os, sys
from datetime import datetime, timedelta

argList = []

def DoRunCommand(argList):        
    del argList[0]        
    try:
        tstVar = subprocess.run(argList, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f'{tstVar.stdout}')
    except FileExistsError as e:
        print(f'And Return Code {e}')
    except FileNotFoundError as e:
        print(f'And Return Code {e}')

#logFileName = 'cmdLogFile'+datetime.now().strftime("%d%m%Y%H%M%S")
#logFile = open(logFileName, 'a+')
#logFile.write('#'*200)

pastDay = datetime(2020, 3, 16, 15, 41, 00, 000000)
dayDiff = datetime.now() - pastDay
print(f'Difference -> {dayDiff}')

for i in range(len(sys.argv)):    
    argList.append(sys.argv[i])

DoRunCommand(argList)