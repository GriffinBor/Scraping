
class Account_Manager:

    def __init__(self, Name, Money):
        try:
            self.Account_Name = Name
            self.Account_Money = Money
            self.Account_Manager_Output = True
            self.output_manager_response('Created Account_Manager for: ' + self.Account_Name + ', Currency amount: $' + self.Account_Money)
        except:
            self.output_manager_response('Failed to create Account_Manager')


    def output_manager_response(self, message):
        if self.Account_Manager_Output:
            print(self.Account_Name + ' Account_Manager: ' + message)


    def write_to_file(self, data):
        try:
            f = open('Manager/' + self.Account_Name + '.manage', 'w')
            f.write(data)
            f.close()
        except:
            self.output_manager_response('Failed to write to file')

    def append_to_file(self, data):
        try:
            f = open('Manager/' + self.Account_Name + '.manage', 'a')
            f.write(data)
            f.close()
        except:
            self.output_manager_response('Failed to append to file')


    def read_from_file(self):
        try:
            f = open('Manager/' + self.Account_Name + '.manage', 'r')
            data = f.read()
            f.close()
            return data
        except:
            self.output_manager_response('Failed to write to file')
