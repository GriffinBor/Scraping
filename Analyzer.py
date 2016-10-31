
class Ticker_Analzyer:

    def __init__(self, Ticker):
        try:
            self.Ticker_Name = Ticker
            self.Ticker_Analyzer_Output = True
            self.output_analyzer_response('Created Ticker_Anzlyer for ticker: ' + Ticker)
        except:
            self.output_analyzer_response('Failed to create Ticker_Analzyer')


    def output_analyzer_response(self, message):
        if self.Ticker_Analyzer_Output:
            print(self.Ticker_Name + ' Ticker_Analyer: ' + message)

    def write_to_file(self, data):
        try:
            f = open('Analyzer/' + self.Ticker_Name + '.analyze', 'w')
            f.write(data)
            f.close()
        except:
            self.output_analyzer_response('Failed to write to file')


    def read_from_file(self):
        try:
            f = open('Analyzer/' + self.Ticker_Name + '.analyze', 'r')
            data = f.read()
            f.close()
            return data
        except:
            self.output_analyzer_response('Failed to write to file')

    '''
    Math Functions
    '''

    def get_moving_average(self, data_list, length):
        for data in data_list:
            if data == None:
                data_list.remove(data)
        average = 0
        temp_list = data_list[-length:]
        for item in temp_list:
            average += item
        return average/length


    # def get_moving_average(self, data_list, length):
    #     for data in data_list:
    #         if str(data) == 'None' or str(data) == 'null':
    #             data_list.remove(data)
    #     average = 0
    #     temp_list = data_list[-length:-1]
    #     print(temp_list)
    #     for item in temp_list:
    #         if temp_list.index(item) +1 < len(temp_list):
    #             print(item,'\n')
    #             y1 = item
    #             y2 = temp_list[temp_list.index(item) + 1]
    #             x1 = temp_list.index(item)
    #             x2 = temp_list.index(item) + 1
    #             average += ((y2-y1)/(x2-x1))
    #             # print('Index: ' + str(temp_list.index(item)) + ', ' + str(average))
    #     return average/length


