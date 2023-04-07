import time, re
import pickle, signal
from config import *
import random
from pathlib import Path
import traceback
import requests
import colorama
from colorama import *
init(autoreset=True)
ab = "\033[90m"
rd = "\033[91m"
ij = "\033[92m"
kn = "\033[93m"
rs = "\033[0;0m"
sp = f"{ab}|{rs}"
kuning = "\033[93m"
ij = "\033[92m"
res = Style.RESET_ALL
putih = Style.NORMAL + Fore.WHITE
putih2 = Style.BRIGHT + Fore.WHITE
hitam = Style.BRIGHT + Fore.BLACK
hitam2 = Style.BRIGHT + Fore.BLACK
ungu = Style.NORMAL + Fore.MAGENTA
hijau = Style.NORMAL + Fore.GREEN
hijau2 = Style.BRIGHT + Fore.GREEN
merah = Style.NORMAL + Fore.RED
merah2 = Style.BRIGHT + Fore.RED
biru = Style.NORMAL + Fore.BLUE
biru2 = Style.BRIGHT + Fore.BLUE
biru3 = Style.BRIGHT + Fore.LIGHTCYAN_EX
profcolor = Style.BRIGHT + Back.GREEN + Fore.WHITE
losecolor = Style.BRIGHT + Back.RED + Fore.WHITE
rccolor = Style.BRIGHT + Back.WHITE + Fore.BLACK
rcfontcolor = Style.NORMAL + Fore.BLACK
kuning = Style.NORMAL + Fore.YELLOW
kuning2 = Style.BRIGHT + Fore.YELLOW
cyan = Style.NORMAL + Fore.CYAN
cyan2 = Style.BRIGHT + Fore.LIGHTCYAN_EX
merah = Fore.LIGHTRED_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
babi = [putih, cyan, biru, magenta]
war = random.choice(babi)
colorama.init()
try:
    import cloudscraper
    init(autoreset=True)
    kuning = "\033[93m"
    ab = "\033[90m"
    rd = "\033[91m"
    ij = "\033[92m"
    kn = "\033[93m"
    rs = "\033[0;0m"
    sp = f"{ab}|{rs}"
except ModuleNotFoundError:
    import pip
    install = ['install', 'cloudscraper']
    pip.main(install)
    del pip, install
    import cloudscraper

try:
    #import requests as rq
    import ext_httpx as httpx
except ModuleNotFoundError:
    import pip
    install = ['install', 'requests']
    pip.main(install)
    del pip, install
    import ext_requests as rq

import os, sys
from time import sleep
import json
from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
from anticaptchaofficial.hcaptchaproxyless import *
from multiprocessing import Process
from random import choice
import ujson
import ext_httpx as httpx
sys.dont_write_bytecode = True
_dumps = lambda obj, **kwargs: ujson.dumps(obj, escape_forward_slashes=False, **kwargs)

try:
    from python_anticaptcha import AnticaptchaClient, HCaptchaTaskProxyless, AnticatpchaException
except ModuleNotFoundError:
    import pip
    install = ['install', 'python-anticaptcha']
    pip.main(install)
    del pip, install
    from python_anticaptcha import AnticaptchaClient, HCaptchaTaskProxyless, AnticatpchaException

try:
    from twocaptcha.solver import TimeoutException, ApiException
    from twocaptcha import TwoCaptcha
except ModuleNotFoundError:
    import pip

    install = ['install', '2captcha-python==1.1.1']
    pip.main(install)
    del pip, install
    from twocaptcha import TwoCaptcha
    from twocaptcha.solver import TimeoutException, ApiException

class NotEnougt(Exception):
    pass

class CaptchaInvalid(Exception):
    pass

class Kesalahan(Exception):
    pass
class _printex:
    def __init__(self, msg, err_code: int = 0):
        print(msg)
        sys.exit(err_code)


class BLBaseException(Exception):
    """bancetzLaut base exceptions."""


