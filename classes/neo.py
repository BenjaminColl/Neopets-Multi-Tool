import requests


class neo:
    def __init__(self, user, pw, pin):
        self.s = requests.session()
        self.base = 'http://www.neopets.com/'
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9'})
        self.user = user
        self.pw = pw
        self.pin = pin


    def get(self, path, ref=''):
        if ref != '':
            self.s.headers.update({'Referer': ref})
        url = self.base + path
        data = self.s.get(url)
        return data

    def post(self, path, data, ref=''):
        if ref != '':
            self.s.headers.update({'Referer': ref})
        url = self.base + path
        pdata = data
        data = self.s.post(url, pdata)
        return data

    def login(self):
        getlogged = self.get('index.phtml')
        logged = self.post('login.phtml', {'destination': '%2Findex.phtml', 'username': self.user, 'password': self.pw}, getlogged.url)
        if 'index' in logged.url:
            print('Logged in as ' + self.user)
        elif 'badpassword' in logged.url:
            print('Invalid password')
        elif 'login' in logged.url:
            print('Account frozen')
        elif 'hi' in logged.url:
            print('Account is birthday locked')
