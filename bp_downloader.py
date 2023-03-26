# -*- coding: utf-8 -*-
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile, QTimer
#from PySide6.QtUiTools import QUiLoader
from osu_apy_v2 import OsuApiV2
from _thread import start_new_thread
from mainui import Ui_MainWindow
from oauth_configui import Ui_Dialog
from shutil import copyfile
import webbrowser
import tempfile
import time
import os
import re
import subprocess

class SetAuthWindow(QDialog):
    def __init__(self):
        super(SetAuthWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('OSU BP下载器')
        self.ui.apply.clicked.connect(self.set_oauth)
        self.ui.pushButton.clicked.connect(self.open_gh)

    def set_oauth(self):
        client_id = self.ui.lineEdit.text()
        secret = self.ui.lineEdit_2.text()
        with open('oauth', 'w+') as f:
            f.write(client_id + '\n' + secret)
        w.init_osu_api()

    def open_gh(self):
        webbrowser.open_new('https://github.com/QLchedan/OsuBestplayDownloader') 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.bp = [0]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.saw = None
        self.tasks = 0
        self.is_downloading = False
        self.ui.progressBar.setValue(0)
        self.setWindowTitle('OSU BP下载器')
        self.ui.get_bp_button.clicked.connect(self.get_bp)
        self.ui.oauth_config_btn.clicked.connect(self.set_oauth)
        self.ui.btn_save_as_osz.clicked.connect(self.sel_osz_path)
        self.ui.btn_save_to_osu.clicked.connect(self.sel_osu_path)
        self.ui.download_all_button.clicked.connect(self.start_download)
        self.ui.progressBar.setRange(0, 100)
        self.done = 0
        self.t = 0
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
    
    def closeEvent(self, event):
        os.system('taskkill /F /IM aria2c.exe')
        event.accept()

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
        self.t = time.time()
        self.is_downloading = True
        if self.ui.down_from_sayo.isChecked():
            self.ui.down_status_label.setText('下载中')
            self.done = 0
            start_new_thread(self.downloading, (0,))

    def downloading(self, n):
        self.down_from_sayo = self.ui.down_from_sayo.isChecked()
        bp = list(set(self.bp))
        k = 0
        while True:
            if k - self.done <= 4:
                for i in range(5):
                    self.tasks += 1
                    start_new_thread(self.download, (k,))
                    k += 1
            if self.done == len(bp):
                break
        

    def download(self, i):
        if self.ui.down_from_sayo.isChecked():
            bp = list(set(self.bp))
            map_id = bp[i]
            idx = self.bp.index(map_id)
            filename = str(map_id) + ' ' + self.composer[idx] + ' - ' + self.songname[idx]
            filename = re.sub('[*?"<>]', '', filename)
            filename = re.sub('[\/|~:]', '_', filename)
            if '.' in filename:
                filename = filename.replace('.', '')
            url = 'https://txy1.sayobot.cn/download/osz/' + str(map_id)
            #dir_ = '"' + self.ui.save_as_osz_textedit.text() + '"'
            filename_a = '"' + filename + '.osz"'
            with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmpdir:
                try:
                    #os.system('.\\aria2c.exe -x2 -o ' + filename_a + ' -d "' + tmpdir + '" ' + url)
                    res = subprocess.Popen('.\\aria2c.exe -x5 -o ' + filename_a + ' -d "' + tmpdir + '" ' + url, shell=True)
                    r_code = res.wait()
                    if self.ui.save_as_osz_checkbox.isChecked():
                        print(os.listdir(tmpdir))
                        copyfile(tmpdir + '\\' + filename + '.osz', self.ui.save_as_osz_textedit.text() + '/' + filename + '.osz')
                    if self.ui.save_to_osu_checkbox.isChecked():
                        if os.path.exists(self.ui.save_to_osu_textedit.text()) and not os.path.exists(self.ui.save_to_osu_textedit.text() + '/' + filename):
                            os.mkdir(self.ui.save_to_osu_textedit.text() + '/' + filename)
                            #unpack_archive(tmpdir + '\\' + filename + '.osz', self.ui.save_to_osu_textedit.text() + '/' + filename)
                            os.system('.\\7z.exe x "' + tmpdir + '\\' + filename + '.osz" ' + '-o"' + self.ui.save_to_osu_textedit.text() + '/' + filename + '"')
                except:
                    pass
            self.done += 1
            self.tasks -= 1
        else:
            pass
    
    def progress_display(self):
        self.ui.progressBar.setValue(round(100 * (self.done / len(list(set(self.bp))))))
        if self.done == len(list(set(self.bp))):
            ti = round(time.time() - self.t)
            self.ui.down_status_label.setText('下载完成。共用时' + str(ti) + '秒')
            self.done = 0
            self.is_downloading = False
        

if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = MainWindow()
    w.show()
    app.exec()
