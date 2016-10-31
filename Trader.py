
class Ticker_Trader:

    def __init__(self, Ticker):
        try:
            self.Ticker_Name = Ticker
            self.Ticker_Trader_Output = True
            self.output_trader_response('Created Ticker_Trader for ticker: ' + Ticker)
        except:
            self.output_trader_response('Failed to create Ticker_Trader')


    def output_trader_response(self, message):
        if self.Ticker_Trader_Output:
            print(self.Ticker_Name + ' Ticker_Trader: ' + message)

    def write_to_file(self, data):
        try:
            f = open('Trader/' + self.Ticker_Name + '.trade', 'w')
            f.write(data)
            f.close()
        except:
            self.output_trader_response('Failed to write to file')


    def read_from_file(self):
        try:
            f = open('Trader/' + self.Ticker_Name + '.trade', 'r')
            data = f.read()
            f.close()
            return data
        except:
            self.output_trader_response('Failed to write to file')