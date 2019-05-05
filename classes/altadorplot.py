import requests


class altador:
    def __init__(self, user):
        self.s = requests.session()
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

    def parttwo(self):
        self.user.get('altador/archives.phtml', 'http://thedailyneopets.com/altador-plot/part2/')
        self.user.get('altador/archives.phtml?board=6', 'http://www.neopets.com/altador/archives.phtml')
        data = {'board': '6', 'join_club': '1'}
        self.user.post('altador/archives.phtml', data, 'http://www.neopets.com/altador/archives.phtml?board=6')

    def partthree(self):
        r = self.user.get('altador/tomb.phtml', 'http://thedailyneopets.com/altador-plot/part3/')
        code = r.text.find('href="/altador/tomb.phtml?thv=') + len('href="/altador/tomb.phtml?thv=')
        code1 = r.text.find('"><AREA shape="poly" coords="', code)
        thv = r.text[code:code1]
        self.user.get('altador/tomb.phtml?thv=' + thv, 'http://www.neopets.com/altador/tomb.phtml')
        self.user.get('altador/archives.phtml?archivist=1', 'http://thedailyneopets.com/altador-plot/part3/')
        stardata = self.user.get('altador/astro.phtml?get_star_data=1', 'http://www.thedailyneopets.com/altador-plot/constellation-finder/')
        jellyurl = 'http://www.jellyneo.net/content/plot/?id=constellation_finder'
        jellyref = {'Referer': 'http://www.jellyneo.net/content/plot/?id=constellation_finder'}
        data = {'stardata': stardata.text, 'constellation': 'sleeper'}
        r = requests.post(jellyurl, data=data, headers=jellyref)
        code = r.text.find('<br>The Sleeper:<br>') + len('<br>The Sleeper:<br>')
        code1 = r.text.find('<br>Sum of Coordinates:', code)
        output = r.text[code:code1]
        data_split = output.split('<br>')
        self.user.get('altador/astro.phtml?star_submit='  + \
        data_split[0] + ";" + data_split[1] + "|" + data_split[1] + ";" + data_split[0] + "|" + \
        data_split[1] + ";" + data_split[2] + "|" + data_split[2] + ";" + data_split[1] + "|"+ \
        data_split[3] + ";" + data_split[4] + "|" + data_split[4] + ";" + data_split[3] + "|"+ \
        data_split[4] + ";" + data_split[5] + "|" + data_split[5] + ";" + data_split[4] + 'http://thedailyneopets.com/altador-plot/part3/')

    def partfour(self):
        r = self.user.get('altador/clouds.phtml', 'http://thedailyneopets.com/altador-plot/part4/')
        code = r.text.find('"/altador/clouds.phtml?chv=') + len('"/altador/clouds.phtml?chv=')
        code1 = r.text.find('"><AREA shape="poly" coords="', code)
        chv = r.text[code:code1]
        self.user.get('altador/clouds.phtml?chv=' + chv, 'http://www.neopets.com/altador/clouds.phtml')
        stardata = self.user.get('altador/astro.phtml?get_star_data=1', 'http://www.thedailyneopets.com/altador-plot/constellation-finder/')
        jellyurl = 'http://www.jellyneo.net/content/plot/?id=constellation_finder'
        jellyref = {'Referer': 'http://www.jellyneo.net/content/plot/?id=constellation_finder'}
        data = {'stardata': stardata.text, 'constellation': 'dreamer'}
        r = requests.post(jellyurl, data=data, headers=jellyref)
        code = r.text.find('<br>The Dreamer:<br>') + len('<br>The Dreamer:<br>')
        code1 = r.text.find('</div><p><i style=', code)
        output = r.text[code:code1]
        data_split = output.split('<br>')
        self.user.get('altador/astro.phtml?star_submit=' + \
        data_split[0] + ";" + data_split[1] + "|" + data_split[1] + ";" + data_split[0] + "|" + \
        data_split[1] + ";" + data_split[2] + "|" + data_split[2] + ";" + data_split[1] + "|" + \
        data_split[2] + ";" + data_split[3] + "|" + data_split[3] + ";" + data_split[2] + "|" + \
        data_split[3] + ";" + data_split[4] + "|" + data_split[4] + ";" + data_split[3] + "|" + \
        data_split[5] + 'http://thedailyneopets.com/altador-plot/part3/')

    def partfive(self):
        r = self.user.get('altador/tomb.phtml', 'http://thedailyneopets.com/altador-plot/part5/')
        code = r.text.find('"/altador/tomb.phtml?acvhv=') + len('"/altador/tomb.phtml?acvhv=')
        code1 = r.text.find('"></MAP><DIV align="center"><IMG src="', code)
        output = r.text[code:code1]
        self.user.get('altador/tomb.phtml?acvhv=' + output, 'http://www.neopets.com/altador/tomb.phtml')
        r = self.user.get('altador/hallofheroes.phtml?view_statue_id=11', 'http://thedailyneopets.com/altador-plot/part5/')
        code = r.text.find('"/altador/hallofheroes.phtml?view_statue_id=11&vwhv=') + len('"/altador/hallofheroes.phtml?view_statue_id=11&vwhv=')
        code1 = r.text.find('"></MAP><DIV align="center"><IMG src="', code)
        outputs = r.text[code:code1]
        r = self.user.get('altador/hallofheroes.phtml?view_statue_id=11&vwhv=' + outputs, 'http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11')
        code = r.text.find('&rhv=') + len('&rhv=')
        code1 = r.text.find('"><AREA shape="circle" coords="', code)
        output = r.text[code:code1]
        self.user.get('altador/hallofheroes.phtml?view_statue_id=11&vwhv=' + outputs + '&rhv=' + output, 'http://www.neopets.com/altador/hallofheroes.phtml?view_statue_id=11&vwhv=' + outputs)
        self.user.get('altador/archives.phtml?archivist=1', 'http://thedailyneopets.com/altador-plot/part5/')
        stardata = self.user.get('altador/astro.phtml?get_star_data=1', 'http://www.thedailyneopets.com/altador-plot/constellation-finder/')
        jellyurl = 'http://www.jellyneo.net/content/plot/?id=constellation_finder'
        jellyref = {'Referer': 'http://www.jellyneo.net/content/plot/?id=constellation_finder'}
        data = {'stardata': stardata.text, 'constellation': 'firsttorise'}
        r = requests.post(jellyurl, data=data, headers=jellyref)
        code = r.text.find('<br>The First to Rise:<br>') + len('<br>The First to Rise:<br>')
        code1 = r.text.find('</div><p><i style=', code)
        output = r.text[code:code1]
        data_split = output.split('<br>')
        self.user.get('altador/astro.phtml?star_submit=' + \
        data_split[0] + ";" + data_split[1] + "|" + data_split[1] + ";" + data_split[0] + "|" + \
        data_split[1] + ";" + data_split[2] + "|" + data_split[2] + ";" + data_split[1] + "|" + \
        data_split[5] + ";" + data_split[4] + "|" + data_split[4] + ";" + data_split[5] + "|" + \
        data_split[4] + ";" + data_split[3] + "|" + data_split[3] + ";" + data_split[4], 'http://thedailyneopets.com/altador-plot/part5/')
        self.user.get('altador/hallofheroes.phtml?janitor=1', 'http://thedailyneopets.com/altador-plot/part5/')
        self.user.get('altador/archives.phtml?archivist=1', 'http://thedailyneopets.com/altador-plot/part5/')
        self.user.get('altador/archives.phtml?board=6', 'http://thedailyneopets.com/altador-plot/part5/')
