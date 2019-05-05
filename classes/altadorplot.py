class altador:
    def __init__(self, user):
        self.user = user

    def partone(self):
        print('Starting the altadot plot completer')
        statues = ['12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        num = 0
        self.user.get('altador/hallofheroes.phtml', 'http://thedailyneopets.com/altador-plot/part1/')
        self.user.get('altador/hallofheroes.phtml?janitor=1', 'http://www.neopets.com/altador/hallofheroes.phtml')
        self.user.get('altador/hallofheroes.phtml?janitor=1&push_button=1', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
        self.user.post('altador/hallofheroes.phtml?janitor=1&push_button=1&acpcont=1', '', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')
        self.user.get('altador/archives.phtml', 'http://thedailyneopets.com/altador-plot/part1/')
        self.user.get('altador/archives.phtml?archivist=1', 'http://www.neopets.com/altador/archives.phtml')
        self.user.get('altador/archives.phtml?archivist=1&get_book=1', 'http://www.neopets.com/altador/archives.phtml?archivist=1')
        self.user.post('altador/archives.phtml?archivist=1&get_book=1&acpcont=1', '', 'http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')
        self.user.get('altador/quarry.phtml', 'http://thedailyneopets.com/altador-plot/part1/')
        self.user.get('altador/quarry.phtml?get_rock=1', 'http://www.neopets.com/altador/quarry.phtml')
        self.user.post('altador/quarry.phtml?get_rock=1&acpcont=1', '', 'http://www.neopets.com/altador/quarry.phtml?get_rock=1')
        self.user.get('altador/archives.phtml', 'http://thedailyneopets.com/altador-plot/part1/')
        self.user.get('altador/archives.phtml?archivist=1', 'http://www.neopets.com/altador/archives.phtml')
        self.user.get('altador/archives.phtml?archivist=1&get_book=1', 'http://www.neopets.com/altador/archives.phtml?archivist=1')
        self.user.post('altador/archives.phtml?archivist=1&get_book=1&acpcont=1', '', 'http://www.neopets.com/altador/archives.phtml?archivist=1&get_book=1')
        self.user.get('altador/hallofheroes.phtml?', 'http://thedailyneopets.com/altador-plot/part1/')
        self.user.get('altador/hallofheroes.phtml?janitor=1', 'http://www.neopets.com/altador/hallofheroes.phtml?')
        self.user.get('altador/hallofheroes.phtml?janitor=1&push_button=1', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
        self.user.post('altador/hallofheroes.phtml?janitor=1&push_button=1&acpcont=1', '', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')
        self.user.get('altador/hallofheroes.phtml?', 'http://thedailyneopets.com/altador-plot/part1/')
        print('Looking for the oil, this could take a few minutes')
        while True:
            if num == 12:
                num = 0
            r = self.user.get('altador/hallofheroes.phtml?view_statue_id=' + statues[num], 'http://www.neopets.com/altador/hallofheroes.phtml?')
            num += 1
            if 'you notice a jar of oil' in r.text:
                code = r.text.find('hallofheroes.phtml?soh=') + len('hallofheroes.phtml?soh=')
                code1 = r.text.find('&view_statue_id=', code)
                soh = r.text[code:code1]
                break
        self.user.post('altador/hallofheroes.phtml?soh=' + soh + '&view_statue_id=' + statues[num], '', 'http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=' + statues[num])
        self.user.get('altador/hallofheroes.phtml?janitor=1', 'http://www.neopets.com/altador/hallofheroes.phtml?')
        self.user.get('altador/hallofheroes.phtml?janitor=1&push_button=1', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1')
        self.user.post('altador/hallofheroes.phtml?janitor=1&push_button=1&acpcont=1', '', 'http://www.neopets.com/altador/hallofheroes.phtml?janitor=1&push_button=1')
        print('Finished part one.')
