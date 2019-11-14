import zlib
import base64
import json
import requests
import time
import hashlib
import threading
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Frame_rename import *
# TODO 修改为async方式异步登录

# TODO 动态获取游戏人物姓名
name_data = {"\u9b5f": "\u6276\u6851", "\u9cbc": "\u5c71\u57ce", "\u9ccc": "\u4f0a\u52bf", "\u87af": "\u65e5\u5411",
             "\u59c8": "\u91d1\u521a", "\u59b8": "\u6bd4\u777f", "\u59b1": "\u699b\u540d", "\u59cf": "\u96fe\u5c9b",
             "\u51f0": "\u8d64\u57ce", "\u9e3e": "\u52a0\u8d3a", "\u51e4": "\u7965\u51e4", "\u9e5e": "\u745e\u51e4",
             "\u7352": "\u9ad8\u96c4", "\u72ac": "\u7231\u5b95", "\u72ae": "\u6469\u8036", "\u730b": "\u9e1f\u6d77",
             "\u8c7a": "\u5929\u9f99", "\u8c79": "\u9f99\u7530", "\u72f8": "\u5317\u4e0a", "\u737e": "\u5927\u4e95",
             "\u8c89": "\u4e94\u5341\u94c3", "\u72d0": "\u5915\u5f20", "\u6850": "\u5439\u96ea",
             "\u6749": "\u767d\u96ea", "\u6768": "\u521d\u96ea", "\u68a7": "\u6df1\u96ea ", "\u67ab": "\u6653",
             "\u6800": "\u54cd", "\u6893": "\u96f7", "\u67cf": "\u7535", "\u67da": "\u7eeb\u6ce2",
             "\u67ff": "\u6577\u6ce2", "\u9ca8": "\u957f\u95e8", "\u9c9e": "\u9646\u5965", "\u9e69": "\u5927\u51e4",
             "\u67ad": "\u9f99\u9aa7", "\u72fc": "\u53e4\u9e70", "\u72cc": "\u52a0\u53e4", "\u72b9": "\u9752\u53f6",
             "\u7305": "\u8863\u7b20", "\u51ca": "\u5ddd\u5185", "\u51c9": "\u795e\u901a", "\u51c1": "\u90a3\u73c2",
             "\u691b": "\u79cb\u6708", "\u680e": "\u51c9\u6708", "\u8429": "\u9633\u708e",
             "\u84b2": "\u4e0d\u77e5\u706b", "\u84c9": "\u9ed1\u6f6e", "\u83b2": "\u96ea\u98ce",
             "\u9e6c": "\u745e\u9e64", "\u9e64": "\u7fd4\u9e64", "\u9e34": "\u98de\u9f99", "\u9e37": "\u82cd\u9f99",
             "\u9cb8": "\u4fe1\u6d53", "\u9e31": "\u98de\u9e70", "\u9e22": "\u96bc\u9e70", "\u9e4f": "\u51e4\u7fd4",
             "\u7328": "\u6700\u4e0a", "\u72fb": "\u4e09\u9688", "\u72fa": "\u94c3\u8c37", "\u7301": "\u718a\u91ce",
             "\u72d4": "\u9999\u53d6", "\u6dc0": "\u5927\u6dc0", "\u677e": "\u7766\u6708", "\u6c40": "\u767d\u9732",
             "\u6d5c": "\u65f6\u96e8", "\u6c50": "\u6751\u96e8", "\u6c3f": "\u5915\u7acb", "\u840d": "\u5c9a",
             "\u8292": "\u5c9b\u98ce", "\u68cc": "\u5cf0\u98ce", "\u6759": "\u5bb5\u6708", "\u9b23": "\u5999\u9ad8",
             "\u9e70": "\u795e\u9e70", "\u7afa": "\u7af9", "\u677a": "\u521d\u6708"}
name_dict = ['魟', '鲼', '鳌', '螯', '姈', '妸', '妱', '姏', '凰', '鸾', '凤', '鹞', '獒', '犬', '犮', '猋', '豺', '豹', '狸', '獾', '貉',
             '狐', '桐', '杉', '杨', '梧', '枫', '栀', '梓', '柏', '柚', '柿', '鲨', '鲞', '鹩', '枭', '狼', '狌', '犹', '猅', '凊', '凉',
             '凁', '椛', '栎', '萩', '蒲', '蓉', '莲', '鹬', '鹤', '鸴', '鸷', '鲸', '鸱', '鸢', '鹏', '猨', '狻', '狺', '猁', '狔', '淀',
             '松', '汀', '浜', '汐', '氿', '萍', '芒', '棌', '杙', '鬣', '鹰', '竺', '杺']


class Windows_rename(QMainWindow, Ui_Frame_rename):
    def __init__(self):
        super(Windows_rename, self).__init__()
        self.setupUi(self)