class BLFormatter(BLBaseException):
    """Beautify exceptions."""

    def __init__(self, err):
        if type(err).__name__ == "KeyboardInterrupt":
            _printex(
                f"\r\x1b[1C\x1b[1K\r\n\n{rd}#Iqbalmeduk_:{rs} {kn}Bot terminated! (ctrl + c).{rs}\n"
            )
        else:
            _errMsg = err
            _errType = type(err).__name__

            _wantedFrame = {}
            _unwantedFrame = []

            _stack = traceback.extract_tb(_errMsg.__traceback__)
            for _ in _stack:
                if "bin" in _.filename:
                    _.filename = Path(_.filename).stem
                elif Path(_.filename).parent.is_relative_to(Path.cwd()):
                    _.filename = Path(_.filename).stem
                if _.name != "<module>" and "python" not in _.filename:
                    if _.filename not in _wantedFrame:
                        _wantedFrame.update({_.filename: _})
                    else:
                        _wantedFrame[_.filename] = _
                else:
                    _unwantedFrame.append(_)
            _stack = [_ for _ in _stack if _ not in _unwantedFrame]
            _stack = "Traceback (recent call):\n" + "".join(
                [
                    ("%s\n" % _.split("\n")[0])
                    for _ in traceback.format_list(
                        _unwantedFrame[:1]
                        if not _wantedFrame
                        else [v for k, v in _wantedFrame.items()]
                    )
                ]
            )
            _errStack = _stack

            _printex(
                f"\n\n{kn}{_errStack}{rs}" f"\n{rd}{_errType}:{rs} {kn}{_errMsg}{rs}\n"
            )
            
class Anti_captcha:
    name = 'anti-captcha'
    def __init__(self, key):
        self.client =  AnticaptchaClient(key)

    def solve(self, captcha_key, url):
        """
            """
        solver = hCaptchaProxyless()
        #solver.set_verbose(1)
        solver.set_key("f5139f6c01918fdee549647ef7f36317")
        solver.set_website_url('https://stake.kim/')
        solver.set_website_key('7830874c-13ad-4cfe-98d7-e8b019dc1742')
        solver.set_soft_id(0)
        ret = solver.solve_and_return_solution()
        if ret != 0:
            print("already solver")
            return ret
        else:
            exit(f"\n{solver.err_string}")

    def get_ball(self):
        return self.client.getBalance()

    def report(self, hasil):
        if hasil == 0:
            self.job.report_incorrect_recaptcha()

class capt2:
    name =  '2captcha'
    def __init__(self, api_key):
        self.ress = TwoCaptcha(api_key, defaultTimeout=300, pollingInterval=10)
        self.bal()

    def solve(self, site_key, urls):
        self.bal()
        while sleep(10) or True:
            try:
                res = self.ress.hcaptcha(sitekey=site_key,
                                          url=urls)
                self.id = res['captchaId']
                return res['code']
            except TimeoutException:
                print('captcha Timeout !!!!')
                continue
            except ApiException as e:
                print(e)
                continue

    def bal(self):
        bl = self.ress.balance()
        if bl == 0:
            return sys.exit('balance 2captcha is empety')
        else:
            pass

    def report(self, hasil):
        if hasil == 1:
            self.ress.report(self.id, True)
        if hasil == 0:
            self.ress.report(self.id, False)

class CookieFile():
    def __init__(self, cookie_name, cookie_file='session'):
        if cookie_file:
            if not os.path.isdir(os.path.join(os.getcwd(), cookie_file)):
                os.makedirs(os.path.join(os.getcwd(), cookie_file))

        self.name = os.path.join(os.getcwd(), cookie_file, cookie_name)

    def ada(self):
        return os.path.exists(self.name)

    def save_cookie(self, cok):
        with open(self.name, 'wb') as bb:
            pickle.dump(cok, bb)

    def load_cookie(self):
        with open(self.name, 'rb') as bb:
            bh = pickle.load(bb)
            return bh

