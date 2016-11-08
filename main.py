import settings
import Scraper
import time
import os
import Connections
import Trader
import Analyzer
import psycopg2
start_time = time.time()

def write_basic_data(scraper):
    scraper.write_json_to_file(settings.JSON_FILE_OUTPUT_PATH + scraper.Ticker_Name + '/', str(scraper.get_date_with_offset(0)) +'.json', scraper.Ticker_Data)

def write_financial_data(scraper):
    scraper.write_financial_data(settings.DATA_FILE_OUTPUT_PATH + scraper.Ticker_Name + '/', str(scraper.get_date_with_offset(0)) + '_financial_data.txt')

def write_long_data(scraper):
    scraper.append_long_data_to_file(settings.DATA_FILE_OUTPUT_PATH + scraper.Ticker_Name + '/', str(scraper.get_date_with_offset(0)) + '_long_data.txt')
ticker_list = ['AAPL', 'TWTR', 'NFLX']

manager_accounts = {}
ticker_services = {}

for ticker in settings.TICKER_LIST:
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker,True, False, True), 'Analyzer': Analyzer.Ticker_Analzyer(ticker),
                               'Trader': Trader.Ticker_Trader(ticker)}
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker,True, True, True)}
for ticker in ticker_services:
    cur_scraper = ticker_services[ticker]['Scraper']
    if not os.path.exists(settings.JSON_FILE_OUTPUT_PATH + cur_scraper.Ticker_Name + '/'):
        os.mkdir(settings.JSON_FILE_OUTPUT_PATH + cur_scraper.Ticker_Name + '/')

    if not os.path.exists(settings.DATA_FILE_OUTPUT_PATH + cur_scraper.Ticker_Name + '/'):
        os.mkdir(settings.DATA_FILE_OUTPUT_PATH + cur_scraper.Ticker_Name + '/')

    write_basic_data(cur_scraper)
    write_financial_data(cur_scraper)
    write_long_data(cur_scraper)
    # cur_trader = ticker_services[ticker]['Trader']
    # cur_analyzer = ticker_services[ticker]['Analyzer']

    Connections.post_timestamp_data('data', cur_scraper)
print('\n\n\n')
print("--- %s seconds ---" % (time.time() - start_time))