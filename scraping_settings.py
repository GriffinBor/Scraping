import os
TICKER_FILE_NAME = 'Ticker_List.txt'
TICKER_FILE_PATH = ''
TICKER_LIST = []

NAME_FILE_NAME = 'Name_List.txt'
NAME_FILE_PATH = ''
NAME_LIST = []


JSON_FILE_OUTPUT_PATH = 'Stock JSON/'

if not os.path.isfile(TICKER_FILE_NAME):
    open(TICKER_FILE_PATH + TICKER_FILE_NAME, 'w').close()

if not os.path.isfile(NAME_FILE_PATH):
    open(NAME_FILE_PATH + NAME_FILE_NAME, 'w').close()

if not os.path.isfile(JSON_FILE_OUTPUT_PATH):
    os.mkdir(JSON_FILE_OUTPUT_PATH)

f = open(TICKER_FILE_PATH + TICKER_FILE_NAME, 'r')
for line in f:
    if '\n' in line:
        TICKER_LIST.append(line.rstrip('\n'))
    else:
        TICKER_LIST.append(line)
f.close()

r = open(NAME_FILE_PATH + NAME_FILE_NAME, 'r')
for line in r:
    line = line.replace(' ', '')
    line = line.split(',')
    if '\n' in line[0] or '\n' in line[1]:
        NAME_LIST.append([line[0].rstrip('\n'), line[1].rstrip('\n')])
    else:
        NAME_LIST.append([line[0], line[1]])
r.close()