class Dropstake:
    server1 = 'https://stake.best/_api/graphql'
    site_key = '7830874c-13ad-4cfe-98d7-e8b019dc1742'
    server2 = "https://stake.best/_api/graphql"
    host = 'https://stake.best/'
    r = httpx.Client()
    ret2 = r.request(
    "POST",
    "https://stake.best/_api/graphql")

    def __init__(self, token, coin: str, prov_capt=1, api_key=None, server=None, UA=None):
        self.cok = CookieFile(token+'.session')

        if not server == None:
            self.server2 = self.server2.replace('stake.ac', server)
            self.host = self.host.replace('stake.ac', server)

        self.s = httpx.Client()
        

        self.s.headers.update({
                  #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                  "X-Access-Token": token
         })

        if UA:
            self.s.headers.update({'User-Agent': UA})
            
        self.t = httpx.Client()
        

        self.t.headers.update({
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                  "X-Access-Token": token
         })

        if UA:
            self.t.headers.update({'User-Agent': UA})

        if prov_capt == 0:
            self.capt = Anti_captcha(api_key)
        if prov_capt == 1:
            self.capt = capt2(api_key)

        if self.cok.ada():
            anu = self.cok.load_cookie()
            for cok in anu:
                self.s.cookies.set_cookie(cok)

        self.coin = coin.lower()

    def genLock(self):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ABC = abc+abc.lower()+'0123456789'
        return ''.join([choice(ABC) for i in range(20)])
    
    def _hajarMamah(self, data=None):
        """ """
        retries = 0
        while True:
            retries += 1
            try:
                ret = self._r.post("https://stake.best/_api/graphql", json=data)
                badungbangpak = ret.json()
            except Exception as err:
                if retries <= 3:
                    continue
                else:
                    BLFormatter(err)
            else:
                if "errors" in badungbangpak:
                    return dict(success=False, errors=badungbangpak["errors"])
                else:
                    # return (success==True, **badungbangpak["data"])
                    return dict(success=True, **badungbangpak["data"])
    
    def ClaimDrop(self, code):
        with self.s as c:
            data = {
                "operationName": "ClaimConditionBonusCode",
                "query": "mutation ClaimConditionBonusCode($code: String!, $currency: CurrencyEnum!, $captcha: String!) {\n  claimConditionBonusCode(code: $code, currency: $currency, captcha: $captcha) {\n    bonusCode {\n      id\n      code\n      __typename\n    }\n    amount\n    currency\n    user {\n      id\n      balances {\n        available {\n          amount\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                "variables": {
                    "code": code,
                    "currency": self.coin,
                    "captcha": self.capt.solve(self.site_key, self.host+f'settings/offers?type=drop&code=100billion&currency={self.coin}&modal=redeemBonus')
                }
            }
            headers = {
                'content-length': str(len(str(data)))
            }

            r = c.post(self.server2, json=data, headers=headers, timeout=7)
            try:
                res = r.json()
                if 'errors' in res.keys():
                    pesan = res['errors'][0]['message']
                    if 'claimConditionBonusCode' in res['errors'][0]['path'] and 'You have not wagered enough in the last week' in pesan:
                        raise NotEnougt(pesan)
                    elif 'Variable "$captcha" got invalid value' in pesan:
                        self.capt.report(0)
                        raise CaptchaInvalid(pesan)
                    else:
                        raise Kesalahan(pesan)


            except json.decoder.JSONDecodeError:
                return r.text, None

            else:
                try:
                    clm = res['data']['claimConditionBonusCode']['amount']
                    id = res['data']['claimConditionBonusCode']['id']
                    return clm, id
                except KeyError:
                    return clm, None

    def account(self):
        """Get accounts information

        :param target: username target

        :return: accounts detail if successful, None Otherwise
        :rtype: dict, optional

        """
        with self.t as t:
            data = {
                "query": "query SendTipMeta($name: String) {\n  user(name: $name) {\n    id\n  }\n  self: user {\n    id\n    name\n    hasTfaEnabled\n    isTfaSessionValid\n    balances {\n      available {\n        amount\n        currency\n      }\n    }\n  }\n}\n",
                "operationName": "SendTipMeta",
                "variables": {},
            }
            ret = t.post(self.server1, json=data, timeout=7)
            #print(ret)

            if "errors" in ret.json():
                if ret.json()["errors"][0]["errorType"] == "disabledSession":
                    print("  [!!] Fail: Session disabled!")
                else:
                    print(
                        f"  [!!] Fail: {ret.json()['errors'][0]['errorType']}\n"
                        f"  **** {ret.json()['errors'][0]['message']}"
                    )
                return
            else:
                data = ret.json()["data"]
                if not data["user"]:
                    return
                else:
                    me = [
                        data["self"]["id"],
                        data["self"]["name"],
                        {
                            currency: amount
                            for amount, currency in [
                                i["available"].values()
                                for i in data["self"]["balances"]
                            ]
                        },
                        data["self"]["hasTfaEnabled"],
                    ]
                    # target = [
                    #     data["user"]["id"],
                    #     data["user"]["name"]
                    # ]
                    #targetId = data["user"]["id"]

                    return {"me": me}

class DB:
    @staticmethod
    def save_data(data, nama_file='DATA.json'):
        with open(nama_file, 'w') as file:
            json.dump(data, file, sort_keys=False, indent=4)
            file.close()

    @staticmethod
    def load_data(nama_file='DATA.json'):
        with open(nama_file, 'r') as file:
            rest = json.load(file)
            file.close()
            return rest

    @staticmethod
    def history_save(data, file='history.json'):
        with open(file, 'w') as fil:
            json.dump(data, fil, sort_keys=False, indent=4)
            fil.close()

    @staticmethod
    def history_load(file='history.json'):
        with open(file, 'r') as fil:
            rest = json.load(fil)
            fil.close()
            return rest
                    
