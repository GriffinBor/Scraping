import os
TICKER_FILE_NAME = 'Ticker_List.txt'
TICKER_FILE_PATH = ''
TICKER_LIST = []

NAME_FILE_NAME = 'Name_List.txt'
NAME_FILE_PATH = ''
NAME_LIST = []


JSON_FILE_OUTPUT_PATH = 'Stock JSON/'

#Ranges = ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]
#Intervals = ["1m", "5m", "10m"] could be more
LONG_DATA_INTERVAL = '1s'
LONG_DATA_RANGE = '1d'

BASE_DATA_INTERVAL = '1m'
BASE_DATA_RANGE = '1d'

if not os.path.isfile(TICKER_FILE_NAME):
    open(TICKER_FILE_PATH + TICKER_FILE_NAME, 'w').close()

if not os.path.isfile(NAME_FILE_PATH):
    open(NAME_FILE_PATH + NAME_FILE_NAME, 'w').close()

if not os.path.exists(JSON_FILE_OUTPUT_PATH):
    os.mkdir(JSON_FILE_OUTPUT_PATH)

with open(TICKER_FILE_PATH + TICKER_FILE_NAME, 'r') as f:
    for line in f:
        if '\n' in line:
            TICKER_LIST.append(line.rstrip('\n'))
        else:
            TICKER_LIST.append(line)
    f.close()

with open(NAME_FILE_PATH + NAME_FILE_NAME, 'r') as f:
    for line in f:
        line = line.replace(' ', '')
        line = line.split(',')
        if '\n' in line[0] or '\n' in line[1]:
            NAME_LIST.append([line[0].rstrip('\n'), line[1].rstrip('\n')])
        else:
            NAME_LIST.append([line[0], line[1]])
    f.close()