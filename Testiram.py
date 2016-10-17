import requests
import orodja

for stran in range(1, 96):
    osnovno = 'http://www.emsc-csem.org/Earthquake/'
    parametri = 'filter=yes&start_date=2016-10-01&end_date=2016-10-15'
    naslov = ('{}?{}&view={}'.format(osnovno, parametri, stran))
    datoteka = 'Potresi/{:02}.html'.format(stran)
    orodja.shrani(naslov, datoteka)