def run(token, api_key, coin, captcha, identifer, server, code, ua):
    TOKEN = "5702690829:AAFc9S9wAL7tCAGmOG4zLXmgmTHCVFOkLwc"
    chat_id = "-1001873261891"
    jk = Dropstake(token, coin, captcha, api_key, server, ua)
    accounts = jk.account()
    if not accounts:
        return
    else:
        myId, myUname, myBalances, use2fa = accounts["me"]
    #print(f'{biru}[{identifer}] {biru3}{myUname}{rs} => {ij}run') #,flush=True,end='\r')
    while True:
        try:
            print(f'{biru}[{identifer}] {biru3}{myUname}{rs} => {ij}run')
            try:
                pay, clm = jk.ClaimDrop(code)
                print(f'{ij}[{identifer}] {myUname} {kn}=> {ij}claim: {pay:8f} amo: {myBalances[coin] + pay:8f} {coin.upper()}')
                #response = requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + f"Username : {myUname}\nBalance : {myBalances[coin]:.8f} {coin.upper()}\nClaimed: {pay:8f} {coin.upper()}\nCode : {code}")
                sys.exit()
            except CaptchaInvalid as e:
                print(f'{ij}{myUname} => captcha failed\ntrying again')
                print(f'{ij}{myUname} => {rd}{e}')
                sys.exit(" setres !")

            except NotEnougt as e:
                print(f'{ij}{myUname} => {rd}{e}')
                print(f'{rs}kill this process => {rd}{identifer}')
                sys.exit()

            except ApiException as e:
                print(f'{rs}{ij}{myUname} => {rd}{e}')
                sys.exit(" setres parah !")

            except Kesalahan as e:
                print(f'{ij}[{identifer}] {kn}{myUname} => {rd}{e}')
                #open("result1.json","w").write(f"{identifer} {myUname} => {e} \n")
                #response = requests.get("https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + f"Username : {myUname}\nBalance : {myBalances[coin]:.8f} {coin.upper()}\nError : {e}")
                sys.exit()

        except json.decoder.JSONDecodeError as babi:
            print(babi)
            print(f'akun {identifer} => Koneksi bermasalah !!!')
            print(f'akun {identifer} => mengulang dalam 10 detik')
            #sleep(10)
            sys.exit()

        except KeyboardInterrupt:
            sys.exit("exit")


def setting():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    anu = DB.load_data()
    print('setting')
    print(f'[1] coin => {anu["coin"]}')
    print(f'[2] captcha provider => {"2captcha" if anu["api Captcha"]["2captcha"] else "Anti-captcha"}')
    print(f'[3] API key provider => {anu["api Captcha"]["api key"]}')
    print(f'[4] server => {anu["server"]}')
    print(f'[5] user agent => {anu["user-agent"]}')
    print('[6] back')
    while True:
        pil = input('masukan pilihan: ')
        if pil == '1':
            pl = input('coin: ')
            anu['coin'] = pl
            DB.save_data(anu)
            setting()
        elif pil == '2':
            os.system('cls' if sys.platform == 'win32' else 'clear')
            print('[1] 2captcha')
            print('[2] anti-captcha')
            pil = input('pilih provider: ')
            while True:
                if pil == '1':
                    anu['api Captcha']['2captcha'] = True
                    anu['api Captcha']['Anti-captcha'] = False
                    DB.save_data(anu)
                elif pil == '2':
                    anu['api Captcha']['2captcha'] = False
                    anu['api Captcha']['Anti-captcha'] = True
                    DB.save_data(anu)
                else:
                    print('pilihan tidak benar !!!!')
                    continue
                setting()

        elif pil == '3':
            pil = input('masukan api key: ')
            anu['api Captcha']['api key'] = pil
            DB.save_data(anu)
            setting()

        elif pil == '4':
            pil = input('masukan server: ')
            anu['server'] = pil
            DB.save_data(anu)
            setting()

        elif pil == '5':
            pil = input('masukan user-agent: ')
            anu['user-agent'] = pil
            DB.save_data(anu)
            setting()

        elif pil == '6':
            return menu()

