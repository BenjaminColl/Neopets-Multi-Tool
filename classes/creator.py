import requests, string, random, sys, time

class creator:
    def __init__(self):
        self.s = requests.session()
        self.base = 'http://www.neopets.com/'
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9'})

    def Username(self, stringLength):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def Password(self, stringLength):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    def referer(self, path):
        self.s.headers.update({'Referer': path})

    def autocreate(self):
        passwords = self.Password(15)
        url = self.base + 'index.phtml'
        self.s.get(url)
        url = self.base + 'login/index.phtml'
        self.referer(self.base + 'index.phtml')
        self.s.get(url)
        url = self.base + 'signup/index.phtml'
        self.referer(self.base + 'login/index.phtml')
        self.s.get(url)
        username = self.Username(15)
        url = self.base + 'signup/ajax.phtml'
        self.referer(self.base + 'signup/index.phtml')
        self.s.headers.update({'X-Requested-With': 'XMLHttpRequest', 'Origin': 'http://www.neopets.com'})
        data = {'method': 'step1', 'username': username, 'password1': passwords + '11', 'password2': passwords + '11', 'terms': 'true', 'destination': ''}
        self.s.post(url, data=data)
        url = self.base + 'signup/index.phtml?cookieCheck=1'
        self.referer(self.base + 'signup/index.phtml')
        r = self.s.get(url)
        if '(Step 2 of 4)' not in r.text:
            print('something fucked up, quitting in 5 seconds.')
            time.sleep(5)
            sys.exit()
        countries = ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'GB1', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CK', 'CR', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'TP', 'EC', 'EG', 'SV', 'GB2', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'FX', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GB3', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GN', 'GW', 'GY', 'HT', 'HM', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'GB4', 'IL', 'IT', 'JM', 'JP', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'GB5', 'MP', 'NO', 'OM', 'PK', 'PW', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'GS', 'KN', 'LS', 'VC', 'SM', 'ST', 'SA', 'GB6', 'SN', 'SC', 'SL', 'SG', 'SK', 'SI', 'SB', 'SO', 'ZA', 'ES', 'LK', 'SH', 'PM', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH',' SY', 'TW', 'TJ', 'TZ', 'TH', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UM', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN', 'VG', 'VI', 'WK', 'GB7', 'WF', 'EH', 'WS', 'YE', 'ZR', 'ZM', 'ZW']
        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'WA', 'WV', 'WI', 'WY']
        gender = ['M', 'F', 'O']
        country = random.choice(countries)
        selectedstate = random.choice(states)
        if country != 'US':
            selectedstate = ''
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 25))
        year = random.choice(range(1920, 2000))
        url = self.base + 'signup/ajax.phtml'
        self.referer(self.base + 'signup/index.phtml?cookieCheck=1')
        data = {'method': 'step2', 'gender': random.choice(gender), 'month': month, 'day': day, 'year': year, 'country': random.choice(countries), 'usState': selectedstate}
        self.s.post(url, data=data)
        url = self.base + 'signup/index.phtml?cookieCheck=1'
        self.referer(self.base + 'signup/ajax.phtml')
        r = self.s.get(url)
        if '(Step 3 of 4)' not in r.text:
            print('something fucked up, quitting in 5 seconds.')
            time.sleep(5)
            sys.exit()
        email = self.Username(10)
        url = self.base + 'signup/ajax.phtml'
        self.referer(self.base + 'signup/index.phtml?cookieCheck=1')
        data = {'method': 'step3', 'email1': email + '@gmail.com', 'email2': email + '@gmail.com', 'optinNeopets': 'false', 'optinEmail': ''}
        self.s.post(url, data=data)
        url = self.base + 'reg/page4.phtml'
        self.referer(self.base + 'signup/index.phtml?cookieCheck=1')
        r = self.s.get(url)
        if 'Create a Neopet' not in r.text:
            print('something fucked up, quitting in 5 seconds.')
            time.sleep(5)
            sys.exit()
        pet_gender = ['male', 'female']
        pet_colours = ['red', 'yellow', 'green', 'blue']
        pets = ['korbat', 'chia', 'acara', 'yurble', 'aisha', 'jubjub', 'gnorbu', 'shoyru', 'wocky', 'lenny', 'ixi', 'zafara', 'mynci', 'tuskaninny', 'nimmo', 'skeith', 'gerlert', 'grarrl', 'flotsam', 'quiggle', 'elephante', 'kougra', 'eyerie', 'ogrin', 'xweetok', 'vandagyre', 'kyrii', 'kacheek', 'peophin', 'usul', 'buzz', 'meerca', 'blumaroo', 'moehog', 'kau', 'bruce', 'techo', 'scorchio', 'bori', 'uni', 'pteri', 'lupe']
        url = self.base + 'reg/process_page6.phtml'
        self.referer(self.base + 'reg/page4.phtml')
        data = {'neopet_name': self.Username(15), 'selected_pet': random.choice(pets), 'selected_pet_colour': random.choice(pet_colours), 'gender': random.choice(pet_gender), 'terrain': random.choice(range(1, 8)), 'likes': random.choice(range(1, 6)), 'meetothers': random.choice(range(1, 8)), 'pet_stats_set': random.choice(range(1, 3))}
        r = self.s.post(url, data=data)
        if 'pet_success2' not in r.text:
            print('something fucked up, quitting in 5 seconds.')
            time.sleep(5)
            sys.exit()
        print('Account details:\nUsername: ' + username + '\nPassword: ' + passwords +'11\nDOB (D/M/Y): ' + str(day) + '/' + str(month) + '/' + str(year))
        input('\nPress enter to exit')

if __name__ == '__main__':
    a = creator()
    a.autocreate()
