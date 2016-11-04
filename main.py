import settings
import tkinter
import Scraper
import Analyzer
import Trader
import Manager
import time
import requests
import json
start_time = time.time()

ticker_list = ['AAPL']

manager_accounts = {}
ticker_services = {}

for ticker in ticker_list:
    ticker_services[ticker] = {'Scraper': Scraper.Ticker_Scraper(ticker), 'Analyzer': Analyzer.Ticker_Analzyer(ticker),
                               'Trader': Trader.Ticker_Trader(ticker)}

for ticker in ticker_services:
    cur_scraper = ticker_services[ticker]['Scraper']
    cur_trader = ticker_services[ticker]['Trader']
    cur_analyzer = ticker_services[ticker]['Analyzer']
    print(str(cur_scraper.get_earnings_high()))
    print(str(cur_scraper.get_earnings_low()))
    print(str(cur_scraper.get_earnings_average()))
    print(str(cur_scraper.get_revenue_high()))
    print(str(cur_scraper.get_revenue_low()))
    print(str(cur_scraper.get_revenue_average()))
    print(str(cur_scraper.get_52week_change()))
    print(str(cur_scraper.get_sp_52week_change()))
    print(str(cur_scraper.get_beta_number()))
    print(str(cur_scraper.get_book_value()))
    print(str(cur_scraper.get_quarterly_earnings_growth()))
    print(str(cur_scraper.get_price_to_book()))
    print(str(cur_scraper.get_profit_margins()))
    print(str(cur_scraper.get_trailing_eps()))
    print(str(cur_scraper.get_debt_to_equity()))
    print(str(cur_scraper.get_earnings_growth()))
    print(str(cur_scraper.get_profit_margins()))
    print(str(cur_scraper.get_buying_recommendation()))
    print(str(cur_scraper.get_return_on_assets()))
    print(str(cur_scraper.get_return_on_equity()))
    print(str(cur_scraper.get_revenue_growth()))
    print(str(cur_scraper.get_revenue_per_share()))
    # data_list = []
    # for item in cur_scraper.get_closing_price_list():
    #     print(item)


# pizza = requests.get("https://query1.finance.yahoo.com/v10/finance/quoteSummary/AAPL?formatted=true&crumb=RnfZVQrjb%2FI&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com")
#
# varib = pizza.json()
#
# f = open("newjson.json", 'w')
# f.write(json.dumps(varib, sort_keys=True, indent=4, separators=(',', ':')))

print('\n\n\n')
print("--- %s seconds ---" % (time.time() - start_time))