def menu():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    #print('[1] add akun')
    #print('[2] run')
    #print('[3] setting')
    #print('[4] remove akun')
    #print('[5] add cookie')
    pilih = '2' #input('masukan pilihan: ')
    if pilih == '1':
        anu = DB.load_data()
        while True:
            token = input('masukan token: ')
            if len(token) <= 60:
                print('token tidak falid !!!!')
                continue
            break
        anu['akun'].append(token)
        DB.save_data(anu)
        menu()
    elif pilih == '2':
        #os.system('cls' if sys.platform == 'win32' else 'clear')
        anu = DB.load_data()
        api_capt = anu['api Captcha']
        api_key = api_capt['api key']
        coin = anu['coin']
        server = anu['server'] or 'stake.ac'
        UA = anu["user-agent"]
        print(f"""{war}
{putih}author           : {hijau}Iqbalmedukzzz
{putih}contact          : {hijau}Meduk @Eskowsharkbaby
{putih}update           : {hijau}Versi 4.3
""")
        code = input('masukan code: ')
        #os.system('cls' if sys.platform == 'win32' else 'clear')
        if api_capt['2captcha']:
            cpt = 1
        if api_capt['Anti-captcha']:
            cpt = 0

        inden = 0
        pp = []
        for i in anu['akun']:
            p = Process(target=run, args=(i, api_key, coin, cpt, inden, server, code, UA,))
            pp.append(p)
            p.start()
            inden += 1
        while True:
            try:
                if pp:
                    for proc in pp:
                        if proc == -signal.SIGTERM:
                            pp.remove(proc)

                else:
                    return Main()
                if False in [i.is_alive() for i in pp]:
                    sys.exit("close the account !!!")
                    #pass
                    #return Main()
            except KeyboardInterrupt:
                for ii in pp:
                    if ii.is_alive():
                        ii.terminate()
                sys.exit("exiting the account !!!")

    elif pilih == '3':
        return setting()

    elif pilih == '4':
        os.system('cls' if sys.platform == 'win32' else 'clear')
        anu = DB.load_data()
        for i in anu['akun']:
            print(f'[{anu["akun"].index(i)}] {i}')
        while True:
            pil = input('pilih nomer atau nama akun: ')
            if pil.isnumeric():
                if int(pil) >= len(anu['akun']):
                    print('no tidak ada !!!')
                    continue
                anu['akun'].pop(int(pil))
            else:
                if len(pil) <= 20:
                    print('akun tidak falid')
                    continue
                try:
                    anu['akun'].remove(pil)
                except ValueError:
                    print('akun tidak ada')
                    continue

            DB.save_data(anu)
            return Main()
    elif pilih == '5':
        anu = DB.load_data()
        server = anu['server']
        while True:
            os.system('cls' if sys.platform == 'win32' else 'clear')
            cook = []
            for i in anu['akun']:
                cc = CookieFile(i+'.session')
                cook.append(cc)
                print(f'[{anu["akun"].index(i)}] {i} {"✅" if cc.ada() else ""}')
            pil = input('pilih nomer atau nama akun: ')
            if pil.isnumeric():
                if int(pil) >= len(anu['akun']):
                    print('no tidak ada !!!')
                    time.sleep(1)
                    return Main()
                name = anu['akun'][int(pil)]
                cok = input('masukan cookie: ')
                if ';' in cok and '=' in cok:
                    ck = []
                    for cookie in [rq.cookies.create_cookie(name, value, domain=server, path='/') 
                                       for name, value in re.findall(r'(.+?)=(.+?)?;', cok)]:
                        ck.append(cookie)
                    cook[int(pil)].save_cookie(ck)
            else:
                if len(pil) <= 20:
                    print('akun tidak falid')
                    continue
                try:
                    nomor = anu['akun'].index(pil)
                    cok = input('masukan cookie: ')
                    if ';' in cok and '=' in cok:
                        ck = []
                        for cookie in [rq.cookies.create_cookie(name, value, domain=server, path='/') 
                                       for name, value in re.findall(r'(.+?)=(.+?)?;', cok)]:
                            ck.append(cookie)
                        cook[nomor].save_cookie(ck)
                except ValueError:
                    print('akun tidak ada')
                    continue

def Main():
    if not os.path.isfile('DATA.json'):
        data = {
            'akun': [],
            'coin': 'trx',
            'api Captcha': {
                'api key': None,
                '2captcha': True,
                'Anti-captcha': False
            },
            'server': 'stake.ac',
            'user-agent': None
        }
        DB.save_data(data)
    anu = DB.load_data()
    if not anu['api Captcha']['api key']:
        setting()
    menu()


if __name__ == '__main__':
    Main()
