class bank:
    def __init__(self, user):
        self.user = user

    def openaccount(self):
       check = self.user.get('bank.phtml', 'http://www.jellyneo.net/?go=dailies')
       if 'account with us' in check.text:
           print('You don\'t have a bank account yet, creating one for you')
           data = {'type': 'new_account', 'name': 'salesman', 'add1': '123', 'employment': 'Meerca Master', 'salary': '120,001 NP and above', 'account_type': '0', 'initial_deposit': '1'}
           open = self.user.post('process_bank.phtml', data, 'http://www.neopets.com/process_bank.phtml')
           if 'type=opened' in open.url:
               print('Bank account is created')
           if 'Sorry, to open an Bank Account you must have verified' in open.text:
               print('You need to activate your account before you can open an account')

    def interest(self):
        self.user.get('bank.phtml', 'http://www.jellyneo.net/?go=dailies')
        data = {'type': 'interest'}
        check = self.user.post('process_bank.phtml', data, 'http://www.neopets.com/bank.phtml')
        if 'You have already claimed' not in check.text:
            print('Collected bank interest')
        else:
            print('Already collected bank interest today')

    def withdraw(self, amount):
        self.user.get('bank.phtml', 'http://www.jellyneo.net/?go=dailies')
        data = {'type': 'withdraw', 'amount': amount}
        self.user.post('process_bank.phtml', data, 'http://www.neopets.com/bank.phtml')

    def deposit(self, amount):
        self.user.get('bank.phtml', 'http://www.jellyneo.net/?go=dailies')
        data = {'type': 'deposit', 'amount': amount}
        self.user.post('process_bank.phtml', data, 'http://www.neopets.com/bank.phtml')
