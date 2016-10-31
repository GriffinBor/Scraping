import time
import json
import requests


class Ticker_Scraper:
    Time_Range = '1d'
    Time_Interval = '1m'

    def __init__(self, Ticker):
        try:
            self.Ticker_Name = Ticker
            self.Ticker_Scraper_Output = True
            self.output_scraper_response('Created Ticker_Scraper for ticker: ' + Ticker)
            self.get_all_data()
        except:
            self.output_scraper_response('Failed to create Ticker_Scraper')

    def output_scraper_response(self, message):
        if self.Ticker_Scraper_Output:
            print(self.Ticker_Name + ' Ticker_Scraper: ' + message)

    '''
    File operations
        get_data_write_to_csv(parameters to get from yahoo, file path, file name)
            Writes specified data about a ticker to a csv file

        get_data_apped_to_csv(parameters to get from yahoo, file path, file name)
            Appends specified data about a ticker to a csv file

        get_data_multiple_tickers_write_to_csv(list of tickers, parameters to get from yahoo, file path, file name)
            Writes specified data about a list of tickers to a csv file

        get_data_multiple_tickers_append_to_csv(list of tickers,, parameters to get from yahoo, file path, file name)
            Appends specified data about a list of tickers to a csv file

        write_json_to_file(file path, file name)
            Writes specified data about a ticker to a json file

        append_json_to_file(file path, file name)
            Appends specified data about a ticker to a json file
    '''

    def get_data_write_to_csv(self, params, path, name):
        try:
            data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + self.Ticker_Name + "&f=" + params)
            open(path + name + '.csv', 'wb').write(data.content)
        except:
            self.output_scraper_response('Failed to write data to csv file')

    def get_data_append_to_csv(self, params, path, name):
        try:
            data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + self.Ticker_Name + "&f=" + params)
            open(path + name + '.csv', 'ab').write(data.content)
        except:
            self.output_scraper_response('Failed to append data to csv file')

    def get_data_multiple_tickers_write_to_csv(self, ticker_list, params, path, name):
        try:
            ticker_string = ''
            for item in ticker_list:
                ticker_string += item + '+'
            ticker_string = ticker_string[:-1]
            data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker_string + "&f=" + params)
            open(path + name + '.csv', 'wb').write(data.content)
        except:
            self.output_scraper_response('Failed to write data to csv file')

    def get_data_multiple_tickers_append_to_csv(self, ticker_list, params, path, name):
        try:
            ticker_string = ''
            for item in ticker_list:
                ticker_string += item + '+'
            ticker_string = ticker_string[:-1]
            data = requests.get("http://finance.yahoo.com/d/quotes.csv?s=" + ticker_string + "&f=" + params)
            open(path + name + '.csv', 'ab').write(data.content)
        except:
            self.output_scraper_response('Failed to write data to csv file')

    def write_json_to_file(self, path, name):
        try:
            f = open(path + name, 'w')
            f.write(json.dumps(self.Ticker_Data, sort_keys=True, indent=4, separators=(',', ':')))
        except:
            self.output_scraper_response('Failed to write data to csv file')

    def append_json_to_file(self, path, name):
        try:
            f = open(path + name, 'a')
            f.write(json.dumps(self.Ticker_Data, sort_keys=True, indent=4, separators=(',', ':')))
        except:
            self.output_scraper_response('Failed to write data to csv file')

    '''
    End file operations
    '''

    '''
    Getting lengths of data arrays
        get_timestamp_length
            Returns length of the list of timestamps

        get_closing_price_length
            Returns length of the list of closing prices

        get_high_price_length
            Returns length of the list of high prices

        get_low_price_length
            Returns length of the list of low prices

        get_open_price_length
            Returns length of the list of open prices

        get_volume_price_length
            Returns length of the list of volume prices
    '''

    def get_timestamp_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['timestamp'])
        except:
            self.output_scraper_response('Failed to get timestamp')

    def get_closing_price_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['close'])
        except:
            self.output_scraper_response('Failed to get close price')

    def get_high_price_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['high'])
        except:
            self.output_scraper_response('Failed to get high price')

    def get_low_price_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['low'])
        except:
            self.output_scraper_response('Failed to get low price')

    def get_open_price_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['open'])
        except:
            self.output_scraper_response('Failed to get open price')

    def get_volume_price_length(self):
        try:
            return len(self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['volume'])
        except:
            self.output_scraper_response('Failed to get volume')

    '''
    End of lengths
    '''

    '''
    Getting the item in data arrays
        get_closing_price(index of price)
            Returns closing price from specified index

        get_high_price(index of price)
            Returns high price from specified index

        get_low_price(index of price)
            Returns low price from specified index

        get_open_price(index of price)
            Returns open price from specified index

        get_volume_price(index of price)
            Returns volume price from specified index

        get_time_zone()
            Returns gmt offset in epoch time

        get_ticker_symbol()
            Returns ticker symbol

        get_all_data()
            Gets all data from requests json file and stores it in the Ticker_Data
            Runs on init of this class

        get_timestamp(index, convert_to_datetime=True)
            Returns the epoch timestamp
            Can convert to normal date format (True by default)

        get_timestamp_with_offset(index, convert_to_datetime=True)
            Returns the epoch time in the correct time zone
            Can convert to normal date format (True by default)
    '''

    def get_closing_price(self, index):
        try:
            return self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['close'][index]
        except:
            self.output_scraper_response('Failed to get closing price')

    def get_high_price(self, index):

        try:
            return self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['high'][index]
        except:
            self.output_scraper_response('Failed to get high price')

    def get_low_price(self, index):
        try:
            return self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['low'][index]
        except:
            self.output_scraper_response('Failed to get low price')

    def get_open_price(self, index):
        try:
            return self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['open'][index]
        except:
            self.output_scraper_response('Failed to get open price')

    def get_volume_price(self, index):
        try:
            return self.Ticker_Data['chart']['result'][0]['indicators']['quote'][0]['volume'][index]
        except:
            self.output_scraper_response('Failed to get volume price')

    def get_time_zone(self):
        try:
            return self.Ticker_Data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
        except:
            self.output_scraper_response('Failed to get timezone offset')

    def get_ticker_symbol(self):
        try:
            return self.Ticker_Data['chart']['result'][0]['meta']['symbol']
        except:
            self.output_scraper_response('Failed to get symbol')

    def get_all_data(self):
        try:
            data = requests.get(
                "https://query1.finance.yahoo.com/v7/finance/chart/" + self.Ticker_Name + "?range=" + self.Time_Range + "&interval=" + self.Time_Interval + "&indicators=quote&includeTimestamps=true&includePrePost=false&corsDomain=finance.yahoo.com")
            self.Ticker_Data = data.json()
            self.output_scraper_response('Fetched data')
        except:
            self.output_scraper_response('Failed to fetch data')

    def get_timestamp(self, index, convert_to_datetime=True):
        try:
            if convert_to_datetime:
                return time.strftime("%m-%d-%Y %I:%M:%S %p",
                                     time.gmtime(self.Ticker_Data['chart']['result'][0]['timestamp'][index]))
            elif not convert_to_datetime:
                return self.Ticker_Data['chart']['result'][0]['timestamp'][0]
        except:
            self.output_scraper_response('Failed to get timestamp')

    def get_timestamp_with_offset(self, index, convert_to_datetime=True):
        try:
            offset = self.Ticker_Data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
            current = self.Ticker_Data['chart']['result'][0]['timestamp'][index]
            if convert_to_datetime:
                return time.strftime("%m-%d-%Y %I:%M:%S %p", time.gmtime(current + offset))
            elif not convert_to_datetime:
                return current + offset
        except:
            self.output_scraper_response('Failed to get timestamp with offset')

    '''
    End of get data
    '''
