TICKER_FILE_NAME = 'Ticker_List.txt'
TICKER_FILE_PATH = ''
TICKER_LIST = []

JSON_FILE_OUTPUT_PATH = 'Stock JSON/'

f = open(TICKER_FILE_PATH + TICKER_FILE_NAME, 'r')
for line in f:
    if '\n' in line:
        TICKER_LIST.append(line.rstrip('\n'))
    else:
        TICKER_LIST.append(line)