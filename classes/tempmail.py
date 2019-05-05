import requests, time

class tempmail:
    def __init__(self):
        self.s = requests.session()
        self.base = 'https://temp-mail.org/'
        self.s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'})

    def GenMail(self):
        url = self.base
        email = self.s.get(url)
        value = email.text.find('class="emailbox-input opentip" value="') + len('class="emailbox-input opentip" value="')
        value1 = email.text.find('" readonly />', value)
        output = email.text[value:value1]
        return output

    def FindMail(self):
        while True:
            time.sleep(5)
            find_mail = int(round(time.time() * 1000))
            url = self.base + 'en/option/check/?_=' + str(find_mail)
            r = self.s.get(url)
            if '/en/view/' in r.text:
                value = r.text.find('https://temp-mail.org/en/view/') + len('https://temp-mail.org/en/view/')
                value1 = r.text.find('" title="', value)
                mailid = r.text[value:value1]
                break
        url = self.base + 'en/view/' + mailid
        activation = self.s.get(url)
        value = activation.text.find(' rel="external">') + len(' rel="external">')
        value1 = activation.text.find('</a>', value)
        activate = activation.text[value:value1]
        return activate
