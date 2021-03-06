import re
import orodja

def zajemi():
    for stran in range(1, 96):
        osnovno = 'http://www.emsc-csem.org/Earthquake/'
        parametri = 'filter=yes&start_date=2016-10-01&end_date=2016-10-15'
        naslov = ('{}?{}&view={}'.format(osnovno, parametri, stran))
        datoteka = 'Potresi/{:02}.html'.format(stran)
        orodja.shrani(naslov, datoteka)


def pocisti(potres):
    podatki = potres.groupdict()
    podatki['id'] = int(podatki['id'])
    podatki['leto'] = int(podatki['leto'])
    podatki['mesec'] = int(podatki['mesec'])
    podatki['SIR'] = str(podatki['SIR'])
    podatki['DOL'] = str(podatki['DOL'])
    return podatki

regex_potresa = re.compile(
        r'<tr id="(?P<id>(\d{6}))".*?'
        r'>(?P<leto>(\d{4}))-(?P<mesec>(\d{2}))-(?P<dan>(\d{2})).*?'
        r';(?P<ura>(\d{2})):(?P<minuta>(\d{2})):(?P<sekunda>(\d{2}.\d))<.*?'
        r'>(?P<sirina>(\d{1,2}.\d{2}))&.*?'
        r'">(?P<SIR>([NS]))&.*?'
        r'>(?P<dolzina>(\d{1,3}.\d{2}))&.*?'
        r'">(?P<DOL>([WE]))&.*?'
        r'">(?P<globina>(\d+))<.*?'
        r'">(?P<magnituda>(\d.\d))</.*?'
        r';(?P<regija>(.*?))</.*?'
        , flags=re.DOTALL
        )


def izloci_podatke(imenik):
    potresi = []
    for html_datoteka in orodja.datoteke(imenik):
        for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html_datoteka)):
            potresi.append(pocisti(potres))
    return potresi

potresi = izloci_podatke('Potresi/')
orodja.zapisi_tabelo(potresi, ['id', 'leto', 'mesec', 'dan', 'ura', 'minuta', 'sekunda', 'DOL', 'dolzina', 'SIR', 'sirina', 'globina', 'magnituda', 'regija'], 'potresi_potresi.csv')

# =================== K O N E C   D O K U M E N T A ============================
# =============== samo še neke stvari od prej so spodaj ========================

# regex_potresa = re.compile(
#     r'<tr id="(?P<id>(\d{6}))".*?'
#     r'>(?P<leto>(\d{4}))-(?P<mesec>(\d{2}))-(?P<dan>(\d{2})).*?'
#     r';(?P<ura>(\d{2})):(?P<minuta>(\d{2})):(?P<sekunda>(\d{2}.\d))<.*?'
#     r'>(?P<sirina>(\d{2}.\d{2}))&.*?'
#     r'">(?P<SIR>([NS]))&.*?'
#     r'>(?P<dolzina>(\d{2}.\d{2}))&.*?'
#     r'">(?P<DOL>([WE]))&.*?'
#     r'">(?P<globina>(\d+))<.*?'
#     r'">(?P<magnituda>(\d.\d))</.*?'
#     r';(?P<regija>(.*?))</.*?'
#     # </td><td id="reg0" class="tb_region" >&#160;NEAR THE COAST OF WESTERN TURKEY</td><td class="comment updatetimeno" id="upd0" style="text-align:right;">2016-10-15 07:28</td></tr>
#     , flags=re.DOTALL
# )

# def iskanje():
#     regex_potresa = re.compile(
#         r'<tr id="(?P<id>(\d{6}))".*?'
#         r'>(?P<leto>(\d{4}))-(?P<mesec>(\d{2}))-(?P<dan>(\d{2})).*?'
#         # r';(?P<ura>(\d{2})):(?P<minuta>(\d{2})):(?P<sekunda>(\d{2}.\d))<.*?'
#         # r'>(?P<sirina>(\d{2}.\d{2}))&.*?'
#         # r'">(?P<SIR>([NS]))&.*?'
#         # r'>(?P<dolzina>(\d{2}.\d{2}))&.*?'
#         # r'">(?P<DOL>([WE]))&.*?'
#         # r'">(?P<globina>(\d+))<.*?'
#         # r'">(?P<magnituda>(\d.\d))</.*?'
#         # r';(?P<regija>(.*?))</.*?'
#         # r'">(\d.{4})-(\d.{2})-(?P<lok_dan>(\d.{2})).*?'
#         # r' (?P<lok_ura>(\d{2})):(\d{2})</.*?'
#         #</T;">2016-10-15 07:28</td></tr>
#         , flags=re.DOTALL
#     )
#
#     for html in orodja.datoteke('Potresi/'):
#         for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html)):
#             print(potres.group('id'))