class Game_login():
    def __init__(self):
        self.version = "3.8.0"
        self.headers = {'Accept-Encoding': 'identity',
                        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; Lenovo A7600-m Build/LRX21M)'}
        self.cookies = None
        self.channel = '100016'
        self.server = None
        self.login_url_head = None
        self.allShip = {}
        self.rightName = {}

    def ready_login(self, username, password, server):
        self.server = "http://s" + str(server) + '.jr.moefantasy.com/'
        self.get_version_data()
        self.login(username, password)

    def get_version_data(self):
        """
        功能：获取版本号和登陆地址
        无返回值
        """
        url_version = 'http://version.jr.moefantasy.com/index/checkVer/3.8.1/100016/2&version=3.8.1&channel=100016&market=2'
        while True:
            try:
                windows_rename.list_log.addItem('Connectiing version server...')
                response_version = requests.get(url=url_version, headers=self.headers)
            except Exception as Error_information:
                windows_rename.list_log.addItem('Get version FAILED! Reason:', Error_information)
                windows_rename.list_log.addItem('60s after will try again')
                time.sleep(60)
                continue
            response_version = response_version.text
            response_version = json.loads(response_version)
            self.version = response_version['version']['newVersionId']
            self.login_url_head = response_version['loginServer']
            windows_rename.list_log.addItem('Connect version server success!')
            break

    def login(self, username, password):
        """
        功能：登录游戏并返回cookies
        无返回值
        """
        # TODO 修改为最新方式
        login_dict = {'username': base64.b64encode(username.encode()), 'pwd': base64.b64encode(password.encode())}
        login_url = self.login_url_head + 'index/passportLogin/' + self.get_url_end()
        # login_dict：登录密码字典  login_url:登录url
        while True:
            try:
                windows_rename.list_log.addItem('Connectiing login server...')
                login_response = requests.post(url=login_url, data=login_dict, headers=self.headers)
                self.cookies = login_response.cookies.get_dict()
                break
            except Exception as Error_information:
                windows_rename.list_log.addItem('Login FAILED! Reason:', Error_information)
                windows_rename.list_log.addItem("30s after will try again")
                time.sleep(30)
                continue
        windows_rename.list_log.addItem('Login successed!')

    def get_user_data(self):
        """
        功能：首次登陆获取信息
        无返回值
        """
        windows_rename.list_log.addItem('Getting user data...')
        while True:
            user_data = {}
            try:
                user_data = zlib.decompress(
                    requests.get(url=self.server + 'api/initGame?&crazy=0' + self.get_url_end(), headers=self.headers,
                                 cookies=self.cookies).content)
                break
            except Exception as Error_information:
                windows_rename.list_log.addItem('Get user data FAILED! Reason:', Error_information)
                time.sleep(30)
                continue
        user_data = json.loads(user_data)
        for eachShip in user_data['userShipVO']:
            self.allShip[eachShip['id']] = eachShip['title']

        for shipId, shipName in self.allShip.items():
            if shipName in name_dict:
                self.rightName[shipId] = {'old': shipName, 'new': name_data[shipName]}

        num = 0
        for shipId, shipName in self.rightName.items():
            windows_rename.list_log.addItem('Rename...' + shipName['old'] + "→" + shipName['new'])
            num = num + 1
            value = int((num / len(self.rightName) * 100))
            windows_rename.progressBar.setValue(value)
            url = game_login.server + "boat/renameShip/" + str(shipId) + "/" + hex_encode(
                shipName['new']) + "/" + game_login.get_url_end()
            requests.get(url=url, headers=game_login.headers, cookies=game_login.cookies)

    def get_url_end(self):
        """
        功能：返回url尾部
        返回值：文本型
        """
        url_time = str(int(round(time.time() * 1000)))
        md5_raw = url_time + 'ade2688f1904e9fb8d2efdb61b5e398a'
        md5 = hashlib.md5(md5_raw.encode('utf-8')).hexdigest()
        url_end = '&t={time}&e={key}&gz=1&market=2&channel={channel}&version={version}'
        url_end_dict = {'time': url_time, 'key': md5, 'channel': self.channel, 'version': self.version}
        url_end = url_end.format(**url_end_dict)
        return url_end


def hex_encode(s):
    byte = bytes(s, 'utf-8')
    hexs = ''.join(["%02X" % x for x in byte]).strip()
    lists = list(hexs)
    result = ''
    for i in range(0, len(hexs), 2):
        result = result + '%' + lists[i] + lists[i + 1]
    return result


def rename():
    def run():
        try:
            server = str(int(windows_rename.cb_server.currentIndex()) + 2)
            game_login.ready_login(username=windows_rename.ed_username.text(),
                                   password=windows_rename.ed_password.text(), server=server)
            game_login.get_user_data()
        except Exception as e:
            print(e)

    windows_rename.bt_login.setVisible(False)
    threading.Thread(target=run).start()


app = QtWidgets.QApplication(sys.argv)
windows_rename = Windows_rename()
game_login = Game_login()
windows_rename.bt_login.clicked.connect(rename)
windows_rename.show()
sys.exit(app.exec_())
