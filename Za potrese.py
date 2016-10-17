import re
import orodja

def zajemi():
    for stran in range(1, 96):
        osnovno = 'http://www.emsc-csem.org/Earthquake/'
        parametri = 'filter=yes&start_date=2016-10-01&end_date=2016-10-15'
        naslov = ('{}?{}&view={}'.format(osnovno, parametri, stran))
        datoteka = 'Potresi/{:02}.html'.format(stran)
        orodja.shrani(naslov, datoteka)

def iskanje():
    regex_potresa = re.compile(
        r'<tr id="(?P<id>(\d{6}))".*?'
        r'>(?P<leto>(\d{4}))-(?P<mesec>(\d{2}))-(?P<dan>(\d{2})).*?'
        r';(?P<ura>(\d{2})):(?P<minuta>(\d{2})):(?P<sekunda>(\d{2}.\d))<',
        #;07:17:26.5</a></b></td><td class="tabev1">38.17&nbsp;</td><td class="tabev2">N&nbsp;&nbsp;</td><td class="tabev1">26.57&nbsp;</td><td class="tabev2">E&nbsp;&nbsp;</td><td class="tabev3">11</td><td class="tabev5" id="magtyp0" >ML</td><td class="tabev2">2.6</td><td id="reg0" class="tb_region" >&#160;NEAR THE COAST OF WESTERN TURKEY</td><td class="comment updatetimeno" id="upd0" style="text-align:right;">2016-10-15 07:28</td></tr>
        flags=re.DOTALL
    )

    for html in orodja.datoteke('Potresi/'):
        for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html)):
            print(potres.group('sekunda'))

iskanje()