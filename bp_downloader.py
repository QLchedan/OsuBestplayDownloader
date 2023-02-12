from PySide6.QtWidgets import *
from PySide6.QtCore import QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from osu_apy_v2 import OsuApiV2
from _thread import start_new_thread
from mainui import Ui_MainWindow
from oauth_configui import Ui_Dialog
from io import BytesIO
import time
import os
import requests
import zipfile
import re

class SetAuthWindow(QDialog):
    def __init__(self):
        super(SetAuthWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('OSU BP下载器')
        self.ui.apply.clicked.connect(self.set_oauth)

    def set_oauth(self):
        client_id = self.ui.lineEdit.text()
        secret = self.ui.lineEdit_2.text()
        with open('oauth', 'w+') as f:
            f.write(client_id + '\n' + secret)
        w.init_osu_api()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.saw = None
        self.ui.progressBar.setValue(0)
        self.setWindowTitle('OSU BP下载器')
        self.ui.get_bp_button.clicked.connect(self.get_bp)
        self.ui.oauth_config_btn.clicked.connect(self.set_oauth)
        self.ui.btn_save_as_osz.clicked.connect(self.sel_osz_path)
        self.ui.btn_save_to_osu.clicked.connect(self.sel_osu_path)
        self.ui.download_all_button.clicked.connect(self.start_download)
        self.ui.progressBar.setRange(0, 100)
        self.done = 0
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.progress_display)
        self.init_osu_api()

    def init_oauth(self):
        
        with open('oauth', 'r') as f:
            oauth = f.read().split('\n')
            print('当前oauth: ' + str(oauth))
        if len(oauth) != 2:
            oauth = -1
        return oauth

    def init_osu_api(self):
        oauth = self.init_oauth()
        if oauth == -1:
            QMessageBox.warning(self, 'OSU BP下载器', '未设置OAuth密钥, 点击 配置OAuth 进行设置')
        else:
            self.api = OsuApiV2(int(oauth[0]), oauth[1])

    def get_bp(self):
        mode_txt = self.ui.game_mode.currentText()
        mode = str()
        if mode_txt == '默认':
            mode = ''
        elif mode_txt == 'standard':
            mode = '&mode=osu'
        elif mode_txt == 'mania':
            mode = '&mode=mania'
        elif mode_txt == 'taiko':
            mode = '&mode=taiko'
        else:
            mode = '&mode=catch'
        self.bp = list()
        self.composer = list()
        self.songname = list()
        self.done = 0
        osu_id = self.ui.osu_id.text()
        user_id = self.api.get_user_id(osu_id)
        res = self.api.get(f"/users/{user_id}/scores/best?limit=100" + mode)
        content = res.json()
        for i in range(len(content)):
            self.bp.append(str(content[i]['beatmap']['beatmapset_id']))
            self.composer.append(content[i]['beatmapset']['artist'])
            self.songname.append(content[i]['beatmapset']['title'])
            item = QTableWidgetItem(content[i]['beatmapset']['title'])
            self.ui.table.setItem(i, 0, item)
            item = QTableWidgetItem(content[i]['beatmap']['version'])
            self.ui.table.setItem(i, 1, item)
            item = QTableWidgetItem(', '.join(content[i]['mods']))
            self.ui.table.setItem(i, 2, item)
            item = QTableWidgetItem(str(content[i]['beatmap']['difficulty_rating']))
            self.ui.table.setItem(i, 3, item)
            item = QTableWidgetItem(content[i]['beatmapset']['creator'])
            self.ui.table.setItem(i, 4, item)
            item = QTableWidgetItem(str(content[i]['beatmap']['beatmapset_id']))
            self.ui.table.setItem(i, 5, item)

    def set_oauth(self):
        if self.saw is None:
            self.saw = SetAuthWindow()
        self.saw.show()
        

    def sel_osz_path(self):
        file_path = QFileDialog.getExistingDirectory(
             self,
             "选择存储路径",
             os.getcwd()
        )
        self.ui.save_as_osz_textedit.setText(file_path)

    def sel_osu_path(self):
        file_path = QFileDialog.getExistingDirectory(
             self,
             "选择存储路径",
             os.getcwd()
        )
        self.ui.save_to_osu_textedit.setText(file_path)

    def start_download(self):
        if self.ui.down_from_sayo.isChecked():
            self.done = 0
            start_new_thread(self.downloading, (0,))
            #start_new_thread(self.progress_display, (0,))

    def downloading(self, n):
        self.down_from_sayo = self.ui.down_from_sayo.isChecked()
        for k in range(len(self.bp)):
            start_new_thread(self.download, (k,))
            time.sleep(2)
        

    def download(self, i):
        if self.ui.down_from_sayo.isChecked():
            map_id = self.bp[i]
            if len(str(map_id)) >= 5:
                path = str(map_id)[0:-4] + '/' + str(map_id)[-4:len(str(map_id))]
            else:
                path = '0/' + str(map_id)
            filename = str(map_id) + ' ' + self.composer[i] + ' - ' + self.songname[i]
            filename = re.sub('[\/:*?"<>|]', '', filename)
            if self.done % 3 == 0:
                file = requests.get('https://tc2.sayobot.cn:25225/beatmaps/' + path + '/novideo').content
            elif self.done % 3 == 1:
                file = requests.get('https://b4.sayobot.cn:25225/beatmaps/' + path + '/novideo').content
            else:
                file = requests.get('https://b11.sayobot.cn:25225/beatmaps/' + path + '/novideo').content
            if self.ui.save_as_osz_checkbox.isChecked():
                with open(self.ui.save_as_osz_textedit.text() + '/' + filename + '.osz', 'wb+') as f:
                    f.write(file)
            if self.ui.save_to_osu_checkbox.isChecked():
                zip_file = zipfile.ZipFile(BytesIO(file))
                if os.path.exists(self.ui.save_to_osu_textedit.text()) and not os.path.exists(self.ui.save_to_osu_textedit.text() + '/' + filename):
                    os.mkdir(self.ui.save_to_osu_textedit.text() + '/' + filename)
                    for k in zip_file.namelist():
                        zip_file.extract(k, self.ui.save_to_osu_textedit.text() + '/' + filename)
            self.done += 1
            #self.ui.progressBar.setValue(self.done)
        else:
            pass
    
    def progress_display(self):
        self.ui.progressBar.setValue(self.done)

if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = MainWindow()
    w.show()
    app.exec()