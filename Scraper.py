import time
import json
import requests
import settings


class Ticker_Scraper:
    def __init__(self, Ticker,  get_base_data=True, get_financial_data=False, get_long_data=False):
        try:
            self.Ticker_Name = Ticker
            self.Ticker_Scraper_Output = True
            self.output_scraper_response('Created Ticker_Scraper for ticker: ' + Ticker)
            self.get_base_data = get_base_data
            self.get_financial_data = get_financial_data
            self.get_long_data = get_long_data
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

    def write_json_to_file(self, path, name, data):
        try:
            f = open(path + name, 'w')
            f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))
        except:
            self.output_scraper_response('Failed to write data to csv file')

    def append_json_to_file(self, path, name, data):
        try:
            f = open(path + name, 'a')
            f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))
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

    def get_long_timestamp_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['timestamp'])
        except:
            self.output_scraper_response('Failed to get long timestamp')


    def get_long_closing_price_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['close'])
        except:
            self.output_scraper_response('Failed to get long close price')

    def get_long_high_price_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['high'])
        except:
            self.output_scraper_response('Failed to get long high price')

    def get_long_low_price_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['low'])
        except:
            self.output_scraper_response('Failed to get long low price')

    def get_long_open_price_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['open'])
        except:
            self.output_scraper_response('Failed to get long open price')

    def get_long_volume_price_length(self):
        try:
            return len(self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['volume'])
        except:
            self.output_scraper_response('Failed to get long volume')




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

    def get_revenue_per_share(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['revenuePerShare']['raw']
        except:
            self.output_scraper_response('Failed to get revenue per share')

    def get_revenue_growth(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['revenueGrowth']['raw']
        except:
            self.output_scraper_response('Failed to get revenue growth')

    def get_return_on_equity(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['returnOnEquity']['raw']
        except:
            self.output_scraper_response('Failed to get return on equity')

    def get_return_on_assets(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['returnOnAssets']['raw']
        except:
            self.output_scraper_response('Failed to get return on assests')

    def get_buying_recommendation(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['recommendationKey']
        except:
            self.output_scraper_response('Failed to get recommendation')

    def get_earnings_growth(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['earningsGrowth']['raw']
        except:
            self.output_scraper_response('Failed to get earnings growth')

    def get_debt_to_equity(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['financialData']['debtToEquity']['raw']
        except:
            self.output_scraper_response('Failed to get debt to equity')

    def get_trailing_eps(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['trailingEps']['raw']
        except:
            self.output_scraper_response('Failed to get trailing eps')

    def get_profit_margins(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['profitMargins']['raw']
        except:
            self.output_scraper_response('Failed to get profit margins')

    def get_price_to_book(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['priceToBook']['raw']
        except:
            self.output_scraper_response('Failed to get price to book')

    def get_quarterly_earnings_growth(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['earningsQuarterlyGrowth'][
                'raw']
        except:
            self.output_scraper_response('Failed to get quarterly earnings growth')

    def get_book_value(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['bookValue']['raw']
        except:
            self.output_scraper_response('Failed to get book value')

    def get_beta_number(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['beta']['raw']
        except:
            self.output_scraper_response('Failed to get beta number')

    def get_52week_change(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['52WeekChange']['raw']
        except:
            self.output_scraper_response('Failed to get 52 week change')

    def get_sp_52week_change(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['defaultKeyStatistics']['SandP52WeekChange']['raw']
        except:
            self.output_scraper_response('Failed to get S and P 52 week change')

    def get_earnings_high(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['earningsHigh']['raw']
        except:
            self.output_scraper_response('Failed to get earnings high')

    def get_earnings_low(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['earningsLow']['raw']
        except:
            self.output_scraper_response('Failed to get earnings low')

    def get_earnings_average(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['earningsAverage'][
                'raw']
        except:
            self.output_scraper_response('Failed to get earnings average')

    def get_revenue_high(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['revenueHigh']['raw']
        except:
            self.output_scraper_response('Failed to get revenue high')

    def get_revenue_low(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['revenueLow']['raw']
        except:
            self.output_scraper_response('Failed to get revenue low')

    def get_revenue_average(self):
        try:
            return self.Financial_Data['quoteSummary']['result'][0]['calendarEvents']['earnings']['revenueAverage'][
                'raw']
        except:
            self.output_scraper_response('Failed to get revenue average')

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

    def get_long_closing_price(self, index):
        try:
            return self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['close'][index]
        except:
            self.output_scraper_response('Failed to get long closing price')

    def get_long_high_price(self, index):

        try:
            return self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['high'][index]
        except:
            self.output_scraper_response('Failed to get long high price')

    def get_long_low_price(self, index):
        try:
            return self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['low'][index]
        except:
            self.output_scraper_response('Failed to get long low price')

    def get_long_open_price(self, index):
        try:
            return self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['open'][index]
        except:
            self.output_scraper_response('Failed to get long open price')

    def get_long_volume_price(self, index):
        try:
            return self.Long_Data['chart']['result'][0]['indicators']['quote'][0]['volume'][index]
        except:
            self.output_scraper_response('Failed to get long volume price')

    def get_long_time_zone(self):
        try:
            return self.Long_Data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
        except:
            self.output_scraper_response('Failed to get long timezone offset')

    def get_long_timestamp(self, index, convert_to_datetime=True):
        try:
            if convert_to_datetime:
                return time.strftime("%m-%d-%Y %I:%M:%S %p",
                                     time.gmtime(self.Long_Data['chart']['result'][0]['timestamp'][index]))
            elif not convert_to_datetime:
                return self.Long_Data['chart']['result'][0]['timestamp'][0]
        except:
            self.output_scraper_response('Failed to get long timestamp')

    def get_long_timestamp_with_offset(self, index, convert_to_datetime=True):
        try:
            offset = self.Long_Data['chart']['result'][0]['meta']['tradingPeriods'][0][0]['gmtoffset']
            current = self.Long_Data['chart']['result'][0]['timestamp'][index]
            if convert_to_datetime:
                return time.strftime("%m-%d-%Y %I:%M:%S %p", time.gmtime(current + offset))
            elif not convert_to_datetime:
                return current + offset
        except:
            self.output_scraper_response('Failed to get long timestamp with offset')

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
            if self.get_base_data:
                data = requests.get(
                    "https://query1.finance.yahoo.com/v7/finance/chart/" + self.Ticker_Name + "?range=" + settings.BASE_DATA_RANGE + "&interval=" + settings.BASE_DATA_INTERVAL + "&indicators=quote&includeTimestamps=true&includePrePost=false&corsDomain=finance.yahoo.com")
                self.Ticker_Data = data.json()

            if self.get_financial_data:
                data2 = requests.get(
                    "https://query1.finance.yahoo.com/v10/finance/quoteSummary/" + self.Ticker_Name + "?formatted=true&crumb=RnfZVQrjb%2FI&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com")
                self.Financial_Data = data2.json()

            if self.get_long_data:
                data3 = requests.get(
                    "https://query2.finance.yahoo.com/v8/finance/chart/" + self.Ticker_Name + "?formatted=true&crumb=RnfZVQrjb%2FI&lang=en-US&region=US&interval=" + settings.LONG_DATA_INTERVAL + "events=div%7Csplit&range=" + settings.LONG_DATA_RANGE + "&corsDomain=finance.yahoo.com")
                self.Long_Data = data3.json()

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

    '''
    Compund Functions
    '''

    def get_timestamp_list(self, convert_to_date=True):
        try:
            temp_list = []
            for item in range(self.get_timestamp_length()):
                temp_list.append(self.get_timestamp(item, convert_to_date))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of timestamps')

    def get_low_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_low_price_length()):
                temp_list.append(self.get_low_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of low prices')

    def get_high_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_high_price_length()):
                temp_list.append(self.get_high_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of high prices')

    def get_open_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_open_price_length()):
                temp_list.append(self.get_open_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of open prices')

    def get_closing_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_closing_price_length()):
                temp_list.append(self.get_closing_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of closing prices')

    def get_long_low_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_long_low_price_length()):
                temp_list.append(self.get_long_low_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of long low prices')

    def get_long_high_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_long_high_price_length()):
                temp_list.append(self.get_long_high_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of long high prices')

    def get_long_open_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_long_open_price_length()):
                temp_list.append(self.get_long_open_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of long open prices')

    def get_long_closing_price_list(self):
        try:
            temp_list = []
            for item in range(self.get_long_closing_price_length()):
                temp_list.append(self.get_long_closing_price(item))
            return temp_list
        except:
            self.output_scraper_response('Failed to get list of long closing prices')

    '''
    End of Compound Functions
    '''
