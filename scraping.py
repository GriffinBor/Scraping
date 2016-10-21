import requests
import json
import time


# File Operations


def get_data_write_to_csv(ticker, params, path, name):
    data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=" + params)
    open(path + name + '.csv', 'wb').write(data.content)


def get_data_append_to_csv(ticker, params, path, name):
    data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=" + params)
    open(path + name + '.csv', 'ab').write(data.content)


def get_data_multiple_tickers_write_to_csv(ticker_list, params, path, name):
    ticker_string = ''
    for item in ticker_list:
        ticker_string += item + '+'
    ticker_string = ticker_string[:-1]
    data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker_string + "&f=" + params)
    open(path + name + '.csv', 'wb').write(data.content)


def get_data_multiple_tickers_append_to_csv(ticker_list, params, path, name):
    ticker_string = ''
    for item in ticker_list:
        ticker_string += item + '+'
    ticker_string = ticker_string[:-1]
    data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker_string + "&f=" + params)
    open(path + name + '.csv', 'ab').write(data.content)


def write_json_to_file(data, path_and_name):
    f = open(path_and_name, 'w')
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))


def append_json_to_file(data, path_and_name):
    f = open(path_and_name, 'a')
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))


def get_all_data(ticker, time_range, time_interval):
    data = requests.get(
        "https://query1.finance.yahoo.com/v7/finance/chart/" + ticker + "?range=" + time_range + "&interval=" + time_interval + "&indicators=quote&includeTimestamps=true&includePrePost=false&corsDomain=finance.yahoo.com")
    jsondata = data.json()
    return jsondata


def get_custom_data():
    data = requests.get(
        "https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=RnfZVQrjb&symbols=AAPL%2CheadSymbolAsString&corsDomain=finance.yahoo.com")
    jsondata = data.json()
    return jsondata


# File Operations




# Get Operations

def get_regular_open_trading_time(data, convert_to_datetime=True):
    try:
        offset = data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
        current = data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['start']
        if convert_to_datetime:
            return time.strftime("%m-%d-%Y, %I:%M:%S %p",
                                 time.gmtime(current + offset))
        elif not convert_to_datetime:
            return current + offset
    except:
        print('Could not get data')


def get_regular_closing_trading_time(data, convert_to_datetime=True):
    try:
        offset = data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
        current = data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['end']
        if convert_to_datetime:
            return time.strftime("%m-%d-%Y, %I:%M:%S %p",
                                 time.gmtime(current + offset))
        elif not convert_to_datetime:
            return current + offset
    except:
        print('Could not get data')


def get_time_zone(data):
    return data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']


def get_ticker_symbol(data):
    return data['chart']['result'][0]['meta']['symbol']


def get_closing_price(data, index):
    return data['chart']['result'][0]['indicators']['quote'][0]['close'][index]


def get_high_price(data, index):
    return data['chart']['result'][0]['indicators']['quote'][0]['high'][index]


def get_low_price(data, index):
    return data['chart']['result'][0]['indicators']['quote'][0]['low'][index]


def get_open_price(data, index):
    return data['chart']['result'][0]['indicators']['quote'][0]['open'][index]


def get_volume_price(data, index):
    return data['chart']['result'][0]['indicators']['quote'][0]['volume'][index]


def get_timestamp(data, index, convert_to_datetime=True):
    if convert_to_datetime:
        return time.strftime("%m-%d-%Y %I:%M:%S %p", time.gmtime(data['chart']['result'][0]['timestamp'][index]))
    elif not convert_to_datetime:
        return data['chart']['result'][0]['timestamp'][0]


def get_timestamp_with_offset(data, index, convert_to_datetime=True):
    offset = data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
    current = data['chart']['result'][0]['timestamp'][index]
    if convert_to_datetime:
        return time.strftime("%m-%d-%Y %I:%M:%S %p", time.gmtime(current + offset))
    elif not convert_to_datetime:
        return current + offset


# Get Operations



# Get Length Operations


def get_timestamp_length(data):
    return len(data['chart']['result'][0]['timestamp'])


def get_closing_price_length(data):
    return len(data['chart']['result'][0]['indicators']['quote'][0]['close'])


def get_high_price_length(data):
    return len(data['chart']['result'][0]['indicators']['quote'][0]['high'])


def get_low_price_length(data):
    return len(data['chart']['result'][0]['indicators']['quote'][0]['low'])


def get_open_price_length(data):
    return len(data['chart']['result'][0]['indicators']['quote'][0]['open'])


def get_volume_price_length(data):
    return len(data['chart']['result'][0]['indicators']['quote'][0]['volume'])



    # Get Length Operations
